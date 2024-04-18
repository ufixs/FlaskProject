/*
 Navicat MySQL Data Transfer

 Source Server         : demo
 Source Server Type    : MySQL
 Source Server Version : 80034
 Source Host           : localhost:3306
 Source Schema         : flaskdb

 Target Server Type    : MySQL
 Target Server Version : 80034
 File Encoding         : 65001

 Date: 18/12/2023 10:59:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `a_id` int(0) NOT NULL AUTO_INCREMENT,
  `a_username` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `a_password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`a_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', '123456');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `c_id` int(0) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `c_grade` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`c_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, '软件工程2001', '20');
INSERT INTO `class` VALUES (2, '软件工程2101', '21');
INSERT INTO `class` VALUES (3, '软件工程2201', '22');
INSERT INTO `class` VALUES (4, '软件工程2301', '23');
INSERT INTO `class` VALUES (5, '软件工程2106', '21');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `s_id` int(0) NOT NULL AUTO_INCREMENT,
  `c_id` int(0) NOT NULL,
  `s_name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `s_age` int(0) NULL DEFAULT NULL,
  `s_sex` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`s_id`) USING BTREE,
  INDEX `c_id`(`c_id`) USING BTREE,
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `class` (`c_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, 1, '张三', 18, '男');
INSERT INTO `student` VALUES (2, 1, '李四', 17, '女');
INSERT INTO `student` VALUES (3, 2, '王五', 16, '男');
INSERT INTO `student` VALUES (4, 1, '赵六', 18, '男');
INSERT INTO `student` VALUES (8, 1, '许文莹', 21, '男');
INSERT INTO `student` VALUES (13, 1, '坛洛', 21, '男');
INSERT INTO `student` VALUES (14, 1, '坛洛', 21, '男');
INSERT INTO `student` VALUES (15, 2, '坛洛', 21, '男');
INSERT INTO `student` VALUES (16, 1, '坛洛', 12, '男');
INSERT INTO `student` VALUES (17, 2, '坛洛', 23, '男');
INSERT INTO `student` VALUES (18, 3, '坛洛、', 21, '男');

SET FOREIGN_KEY_CHECKS = 1;
