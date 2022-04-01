USE algas;
CREATE TABLE dados (
	idDados int primary key auto_increment,
	entrada int,
	tempo float,
	memoria float,
	data_insercao date
);
SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
