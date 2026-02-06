-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 13, 2024 at 05:35 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1watermarkdata`
--

-- --------------------------------------------------------

--
-- Table structure for table `filetb`
--

CREATE TABLE `filetb` (
  `id` bigint(20) NOT NULL auto_increment,
  `OwnerName` varchar(250) NOT NULL,
  `FileInfo` varchar(500) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `Pukey` varchar(250) NOT NULL,
  `Pvkey` varchar(250) NOT NULL,
  `hash1` varchar(250) NOT NULL,
  `hash2` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `filetb`
--

INSERT INTO `filetb` (`id`, `OwnerName`, `FileInfo`, `FileName`, `Pukey`, `Pvkey`, `hash1`, `hash2`) VALUES
(1, 'san', 'my image', '65576.jpg', '03c92a8fe803acc2447c4782066231b4113fb856125c03398bb451ef0d2e36d758', '9aa81e5ffec3630caa94d190076705d9ae43d40f24b1671b24364c6fe58ed7a8', '0', '5C317E9BABDAE103B8718A301C28D1371358235A8F32B926E00888AE7666834B');

-- --------------------------------------------------------

--
-- Table structure for table `ownertb`
--

CREATE TABLE `ownertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `ownertb`
--

INSERT INTO `ownertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `LoginKey`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Active', '5922');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `LoginKey`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Active', '7435');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `temptb`
--


-- --------------------------------------------------------

--
-- Table structure for table `userfiletb`
--

CREATE TABLE `userfiletb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FileId` varchar(250) NOT NULL,
  `OwnerName` varchar(250) NOT NULL,
  `Filename` varchar(250) NOT NULL,
  `PrKey` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `ImageName` varchar(250) NOT NULL,
  `Imagedkey` varchar(250) NOT NULL,
  `Unhidekey` varchar(250) NOT NULL,
  `Decryptkey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `userfiletb`
--

INSERT INTO `userfiletb` (`id`, `FileId`, `OwnerName`, `Filename`, `PrKey`, `UserName`, `Status`, `ImageName`, `Imagedkey`, `Unhidekey`, `Decryptkey`) VALUES
(1, '1', 'san', '65576.jpg', '9aa81e5ffec3630caa94d190076705d9ae43d40f24b1671b24364c6fe58ed7a8', 'san', 'Approved', '253gg3.png', '975d76762e5c362b39ed62eddbc3ea11eee553d0c5647e76aeff526117e22245', '123', 'VE9WXMrc8d9SkRGvsRiXO0VB9yfjTzyGP4pV1e7JN4c=');
