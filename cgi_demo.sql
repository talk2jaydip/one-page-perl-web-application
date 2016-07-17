/*
SQLyog Trial v12.2.4 (64 bit)
MySQL - 5.5.49-0ubuntu0.14.04.1 : Database - cgi_demo
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cgi_demo` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cgi_demo`;

/*Table structure for table `APPOINTMENTS` */

DROP TABLE IF EXISTS `APPOINTMENTS`;

CREATE TABLE `APPOINTMENTS` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Description` text COLLATE utf8_swedish_ci,
  `Date` varchar(255) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Time` varchar(255) COLLATE utf8_swedish_ci DEFAULT NULL,
  `Createdtine` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `APPOINTMENTS` */

insert  into `APPOINTMENTS`(`Id`,`Description`,`Date`,`Time`,`Createdtine`) values 
(1,'','','',NULL),
(2,'check data','july 17','13:08',NULL),
(3,'check data','july 17','13:08',NULL),
(4,'check data','july 17','13:08',NULL),
(5,'check data','july 17','13:08',NULL),
(6,'check data','july 17','13:08',NULL),
(7,'','','',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
