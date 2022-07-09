-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2022 at 08:19 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `image`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `message` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `message`) VALUES
(1, 'manisha', 'techhuub@gmail.com', 'about wepage', 'dfsdfsdfdsfgdfgdfgdfgsdfbfghfdghdfghdfghdfgh'),
(2, 'manisha', 'techhuub@gmail.com', 'about wepage', 'dfsdfsdfdsfgdfgdfgdfgsdfbfghfdghdfghdfghdfgh'),
(3, 'manisha', 'techhuub@gmail.com', 'about wepage', 'dfsdfsdfdsfgdfgdfgdfgsdfbfghfdghdfghdfghdfgh'),
(4, 'manisha', 'techhuub@gmail.com', 'about wepage', 'dfsdfsdfdsfgdfgdfgdfgsdfbfghfdghdfghdfghdfgh'),
(5, 'manisha', 'techhuub@gmail.com', 'about wepage', 'dfsdfsdfdsfgdfgdfgdfgsdfbfghfdghdfghdfghdfgh');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cpassword` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `uname`, `email`, `password`, `cpassword`) VALUES
(1, 'manisha', 'manishas', 'techhub@gmail.com', 'tech@123', 'tech@123'),
(2, 'manisha', 'manishas', 'manisha@gmail.com', '123456789', '123456789'),
(3, 'bdgbd', 'fdgdfg', 'xvgfdsg@co.in', '12345678', '12345678'),
(4, 'Shrushti', 'ShrushtiV', 'shrushti@gmail.com', 'shrushti', 'shrushti');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
