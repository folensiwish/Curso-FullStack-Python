var clicks = 0;

function onClick() {
clicks += 1;
document.getElementById("clicks").innerHTML = clicks;
};



function oferta(){
 const elemento = document.getElementById('ofertas');
 if (elemento.style.display === 'none') {
   elemento.style.display = 'block';
 } else {
   elemento.style.display = 'none';
 }

}


function toggleModoOscuro()
{
document.body.classList.toggle("oscuro");
}



