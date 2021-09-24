CREATE DATABASE db_diseases;

CREATE TABLE enfermedad (
	id INT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR (50) NOT NULL,
	PRIMARY KEY (id,Nombre)
);

CREATE TABLE tratamientos (
	Tratamiento_id INT NOT NULL AUTO_INCREMENT,
    Tratamiento VARCHAR (275) NOT NULL,
    Nombre_E VARCHAR (50) NOT NULL,
    PRIMARY KEY (Tratamiento_id),
    CONSTRAINT fk_Tratamiento_Enfermedad FOREIGN KEY (Nombre_E) REFERENCES enfermedad (Nombre)
);

INSERT INTO enfermedad (Nombre,Sintomas,Tratamientos,Causas) VALUES
('Ulcera Corneal','Lagrimeo-Escozor-Irritacion-Enrojecimiento-Dolor_De_Cabeza-Vision_Borrosa',
'Proteger Los Ojos De Forma Adecuada Y Unos Primeros Auxilios A Tiempo Pueden Salvar La Vista',
'Traumatismo_directos-Cuerpos_extraños');

SELECT * FROM enfermedad;
