CREATE DATABASE  IF NOT EXISTS `self_service` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `self_service`;
-- MySQL dump 10.13  Distrib 5.6.17, for osx10.6 (i386)
--
-- Host: localhost    Database: self_service
-- ------------------------------------------------------
-- Server version	5.6.21

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add industry',7,'add_industry'),(20,'Can change industry',7,'change_industry'),(21,'Can delete industry',7,'delete_industry'),(22,'Can add channel',8,'add_channel'),(23,'Can change channel',8,'change_channel'),(24,'Can delete channel',8,'delete_channel'),(25,'Can add price metrics',9,'add_pricemetrics'),(26,'Can change price metrics',9,'change_pricemetrics'),(27,'Can delete price metrics',9,'delete_pricemetrics'),(28,'Can add industry',10,'add_industry'),(29,'Can change industry',10,'change_industry'),(30,'Can delete industry',10,'delete_industry'),(31,'Can add channel',11,'add_channel'),(32,'Can change channel',11,'change_channel'),(33,'Can delete channel',11,'delete_channel'),(34,'Can add price matrix',12,'add_pricematrix'),(35,'Can change price matrix',12,'change_pricematrix'),(36,'Can delete price matrix',12,'delete_pricematrix');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$BhdWBbO1cRh2$tTlkZ3I+p6GXB+MrecS8UZcB2/HJ2+CKXkSx/oGVF9s=','2014-11-17 23:00:06',1,'dj_admin','','','help@glogou.com',1,1,'2014-11-17 23:00:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `budget_allocation_channel`
--

DROP TABLE IF EXISTS `budget_allocation_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `budget_allocation_channel` (
  `channelId` int(11) NOT NULL AUTO_INCREMENT,
  `channelName` varchar(100) NOT NULL,
  `minMediaBuy` int(11) DEFAULT NULL,
  PRIMARY KEY (`channelId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budget_allocation_channel`
--

LOCK TABLES `budget_allocation_channel` WRITE;
/*!40000 ALTER TABLE `budget_allocation_channel` DISABLE KEYS */;
INSERT INTO `budget_allocation_channel` VALUES (1,'Baidu PPC',NULL),(2,'SouFun',NULL),(3,'Baidu RRC',NULL),(4,'CTrip',NULL);
/*!40000 ALTER TABLE `budget_allocation_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `budget_allocation_industry`
--

DROP TABLE IF EXISTS `budget_allocation_industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `budget_allocation_industry` (
  `industryId` int(11) NOT NULL AUTO_INCREMENT,
  `industryName` varchar(100) NOT NULL,
  PRIMARY KEY (`industryId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budget_allocation_industry`
--

LOCK TABLES `budget_allocation_industry` WRITE;
/*!40000 ALTER TABLE `budget_allocation_industry` DISABLE KEYS */;
INSERT INTO `budget_allocation_industry` VALUES (1,'Education Market'),(2,'Destination Marketing'),(3,'Real Estate'),(4,'High Tech Industry');
/*!40000 ALTER TABLE `budget_allocation_industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `budget_allocation_pricemetrics`
--

DROP TABLE IF EXISTS `budget_allocation_pricemetrics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `budget_allocation_pricemetrics` (
  `priceMatrixId` int(11) NOT NULL AUTO_INCREMENT,
  `allocation` double NOT NULL,
  `budget` double NOT NULL,
  `expectedClicks` int(11) NOT NULL,
  `costPerClick` double NOT NULL,
  `expectedImpressions` double NOT NULL,
  `costPerImpression` double NOT NULL,
  `industryId` int(11) NOT NULL,
  `channelId` int(11) NOT NULL,
  PRIMARY KEY (`priceMatrixId`),
  KEY `budget_allocation_pricemetrics_a9631a33` (`industryId`),
  KEY `budget_allocation_pricemetrics_176fd3f7` (`channelId`),
  CONSTRAINT `channelId_refs_channelId_d403d3ca` FOREIGN KEY (`channelId`) REFERENCES `budget_allocation_channel` (`channelId`),
  CONSTRAINT `industryId_refs_industryId_9089bf7b` FOREIGN KEY (`industryId`) REFERENCES `budget_allocation_industry` (`industryId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budget_allocation_pricemetrics`
--

LOCK TABLES `budget_allocation_pricemetrics` WRITE;
/*!40000 ALTER TABLE `budget_allocation_pricemetrics` DISABLE KEYS */;
INSERT INTO `budget_allocation_pricemetrics` VALUES (1,1000,5000,3000,0.68,680000,2.2,1,1),(2,1000,5000,3000,0.68,680000,2.2,1,2),(9,1000,5000,2000,0.7,784000,2.4,1,3),(10,1000,5000,1500,0.5,50000,3.4,1,4);
/*!40000 ALTER TABLE `budget_allocation_pricemetrics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `channelid` int(11) NOT NULL AUTO_INCREMENT,
  `channelname` varchar(50) NOT NULL,
  `Min_Media_Buy` int(11) DEFAULT NULL,
  PRIMARY KEY (`channelid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='channel information';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'industry','budget_allocation','industry'),(8,'channel','budget_allocation','channel'),(9,'price metrics','budget_allocation','pricemetrics'),(10,'industry','restapi','industry'),(11,'channel','restapi','channel'),(12,'price matrix','restapi','pricematrix');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `industry`
--

DROP TABLE IF EXISTS `industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `industry` (
  `industryid` int(11) NOT NULL AUTO_INCREMENT,
  `industryname` varchar(50) NOT NULL,
  PRIMARY KEY (`industryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='industry name';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `industry`
--

LOCK TABLES `industry` WRITE;
/*!40000 ALTER TABLE `industry` DISABLE KEYS */;
/*!40000 ALTER TABLE `industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `market_trend`
--

DROP TABLE IF EXISTS `market_trend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `market_trend` (
  `index_date` date NOT NULL,
  `product_id` int(11) NOT NULL,
  `purchase_index1688` decimal(10,0) NOT NULL,
  `purchase_indexTb` decimal(10,0) NOT NULL,
  `supply_index` decimal(10,0) NOT NULL,
  PRIMARY KEY (`index_date`,`product_id`),
  KEY `fk_market_trend_product_dictionary1_idx` (`product_id`),
  CONSTRAINT `fk_market_trend_product_dictionary1` FOREIGN KEY (`product_id`) REFERENCES `product_dictionary` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `market_trend`
--

LOCK TABLES `market_trend` WRITE;
/*!40000 ALTER TABLE `market_trend` DISABLE KEYS */;
/*!40000 ALTER TABLE `market_trend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pricematrix`
--

DROP TABLE IF EXISTS `pricematrix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pricematrix` (
  `channelid` int(11) NOT NULL,
  `industryid` int(11) NOT NULL,
  `price_per_click` decimal(10,0) DEFAULT NULL,
  `price_impression` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`channelid`,`industryid`),
  KEY `fk_pricematrix_industry1_idx` (`industryid`),
  CONSTRAINT `fk_pricematrix_channel1` FOREIGN KEY (`channelid`) REFERENCES `channel` (`channelid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_pricematrix_industry1` FOREIGN KEY (`industryid`) REFERENCES `industry` (`industryid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='price information based on channel and industry';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pricematrix`
--

LOCK TABLES `pricematrix` WRITE;
/*!40000 ALTER TABLE `pricematrix` DISABLE KEYS */;
/*!40000 ALTER TABLE `pricematrix` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_dictionary`
--

DROP TABLE IF EXISTS `product_dictionary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_dictionary` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `eng_kw` varchar(50) NOT NULL,
  `chn_kw` varchar(50) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_dictionary`
--

LOCK TABLES `product_dictionary` WRITE;
/*!40000 ALTER TABLE `product_dictionary` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_dictionary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restapi_channel`
--

DROP TABLE IF EXISTS `restapi_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restapi_channel` (
  `channelID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`channelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restapi_channel`
--

LOCK TABLES `restapi_channel` WRITE;
/*!40000 ALTER TABLE `restapi_channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `restapi_channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restapi_industry`
--

DROP TABLE IF EXISTS `restapi_industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restapi_industry` (
  `industryID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`industryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restapi_industry`
--

LOCK TABLES `restapi_industry` WRITE;
/*!40000 ALTER TABLE `restapi_industry` DISABLE KEYS */;
/*!40000 ALTER TABLE `restapi_industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restapi_pricematrix`
--

DROP TABLE IF EXISTS `restapi_pricematrix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restapi_pricematrix` (
  `priceMatrixID` int(11) NOT NULL AUTO_INCREMENT,
  `allocation` double NOT NULL,
  `budget` double NOT NULL,
  `expectedClicks` int(11) NOT NULL,
  `costPerClick` double NOT NULL,
  `expectedImpressions` double NOT NULL,
  `costPerImpression` double NOT NULL,
  `industryID` int(11) NOT NULL,
  `channelID` int(11) NOT NULL,
  PRIMARY KEY (`priceMatrixID`),
  KEY `restapi_pricematrix_6df726f6` (`industryID`),
  KEY `restapi_pricematrix_af42a130` (`channelID`),
  CONSTRAINT `channelID_refs_channelID_417db134` FOREIGN KEY (`channelID`) REFERENCES `restapi_channel` (`channelID`),
  CONSTRAINT `industryID_refs_industryID_85d329c7` FOREIGN KEY (`industryID`) REFERENCES `restapi_industry` (`industryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restapi_pricematrix`
--

LOCK TABLES `restapi_pricematrix` WRITE;
/*!40000 ALTER TABLE `restapi_pricematrix` DISABLE KEYS */;
/*!40000 ALTER TABLE `restapi_pricematrix` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlog` (
  `usersessionid` int(11) NOT NULL AUTO_INCREMENT,
  `industryid` int(11) NOT NULL,
  `sessiondate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `campaign_goal` tinyint(4) NOT NULL,
  `initial_budget` decimal(10,0) NOT NULL,
  `comanyname` varchar(50) DEFAULT NULL,
  `companyurl` varchar(150) DEFAULT NULL,
  `competitor` varchar(50) DEFAULT NULL,
  `competitorurl` varchar(150) DEFAULT NULL,
  `productname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`usersessionid`),
  KEY `fk_userlog_industry1_idx` (`industryid`),
  CONSTRAINT `fk_userlog_industry1` FOREIGN KEY (`industryid`) REFERENCES `industry` (`industryid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlog`
--

LOCK TABLES `userlog` WRITE;
/*!40000 ALTER TABLE `userlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `userlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-12 12:29:44
