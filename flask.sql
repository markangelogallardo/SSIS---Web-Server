DROP DATABASE IF EXISTS `web_ver_ssis`;
CREATE DATABASE IF NOT EXISTS `web_ver_ssis`;
USE `web_ver_ssis`;

DROP TABLE IF EXISTS `colleges`;
CREATE TABLE IF NOT EXISTS `colleges`(
	`College_Code` VARCHAR(10) NOT NULL,
    `College_Name` VARCHAR(100) NOT NULL,
    CONSTRAINT `pk_College_Code` PRIMARY KEY(`College_Code`),
    CONSTRAINT `unique_College_Name` UNIQUE(`College_Name`)
);

DROP TABLE IF EXISTS `programs`;
CREATE TABLE IF NOT EXISTS `programs`(	
   `Program_Code` VARCHAR(15) NOT NULL,
   `Program_Name` VARCHAR(100) NOT NULL,
   `College_Code` VARCHAR(5) NOT NULL,	
   CONSTRAINT `pk_Program_Code` PRIMARY KEY(`Program_Code`),
   CONSTRAINT `unique_Program_Name` UNIQUE(`Program_Name`),
   CONSTRAINT `fk_Program_College` FOREIGN KEY (`College_Code`) REFERENCES `colleges`(`College_Code`) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students`(	
	`ID_Number` CHAR(9) NOT NULL,
	`First_Name` VARCHAR(50) NOT NULL,
	`Last_Name` VARCHAR(50) NOT NULL,
	`Program_Code`VARCHAR(20),
	`Year_Level` ENUM("1st year", "2nd year", "3rd year", "4th year") NOT NULL,
	`Gender` ENUM("Male", "Female", "Rather not specify") NOT NULL,
	CONSTRAINT `pk_ID_Number` PRIMARY KEY(`ID_Number`),
	CONSTRAINT `unique_Name` UNIQUE(`First_Name`, `Last_Name`),
	CONSTRAINT `fk_Student_Program` FOREIGN KEY(`Program_Code`) REFERENCES `programs`(`Program_Code`) ON UPDATE CASCADE ON DELETE SET NULL
);