-- drop database cal;
create database cal;
use cal;

create table alunos(
alucodigo  int primary key auto_increment not null,
alunome varchar(45),
alumatricula varchar(45),
aluemail varchar(45),
aluserie varchar(45),
alufaltas int
);

create table materias(
matcodigo int primary key auto_increment not null,
matnome varchar(45)not null 
);

create table professores(
procodigo int primary key auto_increment not null,
pronome varchar(45),
promatricula varchar(45),
promateria varchar(45),
proemail varchar(45),
profaltas int,
foreign key(matprocodigo) references materias(matcodigo),
matprocodigo int
);

create table alunosDaTurma(
adtcodigo int primary key not null auto_increment,
adtturcodigo int,
adtalunome varchar(45),
adtturnome varchar(45),
adtpronome varchar(45)
);

create table turmas(
turcodigo int primary key auto_increment not null,
turmatnome varchar(45),
turpronome varchar(45)
);