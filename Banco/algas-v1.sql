drop database algas;

create database algas;
use algas;
create table dados (
idDados int primary key auto_increment,
entrada int,
tempo float,
memoria float,
data_insercao date
);

select * from dados;

select Count(idDados) from dados;
