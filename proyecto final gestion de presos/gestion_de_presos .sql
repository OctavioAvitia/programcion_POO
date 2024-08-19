-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-08-2024 a las 05:18:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_de_presos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `crimenes`
--

CREATE TABLE `crimenes` (
  `id` int(11) NOT NULL,
  `Tipo_Crimen` varchar(30) NOT NULL,
  `Condena_Crimen` varchar(30) NOT NULL,
  `Zona_Celda` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `crimenes`
--

INSERT INTO `crimenes` (`id`, `Tipo_Crimen`, `Condena_Crimen`, `Zona_Celda`) VALUES
(1, 'asesinato', '33 años', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guardias`
--

CREATE TABLE `guardias` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Zona_Asig` varchar(30) NOT NULL,
  `Turno` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `guardias`
--

INSERT INTO `guardias` (`id`, `Nombre`, `Zona_Asig`, `Turno`) VALUES
(1, 'edgar', 'zona alta', '8:30-9:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libertad_condicional`
--

CREATE TABLE `libertad_condicional` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Cadena_Cumplida` varchar(30) NOT NULL,
  `Libertad_Condicional` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libertad_condicional`
--

INSERT INTO `libertad_condicional` (`id`, `Nombre`, `Cadena_Cumplida`, `Libertad_Condicional`) VALUES
(1, 'edgar', '33 años', 'bajo custodia ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preso`
--

CREATE TABLE `preso` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Años_Carcel` varchar(30) NOT NULL,
  `Zona_Celda` varchar(30) NOT NULL,
  `Crimen` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `preso`
--

INSERT INTO `preso` (`id`, `Nombre`, `Años_Carcel`, `Zona_Celda`, `Crimen`) VALUES
(4, 'Ale', '3', '0', 'Golpear a un alucin'),
(6, 'jose chavez', 'homicidio ', 'pabellon a', 'homicidio'),
(7, 'jose', '15 años', 'pabellon a', 'homicidio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicacion`
--

CREATE TABLE `ubicacion` (
  `id` int(11) NOT NULL,
  `Zona_celda` varchar(30) NOT NULL,
  `Numero` varchar(30) NOT NULL,
  `Ubicacion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ubicacion`
--

INSERT INTO `ubicacion` (`id`, `Zona_celda`, `Numero`, `Ubicacion`) VALUES
(1, '0', '3', 'zona alta'),
(2, '0', '#4', 'Zona alta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_user` int(11) NOT NULL,
  `user` varchar(60) NOT NULL,
  `con` varchar(10) NOT NULL,
  `horario` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_user`, `user`, `con`, `horario`) VALUES
(1, 'Edgar', '1234', '8:30-9:30'),
(2, 'alejandro', '1234', '8:30-9:30');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `crimenes`
--
ALTER TABLE `crimenes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Zona_Celda` (`Zona_Celda`),
  ADD KEY `Condena_Crimen` (`Condena_Crimen`);

--
-- Indices de la tabla `guardias`
--
ALTER TABLE `guardias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Zona_Asig` (`Zona_Asig`),
  ADD KEY `Turno` (`Turno`);

--
-- Indices de la tabla `libertad_condicional`
--
ALTER TABLE `libertad_condicional`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Cadena_Cumplida` (`Cadena_Cumplida`);

--
-- Indices de la tabla `preso`
--
ALTER TABLE `preso`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Años_Carcel` (`Años_Carcel`),
  ADD KEY `Zona_Celda` (`Zona_Celda`);

--
-- Indices de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Ubicacion` (`Ubicacion`),
  ADD KEY `Zona_celda` (`Zona_celda`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `horario` (`horario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `crimenes`
--
ALTER TABLE `crimenes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `guardias`
--
ALTER TABLE `guardias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `libertad_condicional`
--
ALTER TABLE `libertad_condicional`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `preso`
--
ALTER TABLE `preso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `crimenes`
--
ALTER TABLE `crimenes`
  ADD CONSTRAINT `Zona_Celda` FOREIGN KEY (`Zona_Celda`) REFERENCES `ubicacion` (`id`);

--
-- Filtros para la tabla `guardias`
--
ALTER TABLE `guardias`
  ADD CONSTRAINT `guardias_ibfk_1` FOREIGN KEY (`Zona_Asig`) REFERENCES `ubicacion` (`Ubicacion`),
  ADD CONSTRAINT `guardias_ibfk_2` FOREIGN KEY (`Turno`) REFERENCES `usuarios` (`horario`);

--
-- Filtros para la tabla `libertad_condicional`
--
ALTER TABLE `libertad_condicional`
  ADD CONSTRAINT `libertad_condicional_ibfk_1` FOREIGN KEY (`Cadena_Cumplida`) REFERENCES `crimenes` (`Condena_Crimen`);

--
-- Filtros para la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD CONSTRAINT `ubicacion_ibfk_1` FOREIGN KEY (`Zona_celda`) REFERENCES `preso` (`Zona_Celda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
