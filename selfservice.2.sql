CREATE DATABASE  IF NOT EXISTS `selfservice` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `selfservice`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: localhost    Database: selfservice
-- ------------------------------------------------------
-- Server version	5.6.12-log

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
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `channelid` int(11) NOT NULL AUTO_INCREMENT,
  `channelname` varchar(50) NOT NULL,
  PRIMARY KEY (`channelid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='channel information';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='industry name';
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
  `supplyIndex` decimal(10,0) NOT NULL,
  `product_dictionary_product_id` int(11) NOT NULL,
  PRIMARY KEY (`index_date`,`product_id`,`product_dictionary_product_id`),
  KEY `fk_market_trend_product_dictionary1_idx` (`product_dictionary_product_id`),
  CONSTRAINT `fk_market_trend_product_dictionary1` FOREIGN KEY (`product_dictionary_product_id`) REFERENCES `product_dictionary` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
  `industry_industryid` int(11) NOT NULL,
  `channel_channelid` int(11) NOT NULL,
  PRIMARY KEY (`channelid`,`industryid`,`industry_industryid`,`channel_channelid`),
  KEY `fk_pricematrix_industry_idx` (`industry_industryid`),
  KEY `fk_pricematrix_channel1_idx` (`channel_channelid`),
  CONSTRAINT `fk_pricematrix_industry` FOREIGN KEY (`industry_industryid`) REFERENCES `industry` (`industryid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_pricematrix_channel1` FOREIGN KEY (`channel_channelid`) REFERENCES `channel` (`channelid`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
) ENGINE=InnoDB AUTO_INCREMENT=971 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_dictionary`
--

LOCK TABLES `product_dictionary` WRITE;
/*!40000 ALTER TABLE `product_dictionary` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_dictionary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlog` (
  `usersessionid` int(11) NOT NULL AUTO_INCREMENT,
  `sessiondate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `industryid` tinyint(4) NOT NULL,
  `campaign_goal` tinyint(4) NOT NULL,
  `initial_budget` decimal(10,0) NOT NULL,
  `comanyname` varchar(50) DEFAULT NULL,
  `companyurl` varchar(150) DEFAULT NULL,
  `competitor` varchar(50) DEFAULT NULL,
  `competitorurl` varchar(150) DEFAULT NULL,
  `productname` varchar(50) DEFAULT NULL,
  `industry_industryid` int(11) NOT NULL,
  PRIMARY KEY (`usersessionid`,`industry_industryid`),
  KEY `fk_userlog_industry1_idx` (`industry_industryid`),
  CONSTRAINT `fk_userlog_industry1` FOREIGN KEY (`industry_industryid`) REFERENCES `industry` (`industryid`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2014-10-21 12:32:20
