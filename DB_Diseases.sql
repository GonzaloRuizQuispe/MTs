CREATE DATABASE db_diseases;

CREATE TABLE enfermedad (
	id INT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR (50) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE sintomas (
	sintoma_id INT NOT NULL AUTO_INCREMENT,
    sintomas_posibles VARCHAR (275) NOT NULL,
    sintomas_menos_posibles VARCHAR (275) NOT NULL,
    sintomas_asintomaticos VARCHAR (275) NOT NULL,
    sintoma_enfermedad VARCHAR (50) NOT NULL,
    PRIMARY KEY (sintoma_enfermedad),
    CONSTRAINT fk_sintoma_id FOREIGN KEY (sintoma_id) REFERENCES enfermedad (id)
);

CREATE TABLE tratamientos (
	Tratamiento_id INT NOT NULL AUTO_INCREMENT,
    Tratamiento VARCHAR (275) NOT NULL,
    Nombre_E VARCHAR (50) NOT NULL,
    PRIMARY KEY (Tratamiento_id),
    CONSTRAINT fk_id_tratamiento FOREIGN KEY (Tratamiento_id) REFERENCES sintomas (sintoma_id)
);

CREATE TABLE causas (
	Causa_id INT NOT NULL AUTO_INCREMENT,
    Causa_posible VARCHAR (275) NOT NULL,
    Causa_menos_posible VARCHAR (275) NOT NULL,
    PRIMARY KEY (Causa_id),
    CONSTRAINT fk_causa_N_E FOREIGN KEY (Causa_id) REFERENCES sintomas (sintoma_id)
);

INSERT INTO enfermedad (Nombre,Sintomas,Tratamientos,Causas) VALUES
('Ulcera Corneal','Lagrimeo-Escozor-Irritacion-Enrojecimiento-Dolor_De_Cabeza-Vision_Borrosa',
'Proteger Los Ojos De Forma Adecuada Y Unos Primeros Auxilios A Tiempo Pueden Salvar La Vista',
'Traumatismo_directos-Cuerpos_extraños');

SELECT * FROM enfermedad;

DROP DATABASE db_diseases;
