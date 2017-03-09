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
-- Table structure for table `tb_jobs`
--

DROP TABLE IF EXISTS `tb_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_jobs` (
  `id` int(11) NOT NULL,
  `sp_id` int(11) DEFAULT NULL,
  `job` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_jobs`
--

LOCK TABLES `tb_jobs` WRITE;
/*!40000 ALTER TABLE `tb_jobs` DISABLE KEYS */;
INSERT INTO `tb_jobs` VALUES (1,1,'Accreditor'),(2,1,'Analyst/Manager'),(3,1,'Auditor'),(4,1,'Authorizing Official Designated Representative'),(5,1,'Certification Agent'),(6,1,'Certifying Official'),(7,1,'Compliance Manager'),(8,1,'Designated Accrediting Authority'),(9,1,'IA Compliance'),(10,1,'IA Manager'),(11,1,'IA Officer'),(12,1,'IT Auditor'),(13,1,'Portfolio Manager'),(14,1,'QA Specialist'),(15,1,'Risk/Vulnerability Analyst'),(16,1,'Security Control Assessor'),(17,1,'Systems Analyst'),(18,1,'Validator'),(19,2,'Analyst Programmer'),(20,2,'Computer Programmer'),(21,2,'Configuration Manager'),(22,2,'Database Developer/Engineer/Architect'),(23,2,'IA Engineer'),(24,2,'IA Software Developer'),(25,2,'IA Software Engineer'),(26,2,'R&D Engineer'),(27,2,'Secure Software Engineer'),(28,2,'Security Engineer'),(29,2,'Software Developer'),(30,2,'Software Engineer/Architect'),(31,2,'Systems Analyst'),(32,2,'Web Application Developer'),(33,3,'Firewall Engineer'),(34,3,'IA Developer'),(35,3,'IA Engineer'),(36,3,'IA Software Engineer'),(37,3,'Information Systems Security Engineer'),(38,3,'Program Developer'),(39,3,'Security Engineer'),(40,3,'Systems Engineer'),(41,3,'Systems Security Engineer'),(42,4,'Business Analyst'),(43,4,'Business Process Analyst'),(44,4,'Computer Systems Analyst'),(45,4,'Human Factors Engineer'),(46,4,'Requirements Analyst'),(47,4,'Solutions Architect'),(48,4,'Systems Consultant'),(49,4,'Systems Engineer'),(50,5,'IA Architect'),(51,5,'Information Security Architect'),(52,5,'Information Systems Security Engineer'),(53,5,'Network Security Analyst'),(54,5,'R&D Engineer'),(55,5,'Security Architect'),(56,5,'Security Engineer'),(57,5,'Security Solutions Architect'),(58,5,'Systems Engineer'),(59,5,'Systems Security Analyst'),(60,6,'Capabilities and Development Specialist'),(61,6,'Chief Engineer'),(62,6,'R&D Engineer'),(63,7,'Application Security Tester'),(64,7,'Information Systems Security Engineer'),(65,7,'Quality Assurance Tester'),(66,7,'R&D Engineer'),(67,7,'R&D Research Engineer'),(68,7,'Security Systems Engineer'),(69,7,'Software Quality Assurance Engineer'),(70,7,'Software Quality Engineer'),(71,7,'Systems Engineer'),(72,7,'Testing and Evaluation Specialist'),(73,8,'Service Desk Operator'),(74,8,'Computer Support Specialist'),(75,8,'Customer Support'),(76,8,'Help Desk Representative'),(77,8,'Systems Administrator'),(78,8,'Technical Support Specialist'),(79,8,'User Support Specialist'),(80,9,'Content Staging Specialist'),(81,9,'Data Architect'),(82,9,'Data Custodian'),(83,9,'Data Manager'),(84,9,'Data Warehouse Specialist'),(85,9,'Database Administrator'),(86,9,'Database Developer'),(87,9,'Database Engineer/Architect'),(88,9,'Information Dissemination Manager'),(89,9,'Systems Operations Personnel'),(90,10,'Document Steward'),(91,10,'Business Analyst'),(92,10,'Business Intelligence Manager'),(93,10,'Content Administrator'),(94,10,'Freedom of Information Act Official'),(95,10,'Information Manager'),(96,10,'Information Owner'),(97,10,'Information Resources Manager'),(98,11,'Cabling Technician'),(99,11,'Converged Network Engineer'),(100,11,'Network Administrator'),(101,11,'Network Analyst'),(102,11,'Network Designer'),(103,11,'Network Engineer'),(104,11,'Network Systems and Data Communications Analyst'),(105,11,'Network Systems Engineer'),(106,11,'Systems Engineer'),(107,11,'Telecommunications Engineer/Personnel/Specialist'),(108,12,'LAN Administrator'),(109,12,'Platform Specialist'),(110,12,'Security Administrator'),(111,12,'Server Administrator'),(112,12,'System Operations Personnel'),(113,12,'Systems Administrator'),(114,12,'Website Administrator'),(115,13,'IA Operational Engineer'),(116,13,'Information Assurance Security Officer'),(117,13,'Information Security Analyst/Administrator'),(118,13,'Information Security Manager'),(119,13,'Information Security Specialist'),(120,13,'Information Systems Security Engineer'),(121,13,'Information Systems Security Manager'),(122,13,'Platform Specialist'),(123,13,'Security Administrator'),(124,13,'Security Analyst'),(125,13,'Security Control Assessor'),(126,13,'Security Engineer'),(127,14,'CND Analyst (Cryptologic)'),(128,14,'Cyber Security Intelligence Analyst'),(129,14,'Focused Operations Analyst'),(130,14,'Incident Analyst'),(131,14,'Network Defense Technician'),(132,14,'Network Security Engineer'),(133,14,'Security Analyst'),(134,14,'Security Operator'),(135,14,'Sensor Analyst'),(136,15,'IDS Administrator'),(137,15,'IDS Engineer'),(138,15,'IDS Technician'),(139,15,'Information Systems Security Engineer'),(140,15,'Network Administrator'),(141,15,'Network Analyst'),(142,15,'Network Security Engineer'),(143,15,'Network Security Specialist'),(144,15,'Security Analyst'),(145,15,'Security Engineer'),(146,15,'Security Specialist'),(147,15,'Systems Security Engineer'),(148,16,'Computer Crime Investigator'),(149,16,'Incident Handler'),(150,16,'Incident Responder'),(151,16,'Incident Response Analyst'),(152,16,'Incident Response Coordinator'),(153,16,'Intrusion Analyst'),(154,17,'Blue Team Technician'),(155,17,'Certified TEMPEST Professionals'),(156,17,'Certified TEMPEST Technical Authority'),(157,17,'Close Access Technician'),(158,17,'CND Auditor'),(159,17,'Compliance Manager'),(160,17,'Ethical Hacker'),(161,17,'Governance Manager'),(162,17,'Information Security Engineer'),(163,17,'Internal Enterprise Audit'),(164,17,'Penetration Tester'),(165,17,'Red Team Technician'),(166,17,'Reverse Engineer'),(167,17,'Risk/Vulnerability Analyst'),(168,17,'Technical Surveillance Countermeasures Technician'),(169,17,'Vulnerability Manager'),(170,22,'Cyber Trainer'),(171,22,'Information Security Trainer'),(172,22,'Security Training Coordinator'),(173,23,'Contracting Officer'),(174,23,'Contracting Officer Technical Representative'),(175,23,'Information Assurance Manager'),(176,23,'Information Assurance Program Manager'),(177,23,'Information Assurance Security Officer'),(178,23,'Information Security Program Manager'),(179,23,'Information Systems Security Manager'),(180,23,'Information Systems Security Operations'),(181,24,'Legal Advisor/SJA'),(182,24,'Paralegal'),(183,25,'Chief Information Security Officer (CISO)'),(184,25,'Common Control Provider'),(185,25,'Cyber Security Officer'),(186,25,'Enterprise Security Officer'),(187,25,'Facility Security Officer'),(188,25,'Information Systems Security Manager'),(189,25,'IT Director'),(190,25,'Principal Security Architect'),(191,25,'Risk Executive'),(192,25,'Security Domain Specialist'),(193,25,'Senior Agency Information Security Officer (SAIS)'),(194,26,'Chief Information Officer (CIO)'),(195,26,'Command IO'),(196,26,'Information Security Policy Analyst'),(197,26,'Information Security Policy Manager'),(198,26,'Policy Writer and Strategist'),(199,27,'Computer Forensic Analyst'),(200,27,'Computer Network Defense Forensic Analyst'),(201,27,'Digital Forensic Examiner'),(202,27,'Digital Media Collector'),(203,27,'Forensic Analyst'),(204,27,'Forensic Analyst (Cryptologic)'),(205,27,'Forensic Technician'),(206,27,'Network Forensic Examiner'),(207,28,'Computer Crime Investigator'),(208,28,'Special Agent');
/*!40000 ALTER TABLE `tb_jobs` ENABLE KEYS */;
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
