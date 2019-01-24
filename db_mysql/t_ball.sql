/*
Navicat MySQL Data Transfer

Source Server         : Mysql
Source Server Version : 80013
Source Host           : localhost:3306
Source Database       : ball

Target Server Type    : MYSQL
Target Server Version : 80013
File Encoding         : 65001

Date: 2019-01-22 11:54:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_ball
-- ----------------------------
DROP TABLE IF EXISTS `t_ball`;
CREATE TABLE `t_ball` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` varchar(30) DEFAULT NULL,
  `red_ball` varchar(30) DEFAULT NULL,
  `blue_ball` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_ball
-- ----------------------------
