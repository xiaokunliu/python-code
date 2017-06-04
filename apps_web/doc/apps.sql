/*
SQLyog 企业版 - MySQL GUI v8.14 
MySQL - 5.6.25 : Database - apps
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`apps` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `apps`;

/*Table structure for table `ss_apps_feedback` */

DROP TABLE IF EXISTS `ss_apps_feedback`;

CREATE TABLE `ss_apps_feedback` (
  `feed_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `feed_context` text NOT NULL COMMENT 'user feedback the apps',
  `feed_email` varchar(50) DEFAULT NULL COMMENT 'the user who feedback the opinion with the apps',
  PRIMARY KEY (`feed_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `ss_apps_feedback` */

/*Table structure for table `ss_apps_log` */

DROP TABLE IF EXISTS `ss_apps_log`;

CREATE TABLE `ss_apps_log` (
  `log_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `log_operate_code` tinyint(4) unsigned NOT NULL COMMENT 'record the user behavior',
  `log_user_id` int(11) unsigned NOT NULL COMMENT 'the user id',
  `log_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'user operate time',
  `log_desc` varchar(255) NOT NULL DEFAULT '' COMMENT 'desc log details',
  PRIMARY KEY (`log_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `ss_apps_log` */

/*Table structure for table `ss_crowd_sourcing_project` */

DROP TABLE IF EXISTS `ss_crowd_sourcing_project`;

CREATE TABLE `ss_crowd_sourcing_project` (
  `project_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `project_title` varchar(100) NOT NULL,
  `project_content` text NOT NULL COMMENT 'describe the invite content',
  `project_deployer` int(11) unsigned NOT NULL COMMENT 'references on ss_user',
  `project_receivers` varchar(50) NOT NULL COMMENT 'store for ''uid1,uid2,uid3,...'',the most is five',
  `project_status` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '0 is deployed,1 is building the receiver,2 is done',
  `project_begin_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'the project start time',
  `project_end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'the project end time',
  PRIMARY KEY (`project_id`),
  KEY `project_deployer` (`project_deployer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_crowd_sourcing_project` */

/*Table structure for table `ss_dictionary_type` */

DROP TABLE IF EXISTS `ss_dictionary_type`;

CREATE TABLE `ss_dictionary_type` (
  `dic_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'the dictionary table id',
  `dic_code` tinyint(11) unsigned NOT NULL COMMENT 'the dictionary code',
  `dic_val` varchar(50) NOT NULL DEFAULT '' COMMENT 'the dictionary value',
  `dic_detail` varchar(100) DEFAULT NULL COMMENT 'describe the dictionary sense',
  PRIMARY KEY (`dic_id`),
  UNIQUE KEY `dic_code` (`dic_code`),
  KEY `dic_code_2` (`dic_code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `ss_dictionary_type` */

/*Table structure for table `ss_internet_category` */

DROP TABLE IF EXISTS `ss_internet_category`;

CREATE TABLE `ss_internet_category` (
  `inter_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `inter_type_code` tinyint(4) unsigned NOT NULL COMMENT 'the type code',
  `inter_type_parent_code` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 for not any parent,itself is other type''s parent',
  `inter_type_name` varchar(30) NOT NULL COMMENT 'the type lable name',
  `inter_type_desc` varchar(50) DEFAULT NULL COMMENT 'describe the type info',
  PRIMARY KEY (`inter_id`),
  UNIQUE KEY `inter_type_code` (`inter_type_code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `ss_internet_category` */

/*Table structure for table `ss_message_list` */

DROP TABLE IF EXISTS `ss_message_list`;

CREATE TABLE `ss_message_list` (
  `msg_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `msg_type_code` tinyint(4) unsigned NOT NULL COMMENT 'for question/task/project,1 is for question,2 is for task,3 is for project',
  `msg_reply_id` int(11) unsigned NOT NULL COMMENT 'the user reply to the type_desc,and would be informed the deplyer',
  `msg_reply_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'record the user reply time',
  `msg_send_id` int(11) unsigned NOT NULL COMMENT 'the user who send the type list to ask',
  `msg_status` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '0 for executing,1 for done',
  `msg_end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'the message have been closed',
  PRIMARY KEY (`msg_id`),
  KEY `msg_reply_id` (`msg_reply_id`),
  KEY `msg_send_id` (`msg_send_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_message_list` */

/*Table structure for table `ss_question_list` */

DROP TABLE IF EXISTS `ss_question_list`;

CREATE TABLE `ss_question_list` (
  `qt_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `qt_title` varchar(60) DEFAULT NULL COMMENT 'the title for quetsion',
  `qt_desc` text COMMENT 'the consult detail ',
  `qt_status` tinyint(1) unsigned DEFAULT '0' COMMENT '0 is waitting,1 is executing,2 is done',
  `qt_begin_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'the create time',
  `qt_end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'the end time',
  `qt_type_codes` varchar(18) NOT NULL COMMENT 'store more dictionary_code,and split for sign '','' as speartor ',
  `qt_ask_user` int(11) unsigned NOT NULL COMMENT 'the user who ask the question,references on ss_user',
  `qt_answer_user` int(11) unsigned NOT NULL COMMENT 'the user who answer the question',
  `qt_answer_user_groom_degree` tinyint(1) unsigned DEFAULT '0' COMMENT '0 is not checked groom degree,1 is for lowest,2 is for lower,3 is medium,4 is high',
  `qt_answer_user_server_degree` tinyint(1) unsigned DEFAULT '0' COMMENT '0 is not checked,the same as con_groom_degree ',
  `qt_answer_user_ability_degree` int(11) unsigned DEFAULT '0' COMMENT '0 is not checked,others are the same as above',
  `qt_answer_remarked` text COMMENT 'the asker remark the answerer',
  PRIMARY KEY (`qt_id`),
  KEY `qt_ask_user` (`qt_ask_user`),
  KEY `qt_answer_user` (`qt_answer_user`),
  KEY `qt_status` (`qt_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_question_list` */

/*Table structure for table `ss_task_list` */

DROP TABLE IF EXISTS `ss_task`;

CREATE TABLE `ss_task` (
  `task_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `task_title` varchar(100) NOT NULL COMMENT 'task title',
  `task_deploy_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'when the task is created,the deploy time is created time',
  `task_deploy_user` int(11) unsigned NOT NULL COMMENT 'the task who have deployed',
  `task_price` float(10,2) NOT NULL COMMENT 'the task price',
  `task_type_codes` varchar(18) NOT NULL COMMENT 'store more dictionary_code,and split for sign '','' as speartor ',
  `task_desc` text COMMENT 'decribe the detail of the task',
  `task_status` tinyint(4) unsigned DEFAULT '0' COMMENT '0 is task is deployed but have not received,1 is running for,2 is sure to cooperated(in our system is done),3 is redeployed',
  PRIMARY KEY (`task_id`),
  KEY `task_deploy_user` (`task_deploy_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_task_list` */

/*Table structure for table `ss_task_order` */

DROP TABLE IF EXISTS `ss_task_order`;

CREATE TABLE `ss_task_order` (
  `order_id` int(11) unsigned NOT NULL COMMENT 'the task is done,and it have been some other person have receiver',
  `order_number` char(12) DEFAULT NULL COMMENT 'the order number',
  `order_status` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '0 for receive the task,1 is executing the task,2 for the task have done',
  `order_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'created order time',
  `order_publisher` int(11) unsigned NOT NULL COMMENT 'the user who deploy the task',
  `order_receiver` int(11) unsigned NOT NULL COMMENT 'the user who receiver the task',
  PRIMARY KEY (`order_id`),
  UNIQUE KEY `order_number` (`order_number`),
  KEY `order_publisher` (`order_publisher`),
  KEY `order_receiver` (`order_receiver`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_task_order` */

/*Table structure for table `ss_user` */

DROP TABLE IF EXISTS `ss_user`;

CREATE TABLE `ss_user` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'userTable primary key',
  `user_email` varchar(50) NOT NULL COMMENT 'user email',
  `user_phone` char(11) DEFAULT NULL COMMENT 'the user phone number',
  `user_pwd` char(32) NOT NULL COMMENT 'encrypt password for md5',
  `user_really_name` varchar(50) DEFAULT 'the user really name',
  `user_alias_name` varchar(50) DEFAULT '' COMMENT 'the user name',
  `user_sex` tinyint(1) unsigned DEFAULT '0' COMMENT '0 is for female,1 is for male',
  `user_auth` char(40) NOT NULL COMMENT 'the user auth,is uesd for verfied,when passwod changed,it also could be changed',
  `user_token` char(40) NOT NULL COMMENT 'use sha1(uuid+uuid) for token',
  `user_token_expires` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'the token expires time',
  `user_longitude` double(10,6) DEFAULT '0.000000' COMMENT 'the user longitude',
  `user_latitude` double(10,6) DEFAULT '0.000000' COMMENT 'the user latitude',
  ##`user_ip` int(12) unsigned DEFAULT NULL COMMENT 'the user ip,use inet_aton change str_ip to num,and use inet_nton change num to str_ip',
  `user_ip` varchar(15) DEFAULT NULL COMMENT 'the user ip',
  `user_label_type` varchar(50) DEFAULT NULL COMMENT 'the user label type,such as java and python dev',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_email` (`user_email`),
#  UNIQUE KEY `user_phone` (`user_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_user` */

/*Table structure for table `ss_user_additional` */

DROP TABLE IF EXISTS `ss_user_additional`;

CREATE TABLE `ss_user_additional` (
  `ua_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'the primary key',
  `user_id` int(11) unsigned NOT NULL COMMENT 'reference on table ss_user',
  `photo_url` varchar(255) DEFAULT NULL COMMENT 'the user photo',
  `domain_desc` text COMMENT 'the description of the user who is good at the domain',
  `work_desc` text COMMENT 'the desc of the user wokring experience',
  PRIMARY KEY (`ua_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_user_additional` */

/*Table structure for table `ss_user_type` */

DROP TABLE IF EXISTS `ss_user_type`;

CREATE TABLE `ss_user_type` (
  `type_id` tinyint(4) unsigned NOT NULL AUTO_INCREMENT COMMENT 'the primary key',
  `type_code` varchar(20) NOT NULL COMMENT 'the type code',
  `type_desc` varchar(200) DEFAULT NULL COMMENT 'the type desc',
  PRIMARY KEY (`type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `ss_user_type` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
