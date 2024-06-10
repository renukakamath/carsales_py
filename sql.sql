/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - car_sales
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`car_sales` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `car_sales`;

/*Table structure for table `carbooking` */

DROP TABLE IF EXISTS `carbooking`;

CREATE TABLE `carbooking` (
  `carbooking_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`carbooking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `carbooking` */

insert  into `carbooking`(`carbooking_id`,`vehicle_id`,`customer_id`,`date`,`amount`,`status`) values 
(1,3,1,'2023-01-31','500','pending'),
(2,3,1,'2023-01-31','500','pending');

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `license` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`company_id`,`login_id`,`company`,`license`,`phone`,`email`) values 
(1,1,'com','1234567890','02345678907','compt@gmail.com');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`date`) values 
(1,1,'good','ok','2023-01-31 15:50:56'),
(2,1,'hai','pending','2023-02-01 16:58:14');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,3,'user','qwerty','kerala','02345678907','student@gmail.com');

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `enquiry` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`customer_id`,`company_id`,`enquiry`,`date`,`reply`) values 
(1,1,1,'qwe','2023-01-31','ok');

/*Table structure for table `feature` */

DROP TABLE IF EXISTS `feature`;

CREATE TABLE `feature` (
  `feature_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `features` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feature_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feature` */

insert  into `feature`(`feature_id`,`vehicle_id`,`features`) values 
(5,3,'good');

/*Table structure for table `images` */

DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `images` */

/*Table structure for table `loan` */

DROP TABLE IF EXISTS `loan`;

CREATE TABLE `loan` (
  `loan_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`loan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `loan` */

insert  into `loan`(`loan_id`,`customer_id`,`details`,`amount`,`status`) values 
(1,1,'hai','400000','Accept');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'co','co','company'),
(3,'user','user','customer'),
(2,'admin','admin','admin');

/*Table structure for table `partbook` */

DROP TABLE IF EXISTS `partbook`;

CREATE TABLE `partbook` (
  `partbook_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`partbook_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `partbook` */

insert  into `partbook`(`partbook_id`,`customer_id`,`total`,`date`,`status`) values 
(1,1,'200244','2023-01-31','pending');

/*Table structure for table `partbookdetail` */

DROP TABLE IF EXISTS `partbookdetail`;

CREATE TABLE `partbookdetail` (
  `partdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `partbook_id` int(11) DEFAULT NULL,
  `parts_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`partdetail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `partbookdetail` */

insert  into `partbookdetail`(`partdetail_id`,`partbook_id`,`parts_id`,`amount`,`quantity`) values 
(1,1,3,'200044','4'),
(2,1,2,'200','2');

/*Table structure for table `parts` */

DROP TABLE IF EXISTS `parts`;

CREATE TABLE `parts` (
  `parts_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `parts` varchar(100) DEFAULT NULL,
  `features` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`parts_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `parts` */

insert  into `parts`(`parts_id`,`company_id`,`parts`,`features`,`details`,`amount`) values 
(2,1,'sfssf1','dfererd1',' at today morning 1 9.30 am','100'),
(3,1,'sfssf1','dfererd1','qwertyui1','50011');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`book_id`,`amount`,`date`) values 
(1,2,'500','2023-01-31'),
(2,2,'500','2023-01-31'),
(3,1,'50011','2023-01-31');

/*Table structure for table `sepecification` */

DROP TABLE IF EXISTS `sepecification`;

CREATE TABLE `sepecification` (
  `sepicification_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `specification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sepicification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `sepecification` */

insert  into `sepecification`(`sepicification_id`,`vehicle_id`,`specification`) values 
(2,3,'hellog');

/*Table structure for table `testbooking` */

DROP TABLE IF EXISTS `testbooking`;

CREATE TABLE `testbooking` (
  `testbooking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `booked_for_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`testbooking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `testbooking` */

insert  into `testbooking`(`testbooking_id`,`customer_id`,`vehicle_id`,`date`,`booked_for_date`,`status`) values 
(1,1,3,'2023-01-31','2023-02-05','pending');

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `type` */

insert  into `type`(`type_id`,`type`) values 
(1,'qweghj');

/*Table structure for table `varients` */

DROP TABLE IF EXISTS `varients`;

CREATE TABLE `varients` (
  `variant_id` int(11) NOT NULL AUTO_INCREMENT,
  `variant` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`variant_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `varients` */

insert  into `varients`(`variant_id`,`variant`) values 
(1,'vari');

/*Table structure for table `vehicle` */

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `variant_id` varchar(100) DEFAULT NULL,
  `vehicle` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle` */

insert  into `vehicle`(`vehicle_id`,`company_id`,`type_id`,`variant_id`,`vehicle`,`amount`) values 
(3,1,1,'1','car','500');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
