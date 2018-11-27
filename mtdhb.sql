-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mtdhb
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `black_sn`
--

DROP TABLE IF EXISTS `black_sn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `black_sn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `black_sn` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `black_sn`
--

LOCK TABLES `black_sn` WRITE;
/*!40000 ALTER TABLE `black_sn` DISABLE KEYS */;
INSERT INTO `black_sn` VALUES (6,'11023eb9fa04ec4a'),(7,'1100bdf50204ec36'),(8,'1100bdd01d08ec2d'),(9,'11008fc6fa88ec42'),(10,'10ffe6807508ecd6'),(11,'10ffcb551908ec2e'),(12,'2a03ffbf0a2cec5d'),(13,'2a03a9ab0bb0ec8c'),(14,'2a0bf32d8604ecbf'),(15,'11045a0d5287149a'),(16,'1103cd9d7c87f093'),(17,'1102a9d891868836'),(19,'11044d9ac1853458'),(20,'1102771a8284641b'),(21,'10fccd57be08ecdb'),(22,'2a047d2c06b0ec7e'),(23,'2a04ac6ed4acec5d'),(24,'10fd4b92bb08ec54'),(25,'10fd852fdd08ec52'),(26,'10fd98ff9988ec54'),(27,'2a0614413bb0ec54'),(28,'10fe496d3388ecdb'),(29,'2a055da36730ece3'),(30,'2a0546046830ec8c'),(32,'2a0c020a3f053458'),(33,'2a0bcc19fb1d2cb6'),(34,'11034d00ff053400'),(35,'110478b5dc049c63'),(36,'110471665005bcad'),(37,'1102e994b987c4a9'),(38,'10ff32846a88ec2e'),(39,'2a066f899108ec2e'),(40,'10fec503bf88ecdb'),(41,'10fedc1c7108ec59'),(42,'10ff09b68d88ecdb'),(43,'11047e170c873c64'),(44,'110476e19f07d47a'),(45,'2a0bfdd777060c18'),(46,'2a0bfc902e842418'),(47,'11043a5c2b07f047'),(48,'11040e5245860c6a'),(49,'1103ecf3148424f1'),(50,'110398330384246a'),(51,'110345523987d462'),(52,'1105618b1404ec66'),(53,'11058940eb84ec66'),(54,'1105a09bc504ec66'),(55,'11059b157704eca2'),(56,'1105b3be9404ec66'),(57,'1105db7f8d8488bf'),(58,'1104f875fe060c2d'),(59,'110506c69407d4ae'),(60,'1105239693870cf1'),(61,'110535ccfe87d44d'),(62,'1105418e9485bc0d'),(63,'110542769a060c99'),(64,'110544f7e8873c09'),(65,'11054e4c4004786c'),(66,'11057f5e74060c3c'),(67,'1105964b60860c36'),(68,'1105b9ff38860c18'),(69,'1105bacf6d043059'),(70,'1105c585df860ce2'),(71,'1106036b47858cef'),(72,'110606a0ae05ccd7'),(73,'11061b0e40866885'),(74,'11060c54380764ee'),(75,'1105ce894c04ec66'),(76,'1105c4c04c84ec36'),(77,'10ff60212d88ecc2'),(78,'1105fa35460668bf'),(83,'11050bc09f853462'),(84,'110675bc6e049c10'),(85,'110641f3fe060c36'),(86,'11001194dc2ae03e'),(87,'2a07f515421c88c0'),(88,'2a07f3098dbb98af'),(89,'2a07fa62c72e64a9'),(90,'2a0e8ba91f36808c'),(91,'110693cbe604303d'),(92,'110696ef47060cee'),(93,'110697637005cc39'),(94,'11065edb7d07a4ee'),(95,'11069f9de8845c13'),(96,'1106d410fb048cb6'),(97,'2a0f39e79c858cd1'),(98,'1106bfdcfa05ccf4'),(99,'2a0f031751860cee'),(100,'2a0f2a0b9c07f09f'),(101,'2a0f306eff0424ee'),(102,'2a0f3ac0c2860c63'),(103,'110710c66805cc36'),(104,'1107319fe2858c7c'),(105,'11075aab45071434'),(106,'110119912a84ec24'),(107,'1104c3445b84ec9a'),(108,'11082d074407f0d7'),(109,'110882cbc384788c'),(110,'1108ad9deb060c36'),(111,'1108af0ff5042436'),(112,'1108c8e6288478b6'),(113,'1108f1ce8b04243c'),(114,'1108ff3dfc846444'),(115,'11086ac9c587f0b3'),(116,'2a132eb4f4acecea'),(117,'2a129dbe9e2cecf3'),(118,'2a12e192f4acec0e'),(119,'110a413e98060c36'),(120,'110a3022aa042436'),(121,'110a2c452e843036'),(122,'1109eed6b2048c8a'),(123,'1109e8f24507d4bd'),(124,'1109e47ebd87f0f2');
/*!40000 ALTER TABLE `black_sn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cookie_number`
--

DROP TABLE IF EXISTS `cookie_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cookie_number` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qq` char(10) DEFAULT NULL,
  `cookie_sign` char(32) DEFAULT NULL,
  `phone` char(11) DEFAULT NULL,
  `QQnumber` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cookie_number`
--

LOCK TABLES `cookie_number` WRITE;
/*!40000 ALTER TABLE `cookie_number` DISABLE KEYS */;
INSERT INTO `cookie_number` VALUES (1,'2457755040','fdcc932a41b9c9741b838ae8060d34dc','13486158257',2),(2,'835265836','d98847c729c4cf00924e656f618ee5d8','13458690085',9),(3,'3085164184','8bbe05ae2975c21cd9282263bf8ff733','15834568442',8),(4,'1444813593','0ae0652d6428f7ebcc00177cfb7846a8','157****6923',3),(5,'2670218530','84a30875146b1c1cba37726ae095d550','15983843417',4),(6,'2720995759','8d378988ade6d609a561ce35d19590ea','15104451629',5),(7,'3448678920','556f85a6ec9097c1d333efceb0ccd8cb','15104451629',6),(8,'384806894','becbfbefa8f2127c0794e1231ad1bdb9','15243822426',1),(9,'3353545028','464b9f6ad6ce851d534704b9632e11eb','13568103439',11),(10,'2168877302','f53c1b45b3e1b3775b850272391ac1cc',NULL,NULL),(11,'2159727937','5a95790d1b7a09bab38ad7af7ed42df1','13285705140',7),(12,'3098859761','71060c6ad92c0b8fc9ec71b06cc425a8','13408457439',NULL),(13,'3175465255','b56f109554dfacb4e65d72e144ab95a4','14702851645',NULL),(14,'1471269599','400f306e5dabccfc896519d25345f08f','15183802425',10),(15,'2234344059','6ed7514fa3eb810a5a43cf513d53182f','18483667554',12),(16,NULL,NULL,'13541664180',NULL);
/*!40000 ALTER TABLE `cookie_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mtdhb`
--

DROP TABLE IF EXISTS `mtdhb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `mtdhb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cookie` varchar(2560) DEFAULT NULL,
  `sign` char(32) DEFAULT NULL,
  `jurl` char(32) DEFAULT NULL,
  `utrance` char(45) DEFAULT NULL COMMENT '43',
  `ubt_ssid` char(45) DEFAULT NULL COMMENT '43',
  `perf_ssid` char(45) DEFAULT NULL COMMENT '43',
  `SID` char(36) DEFAULT NULL,
  `info` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mtdhb2`
--

DROP TABLE IF EXISTS `mtdhb2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `mtdhb2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cookie` varchar(2560) DEFAULT NULL,
  `sign` char(32) DEFAULT NULL,
  `jurl` char(32) DEFAULT NULL,
  `utrance` char(45) DEFAULT NULL COMMENT '43',
  `ubt_ssid` char(45) DEFAULT NULL COMMENT '43',
  `perf_ssid` char(45) DEFAULT NULL COMMENT '43',
  `SID` char(36) DEFAULT NULL,
  `info` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ua`
--

DROP TABLE IF EXISTS `ua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ua` (
  `ua` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ua`
--

LOCK TABLES `ua` WRITE;
/*!40000 ALTER TABLE `ua` DISABLE KEYS */;
INSERT INTO `ua` VALUES ('Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1ANDSQ7.2.5744YYBD QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080');
/*!40000 ALTER TABLE `ua` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `write_sn`
--

DROP TABLE IF EXISTS `write_sn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `write_sn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `write_sn` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `write_sn`
--

LOCK TABLES `write_sn` WRITE;
/*!40000 ALTER TABLE `write_sn` DISABLE KEYS */;
/*!40000 ALTER TABLE `write_sn` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-15 18:31:41
