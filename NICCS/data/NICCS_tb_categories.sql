CREATE DATABASE  IF NOT EXISTS `NICCS` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `NICCS`;
-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: NICCS
-- ------------------------------------------------------
-- Server version	5.6.27-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_categories`
--

DROP TABLE IF EXISTS `tb_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_categories` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(150) DEFAULT NULL,
  `des` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_categories`
--

LOCK TABLES `tb_categories` WRITE;
/*!40000 ALTER TABLE `tb_categories` DISABLE KEYS */;
INSERT INTO `tb_categories` VALUES (1,'Securely Provision','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Securely%20Provision','Specialty areas concerned with conceptualizing, designing, and building secure IT systems, with responsibility for some aspect of the systems\' development'),(2,'Operate and Maintain','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Operate%20and%20Maintain','Specialty areas responsible for providing the support, administration, and maintenance necessary to ensure effective and efficient IT system performance and security.'),(3,'Protect and Defend','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Protect%20and%20Defend','Specialty areas responsible for the identification, analysis, and mitigation of threats to internal IT systems or networks.'),(4,'Analyze','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Analyze','Specialty areas responsible for highly specialized review and evaluation of incoming cybersecurity information to determine its usefulness for intelligence.'),(5,'Oversight and Development','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Oversight%20and%20Development','Oversight and Development - Specialty areas providing leadership, management, direction, and/or development and advocacy so that all individuals and the organization may effectively conduct cybersecurity work.'),(6,'Investigate','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Investigate','Specialty areas responsible for the investigation of cyber events and/or crimes of IT systems, networks, and digital evidence.'),(7,'Collect and Operate','https://niccs.us-cert.gov/training/framework/specialty-areas?Category=Collect%20and%20Operate','Specialty areas responsible for specialized denial and deception operations and collection of cybersecurity information that may be used to develop intelligence.');
/*!40000 ALTER TABLE `tb_categories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-01 16:49:11
