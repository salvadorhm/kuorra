DROP DATABASE acme_store_mvc;

CREATE DATABASE acme_store_mvc;

USE acme_store_mvc;

CREATE TABLE products (
  id_product int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product varchar(100) NOT NULL,
  stock float NOT NULL,
  description varchar(200) NOT NULL,
  purchase_price float NOT NULL,
  price_sale float NOT NULL,
  product_image varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO products(product,stock,description,purchase_price,price_sale, product_image) VALUES 
('Moto Maxx',10,'Motorola Moto Maxx',8500,10500 ,'default.jpg'),
('Pebble',100,'Pebble Red',1800,2000,'default.jpg'),
('Laptop Asus Mx34',5,'Laptop Asus i7 8GB Ram 1TB HHD',17000,21000,'default.jpg');

SELECT * FROM products;
