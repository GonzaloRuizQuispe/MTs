CREATE DATABASE db_diseases;

CREATE TABLE enfermedad (
    Nombre VARCHAR (50) NOT NULL,
    Enfermedad_id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (Enfermedad_id)
);

CREATE TABLE sintomas (
	Sintoma_id INT NOT NULL AUTO_INCREMENT,
    Enfermedad_id INT NOT NULL,
    Sintomas_posibles VARCHAR (275) NOT NULL,
    Sintomas_menos_posibles VARCHAR (275) NOT NULL,
    Sintomas_asintomaticos VARCHAR (275) NOT NULL,
    PRIMARY KEY (Sintoma_id),
    CONSTRAINT fk_sintoma_enfermedad FOREIGN KEY (Enfermedad_id) REFERENCES enfermedad (Enfermedad_id)
);

CREATE TABLE tratamientos (
	Tratamiento_id INT NOT NULL AUTO_INCREMENT,
    Sintoma_id INT NOT NULL,
    Tratamiento VARCHAR (275) NOT NULL,
    PRIMARY KEY (Tratamiento_id),
    CONSTRAINT fk_tratamiento_sintoma FOREIGN KEY (Sintoma_id) REFERENCES sintomas (Sintoma_id)
);

CREATE TABLE causas (
	Causa_id INT NOT NULL AUTO_INCREMENT,
    Enfermedad_id INT NOT NULL,
    Causa_posible VARCHAR (275) NOT NULL,
    Causa_menos_posible VARCHAR (275) NOT NULL,
    PRIMARY KEY (Causa_id),
    CONSTRAINT fk_causa_Enfermedad FOREIGN KEY (Enfermedad_id) REFERENCES enfermedad (Enfermedad_id)
);

INSERT INTO enfermedad (Nombre) VALUES
('Ulcera Corneal');
INSERT INTO sintomas (Sintomas_posibles, Sintomas_menos_posibles, Sintomas_asintomaticos,Enfermedad_id) VALUES 
('Dolor de cabeza', 'Vision borrosa', 'Lagrimeo', 1);
INSERT INTO tratamientos (Tratamiento, Sintoma_id) VALUES 
('Proteger los ojos de forma adecuada', 1);
INSERT INTO causas (Causa_posible, Causa_menos_posible, Enfermedad_id) VALUES
('Traumatismo directos', 'Cuerpo extraño', 1);

SELECT * FROM tratamientos WHERE tratamiento_id = 1;

DROP DATABASE db_diseases;