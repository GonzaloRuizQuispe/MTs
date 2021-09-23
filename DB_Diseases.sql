CREATE DATABASE db_diseases

CREATE TABLE diseases (
	id_diseases INT AUTO_INCREMENT NOT NULL,
	name VARCHAR (250) NOT NULL,
    trataments VARCHAR (250) NOT NULL,
    causes VARCHAR (250) NOT NULL,
    symptom VARCHAR (250) NOT NULL,
    PRIMARY KEY (id_diseases)
)