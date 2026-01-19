create table clientes (
	id SERIAL primary key,
	nombre VARCHAR(100),
	ciudad VARCHAR(50));

create table pedidos (
	id SERIAL primary key,
	cliente_id integer,
	fecha date,
	total numeric,
	foreign key (cliente_id) references clientes(id));

INSERT INTO clientes (nombre, ciudad) VALUES
('Juan Pérez', 'Santiago'),
('María González', 'Valparaiso'),
('Carlos Rojas', 'Concepción'),
('Ana Torres', 'La Serena'),
('Pedro Muñoz', 'Antofagasta');

--insertar clientes y pedidos faltantes
insert into clientes(nombre,ciudad) values ('Ashly Reyes', 'Santiago');
insert into clientes(nombre,ciudad) values ('Alberto Fernandez', 'Santiago');
insert into pedidos(cliente_id,fecha,total) values (6, '2026-01-19', 79990);

INSERT INTO pedidos (cliente_id, fecha, total) values 
(1, '2026-01-10', 45990),
(1, '2026-01-15', 12990),
(2, '2026-01-12', 89990),
(3, '2026-01-14', 25990),
(4, '2026-01-16', 34990),
(5, '2026-01-18', 19990),
(2, '2026-01-19', 49990);

-- Se cambia el dato de la ciudad para sacarle los acentos
update clientes
set ciudad = 'Valparaiso'
where ciudad = 'Valparaíso';

update clientes
set ciudad = 'Concepcion'
where ciudad = 'Concepción';

update pedidos
set total = 120000
where cliente_id = 6;

select * from pedidos;
select * from clientes;

--Se consulta clientes que son de Valparaiso
select nombre from clientes
where ciudad = 'Valparaiso';

--Se consulta el nombre del cliente con id=3
select nombre from clientes
where id = 3;

--Contabiliza cuantos clientes existen en la tabla
select count(id) from clientes;

--Se consulta cuales ciudades estan en la tabla
select DISTINCT(ciudad) from clientes;

--Se consulta cuantos clientes hay por ciudad
select ciudad, count(ciudad) from clientes
group by ciudad;

-- Consultas JOIN

--Se consulta todos los pedidos hechos por los clientes
select cli.nombre,
pe.id,pe.fecha ,pe.total  from  pedidos pe
join clientes cli
ON pe.cliente_id = cli.id;

--Se consulta los pedidos hechos por clientes de Santiago
select cli.nombre,
pe.id ,pe.fecha ,pe.total  from  pedidos pe
join clientes cli
ON pe.cliente_id = cli.id
where cli.ciudad = 'Santiago';

-- Consulta para obtener el total de pedidos por clientes
select cli.nombre,count(pe.id) as "Cantidad de pedidos", sum(pe.total) as "Suma total de gastado en los pedidos" from  pedidos pe
join clientes cli
ON pe.cliente_id = cli.id
group by cli.nombre;

--Consulta para obtener todos los datos del cliente con los datos de los pedidos trayendo aun el cliente que no haya hecho pedidos
select cli.*, pe.* from clientes cli
left join pedidos pe
on cli.id = pe.cliente_id

--Consulta para obtener al cliente que 
select cli.nombre,count(pe.id) as "Cantidad de pedidos", sum(pe.total) as "Suma total de gastado en los pedidos" from  pedidos pe
join clientes cli
ON pe.cliente_id = cli.id
group by cli.nombre
having sum(pe.total) > 100000;





	



