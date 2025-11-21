const listaProductos = document.querySelector('#listaProductos');
const contenidoProductos = document.querySelector('#contenidoProductos');
const emptyCart = document.querySelector('#emptyCart');

// creamos esta variable para mostrar los objetos
let productosArray = [];

document.addEventListener('DOMContentLoaded', function(){
    eventListeners();
})

function eventListeners(){
    listaProductos.addEventListener('click', getDataElements);
    emptyCart.addEventListener('click', function (){
        productosArray = [];
        productosHtml();
        updateCartCount();
        updateTotal();
    });

    const loadProduct = localStorage.getItem('products');
    if (loadProduct){
        productosArray = JSON.parse(loadProduct);
        productosHtml();
    } else {
        productosArray = [];
    }
}

function updateCartCount(){
    const cartCount = document.querySelector('#cartCount');
    cartCount.textContent = productosArray.length;
}

function updateTotal(){
    const total = document.querySelector('#total');
    let totalProduct = productosArray.reduce((total, prod) => total + (prod.precio * prod.cantidad), 0);
    total.textContent = `$${totalProduct}`;
}

//A traves del boton se intenta llegar al div que contiene la clase card para poder seleccionar todos los elementos a obtener
function getDataElements(e){
    if (e.target.classList.contains("btn")){
        const elementHtml = e.target.parentElement.parentElement;
        selectData(elementHtml);
    }
}

function selectData(prod){
    const productObjeto = {
        img : prod.querySelector('img').src,
        titulo : prod.querySelector('h5').textContent,
        precio : parseInt(prod.querySelector('strong').textContent.replace('$', '')),
        id : parseInt(prod.querySelector('button[type="button"]').dataset.id, 10),
        cantidad : 1,
    }

    const exits = productosArray.some(prod => prod.id === productObjeto.id);

    if (exits){
        showAlert('El producto ya se encuentra en el carrito','error');
        return;
    }

    productosArray = [...productosArray, productObjeto];
    showAlert('El producto fue agregado al carrito', 'success');
    productosHtml();
    updateCartCount();
    updateTotal();
    
}

function productosHtml(){
    cleanHtml();
    productosArray.forEach(prod =>{
        const {img, titulo, precio, id, cantidad} = prod;

        //imagen
        const tr= document.createElement('tr');
        const tdImg= document.createElement('td');
        const prodImg = document.createElement('img');
        prodImg.src = img;
        prodImg.alt = 'imagen producto'
        tdImg.appendChild(prodImg)

        //Titulo
        const tdTitulo= document.createElement('td');
        const prodTitulo= document.createElement('p');
        prodTitulo.textContent = titulo;
        tdTitulo.appendChild(prodTitulo);

        //precio
        const tdPrecio= document.createElement('td');
        const prodPrecio= document.createElement('p');
        prodPrecio.textContent = `$${precio * cantidad}`;
        tdPrecio.appendChild(prodPrecio);

        //Cantidad
        const tdCantidad = document.createElement('td');
        const prodCantidad = document.createElement('input');
        prodCantidad.type= 'number';
        prodCantidad.min = '1';
        prodCantidad.value= cantidad;
        prodCantidad.dataset.id = id;
        prodCantidad.oninput = updateCantidad;
        tdCantidad.appendChild(prodCantidad);

        const tdDelete = document.createElement('td');
        const prodDelete = document.createElement('button');
        prodDelete.type = 'button';
        prodDelete.textContent = 'X';
        prodDelete.onclick = () => destroyProduct(id);
        tdDelete.appendChild(prodDelete);


        tr.append(tdImg,tdTitulo,tdPrecio,tdCantidad, tdDelete);

        contenidoProductos.appendChild(tr);
    });
    saveLocalStorage ();
}

function saveLocalStorage () {
    localStorage.setItem('products', JSON.stringify(productosArray));
}

function updateCantidad(e){
    const newCantidad = parseInt(e.target.value, 10);
    const idProd = parseInt(e.target.dataset.id, 10);

    const product = productosArray.find(prod => prod.id === idProd);
    if (product && newCantidad > 0 ){
        product.cantidad = newCantidad;
    }

    productosHtml();
    updateTotal();
    saveLocalStorage();

}

function destroyProduct(idProd) {
    productosArray = productosArray.filter(prod => prod.id !== idProd);
    showAlert('El producto fue eliminado exitosamente','success');
    productosHtml();
    updateCartCount();
    updateTotal();
    saveLocalStorage();
}

function cleanHtml() {
    contenidoProductos.innerHTML = '';
}

function showAlert(message, type) {
    const nonRepeatAlert = document.querySelector('.alert');
    if (nonRepeatAlert) {
        nonRepeatAlert.remove();
    }

    const div = document.createElement('div');
    div.classList.add('alert', type);
    div.textContent = message;

    document.body.appendChild(div);

    setTimeout(() => div.remove(), 5000);
}