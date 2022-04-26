CREATE TABLE estado (
	uf char(2) primary key
);

CREATE TABLE dados (
	idDados int primary key auto_increment,
    	entrada int,
    	tempo float,
    	memoria float,
    	etnia varchar(20),
    	idade varchar(20),
    	sexo char(1),
    	grupo_risco boolean,
    	febre boolean,
    	coriza boolean,
    	dor_muscular boolean,
    	tosse boolean,
    	variante varchar(20),
    	classe_social varchar (20),
    	fk_estado char(2),
    	FOREIGN KEY (fk_estado) references estado(uf),
    	data_insercao date
);

CREATE TABLE infos (
	idInfo int primary key auto_increment,
	fk_estado char(2),
	FOREIGN KEY (fk_estado) references estado(uf),
	numero_casos int,
	data_inicio_insercao datetime,
	tempo_execucao time,
	maior_memoria int
);

INSERT INTO estado (uf) VALUES
('AC'),
('AL'),
('AP'),
('AM'),
('BA'),
('CE'),
('DF'),
('ES'),
('GO'),
('MA'),
('MT'),
('MS'),
('MG'),
('PA'),
('PB'),
('PR'),
('PE'),
('PI'),
('RJ'),
('RN'),
('RS'),
('RO'),
('RR'),
('SC'),
('SE'),
('SP'),
('TO');

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
