#### User Module #####
DROP TABLE IF EXISTS `ss_user`;

CREATE TABLE `ss_user` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'userTable primary key',
  `user_email` varchar(50) NOT NULL COMMENT 'user email',
  `user_phone` char(11) DEFAULT NULL COMMENT 'the user phone number',
  `user_pwd` char(32) NOT NULL COMMENT 'encrypt password for md5',
  `user_really_name` varchar(50) DEFAULT 'the user really name',
  `user_alias_name` varchar(50) DEFAULT '' COMMENT 'the user name',
  `user_sex` tinyint(1) unsigned DEFAULT 0 COMMENT '0 is for female,1 is for male',
  `user_auth` char(40) NOT NULL COMMENT 'the user auth,is uesd for verfied,when passwod changed,it also could be changed',
  `user_token` char(40) NOT NULL COMMENT 'use sha1(uuid+uuid) for token',
  `user_token_expires` double NOT NULL COMMENT 'the token expires time', 
  `user_longitude` double(10,6) DEFAULT '0.000000' COMMENT 'the user longitude',
  `user_latitude` double(10,6) DEFAULT '0.000000' COMMENT 'the user latitude',
  `user_ip` int(11) unsigned DEFAULT NULL COMMENT 'the user ip',
  `user_label_type` varchar(50) DEFAULT NULL COMMENT 'the user label type,such as java and python dev',
  `user_type` tinyint(1) unsigned DEFAULT 0 COMMENT '0 is asker,1 is helper',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_email` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ss_user_additional` */

DROP TABLE IF EXISTS `ss_user_additional`;

CREATE TABLE `ss_user_additional` (
  `ua_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'the primary key',
  `user_id` int(11) unsigned NOT NULL COMMENT 'reference on table ss_user',
  `photo_url` varchar(200) DEFAULT NULL COMMENT 'the user photo',
  `domain_desc` longtext COMMENT 'the description of the user who is good at the domain',
  `work_desc` longtext COMMENT 'the desc of the user wokring experience',
  PRIMARY KEY (`ua_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `ss_user_additional` */


DROP TABLE IF EXISTS `ss_label_type`;

CREATE TABLE `ss_label_type` (
  `type_id` tinyint(4) unsigned NOT NULL AUTO_INCREMENT COMMENT 'the primary key',
  `type_code` varchar(20) NOT NULL COMMENT 'the type code',
  `type_desc` varchar(200) NOT NULL COMMENT 'the type desc',
  `parent_code` varchar(20) NOT NULL default '0' COMMENT 'the key references on itself',
  PRIMARY KEY (`type_id`),
  KEY `parent_code` (`parent_code`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

##TODO,not need now
## ss_user_label
##DROP TABLE IF EXISTS `ss_user_label`;

##CREATE TABLE `ss_user_label`(
##   ul_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'the ss_user_label primary key',
##   user_id INT(11) UNSIGNED NOT NULL COMMENT 'the ss_user id',
##   label_code VARCHAR(20) NOT NULL COMMENT 'the ss_label_type type_code',   
##   PRIMARY KEY(ul_id)
##)ENGINE=INNODB DEFAULT CHARSET=utf8;

#### Questions Module #####
DROP TABLE IF EXISTS `ss_question`;

CREATE TABLE `ss_question` (
  `qt_id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `qt_title` VARCHAR(60) DEFAULT NULL COMMENT 'the title for quetsion',
  `qt_desc` LONGTEXT COMMENT 'the consult detail ',
  `qt_status` CHAR(1) DEFAULT '0' COMMENT '0 is waitting,1 is executing,2 is done',
  `qt_begin_time` DOUBLE NOT NULL DEFAULT 0.00 COMMENT 'the create time',
  `qt_end_time` DOUBLE NOT NULL DEFAULT 0.00 COMMENT 'the end time',
  `qt_type_codes` VARCHAR(50) NOT NULL COMMENT 'store more dictionary_code,and split for sign '','' as speartor ',
  `qt_ask_user` INT(11) UNSIGNED NOT NULL COMMENT 'the user who ask the question,references on ss_user',
  `qt_answer_user` INT(11) UNSIGNED NOT NULL COMMENT 'the user who answer the question',
  `groom_degree` CHAR(1) DEFAULT '0' COMMENT 'qt_answer_user_groom_degree,0 is not checked groom degree,1 is for lowest,2 is for lower,3 is medium,4 is high',
  `server_degree` CHAR(1) DEFAULT '0' COMMENT 'qt_answer_user_server_degree,0 is not checked,the same as con_groom_degree ',
  `ability_degree` CHAR(1) DEFAULT '0' COMMENT 'qt_answer_user_ability_degree,0 is not checked,others are the same as above',
  `qt_answer_remarked` LONGTEXT DEFAULT NULL COMMENT 'the asker remark the answerer',
  PRIMARY KEY (`qt_id`),
  KEY `qt_ask_user` (`qt_ask_user`),
  KEY `qt_answer_user` (`qt_answer_user`),
  KEY `qt_status` (`qt_status`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

## task 
DROP TABLE IF EXISTS `ss_task`;
CREATE TABLE `ss_task` (
   `task_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
   `task_title` varchar(100) NOT NULL COMMENT 'task title',
   `task_deploy_time` double NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'when the task is created,the deploy time is created time',
   `task_deploy_user` int(11) unsigned NOT NULL COMMENT 'the task who have deployed',
   `task_price` float(10,2) NOT NULL COMMENT 'the task price',
   `task_type_codes` varchar(50) NOT NULL COMMENT 'store more dictionary_code,and split for sign '','' as speartor ',
   `task_desc` longtext DEFAULT NULL COMMENT 'decribe the detail of the task',
   `task_status` char(1) DEFAULT '0' COMMENT '0 is task is deployed but have not received,1 is sure to cooperated(in our system is done),2 is redeployed',
   PRIMARY KEY (`task_id`),
   KEY `task_deploy_user` (`task_deploy_user`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


##invite_task
DROP TABLE IF EXISTS `ss_invite_project`;

CREATE TABLE `ss_invite_project`(
  	project_id int(11) unsigned NOT NULL COMMENT 'the primary key',
	project_publisher int(11) unsigned NOT NULL COMMENT 'the project publisher id ',
	project_invitors varchar(50) NOT NULL COMMENT 'the project invitor id,at most 3,it store as id1,id2,id3',
	##project_title varchar(20) NOT NULL COMMENT 'the invitor project title',
	project_context LONGTEXT NOT NULL COMMENT 'the project detail text',
  	##project_status char(1) not null default '0' COMMENT '0 is published,1 is inviting,2 is excuting the project,3 is done',
	project_time DOUBLE not null default 0.00 COMMENT 'the time of the published project',
	PRIMARY KEY (`project_id`),
    KEY `task_deploy_user` (`project_publisher`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

## sys info 
DROP TABLE IF EXISTS `ss_apps_feedback`;

CREATE TABLE `ss_apps_feedback` (
  `feed_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `feed_email` varchar(50) DEFAULT NULL COMMENT 'the user who feedback the opinion with the apps',
  `feed_context` longtext NOT NULL COMMENT 'user feedback the apps',
  PRIMARY KEY (`feed_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
