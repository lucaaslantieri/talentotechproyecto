create database alumnos_talentotech;

use alumnos_talentotech;

create table alumnos (
    id int primary key auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    email varchar(100) unique not null,
    fecha_nacimiento date not null
);

--prueba para ver si funciona la conexion a la base de datos
insert into alumnos (nombre, apellido, email, fecha_nacimiento) values
('Juan', 'Pérez', 'juan.perez@example.com', '2000-01-01');

select * from alumnos;