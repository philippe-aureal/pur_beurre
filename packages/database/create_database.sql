
CREATE SCHEMA IF NOT EXISTS pur_beurre CHARACTER SET utf8 ;
USE pur_beurre ;


CREATE TABLE IF NOT EXISTS pur_beurre.Category (
  id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
  name_category VARCHAR(150) UNIQUE NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = InnoDB;




CREATE TABLE IF NOT EXISTS pur_beurre.Product (
  id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  name_product VARCHAR(200) NOT NULL,
  brand_product VARCHAR(70) NOT NULL,
  nutritional_note VARCHAR(10),
  url VARCHAR(250) NULL DEFAULT NULL,
  category_id SMALLINT UNSIGNED,
  PRIMARY KEY (id),
  CONSTRAINT fk_category_id
    FOREIGN KEY (category_id)
    REFERENCES pur_beurre.Category (id))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS pur_beurre.Store (
  id SMALLINT(5) UNSIGNED AUTO_INCREMENT NOT NULL,
  name_store VARCHAR(150) UNIQUE NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;




CREATE TABLE IF NOT EXISTS pur_beurre.Product_Store (
  store_product_id INT(10) UNSIGNED NOT NULL,
  store_id SMALLINT(5) UNSIGNED NOT NULL,
  INDEX fk_store_id (store_id ASC),
  CONSTRAINT fk_store_id
    FOREIGN KEY (store_id)
    REFERENCES pur_beurre.Store (id),
  CONSTRAINT fk_store_product_id
    FOREIGN KEY (store_product_id)
    REFERENCES pur_beurre.Product (id))
ENGINE = InnoDB;




CREATE TABLE IF NOT EXISTS pur_beurre.Substitute (
  id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  product_id INT(10) UNSIGNED NOT NULL,
  Substitute_id SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_product_id (product_id ASC),
  CONSTRAINT fk_product_id
    FOREIGN KEY (product_id)
    REFERENCES pur_beurre.Product (id))
ENGINE = InnoDB;
