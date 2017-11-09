CREATE DATABASE contacts_kuorra;

USE contacts_kuorra;

DROP TABLE IF EXISTS persons;

CREATE TABLE persons (
  id_person int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  telephone varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  email varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (id_person)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


INSERT INTO persons VALUES 
(1,'Dejah Thoris','111111111','dejah@barson.com'),
(2,'Jhon Carter','222222222','jhon@tierra.com'),
(3,'Carthoris','3333333333','carthoris@correobarson.com');

SELECT * FROM persons;
