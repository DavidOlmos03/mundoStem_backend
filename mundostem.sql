-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-02-2024 a las 03:32:29
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mundostem`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `authors` varchar(255) NOT NULL,
  `language` varchar(50) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `pages` int(11) DEFAULT NULL,
  `extension` varchar(10) DEFAULT NULL,
  `size` decimal(10,2) DEFAULT NULL,
  `summary` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `book`
--

INSERT INTO `book` (`id`, `title`, `authors`, `language`, `subject`, `pages`, `extension`, `size`, `summary`) VALUES
(1, 'Cálculo Integral', 'Michael Spivak', 'Español', 'Cálculo', 400, 'PDF', '10.00', 'Libro introductorio al cálculo integral, cubriendo conceptos básicos y técnicas de integración.'),
(2, 'Álgebra Lineal', 'Howard Anton, Chris Rorres', 'Inglés', 'Álgebra', 600, 'EPUB', '8.00', 'Texto completo sobre álgebra lineal, con énfasis en la teoría y aplicaciones en el campo de la ciencia y la ingeniería.'),
(3, 'Geometría Analítica', 'Charles H. Lehmann', 'Español', 'Geometría', 350, 'MOBI', '12.00', 'Libro clásico de geometría analítica, con enfoque en la representación gráfica de ecuaciones y transformaciones geométricas.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `full_name`, `email_address`, `password`) VALUES
(1, 'Juan David Ruiz', 'juan@email.com', '$bcrypt-sha256$v=2,t=2b,r=12$QOMMl26IDhfu7.g2wqcbge$JLMRfuE9gSomj8mpagYz5dYmH3kMK6u'),
(2, 'Hernan Sanchez', 'hernan@correo.com', '$bcrypt-sha256$v=2,t=2b,r=12$ELFpOceA45odAwjPqq8PI.$PGDN7pIRke6V3YnlZJ8DBI4G5vc/jWu'),
(13, 'Juan David Olmos', 'david@email.com', '$bcrypt-sha256$v=2,t=2b,r=12$9RrkMn3.CQS0UOxaeNI1f.$D/IxVWqzA9eQNXWL0eiStsswENQb/GC');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
