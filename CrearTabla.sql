
create database escuela;
use escuela;

create table especialidad(
    num char(5) not null,
    nombre char(25) not null,
    primary key (num)
);

create table alumnos(
    num char(5) not null,
    nombre char(25) not null,
    sem char(2),
    numEsp char(5),
    sexo char(1), # M ó H
    primary key(num),
    foreign key (numEsp)
        references especialidad(num)
);

create table profesor(
    num char(5) not null,
    nombre char(25) not null,
    sueldo integer,
    grado char(25),
    primary key(num)
);

create table materia(
    num char(5) not null,
    nombre char(25) not null,
    creditos integer not null,
    numEsp char(25),
    primary key(num),
    foreign key (numEsp)
        references especialidad(num)
);

create table horarios(
    numMat char(5) not null,
    grupo char(2) not null,
    numProf char(5) not null,
    dia char(15) not null,
    hora char(5) not null,
    salon char(5),
    primary key (numMat,grupo),
    foreign key(numMat)
        references materia(num),
    foreign key(numProf)
        references profesor(num)
);

create table calificaciones(
    numAlum char(5)  not null,
    numMat  char(5)  not null,
    grupo   char(2)  not null,
    periodo char(25) not null,
    calificacion integer,
    primary key(numAlum, numMat, grupo, periodo),
    foreign key(numAlum) references alumnos(num),
    foreign key(numMat)  references materia(num)
    #foreign key(grupo)   references horarios(num)
);
