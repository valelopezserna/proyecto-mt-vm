-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-10-2019 a las 01:09:00
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alquiler`
--

CREATE TABLE `alquiler` (
  `id` int(11) NOT NULL,
  `apartamento` varchar(200) DEFAULT NULL,
  `casas` varchar(200) DEFAULT NULL,
  `lotes` varchar(25) DEFAULT NULL,
  `fincas` varchar(200) DEFAULT NULL,
  `zona` varchar(5) DEFAULT NULL,
  `barrio` varchar(10) DEFAULT NULL,
  `contacto` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alquiler`
--

INSERT INTO `alquiler` (`id`, `apartamento`, `casas`, `lotes`, `fincas`, `zona`, `barrio`, `contacto`) VALUES
(1, 'Apartamento para pareja con 1 habitacion, 1 baño, cocina, comedor, sala y patio', 'Casa de 3 pisos con: sala,comedor, 5 habitaciones, 3 baños y patio', 'Lote de 151x130 metros', 'Finca de 2 pisos con coci', 'Sur', 'Sabaneta', '3370172 - 2867052'),
(2, 'Apartamento para pareja con 1 habitacion, 1 baño, cocina, comedor, sala y patio', 'Casa de 3 pisos con: sala,comedor, 5 habitaciones, 3 baños y patio', 'Lote de 151x130 metros', 'Finca de 2 pisos con coci', 'Sur', 'Itagui', '3370172 - 2867052'),
(3, 'Apartamento en cuarto piso con 4 habitaciones, 2 baños, sala, cocina, patio y balcon', 'Casa de 3 pisos con: sala,comedor, 5 habitaciones, 3 baños y patio', 'Lote de 90 x 110 metros', 'Finca de 3 pisos con parq', 'Sur', 'Estrella', '3370172 - 2867052'),
(4, 'Apartamento con 3 habitaciones, 1 baño, cocina, patio y sala', 'Casa de 3 pisos con: sala,comedor, 5 habitaciones, 3 baños y patio', 'Lote de 168x144 metros', 'Finca doble. Primera part', 'Sur', 'Envigado', '3370172 - 2867052'),
(5, 'Apartamento en cuarto piso con 4 habitaciones, 2 baños, sala, cocina, patio y balcon', 'Casa en tercer piso con 3 habitaciones, 1 baño, cocina y patio', 'Lote de 151x130 metros', 'Finca con 5 habitaciones,', 'Sur', 'Sabaneta', '3370172 - 2867052'),
(6, 'Apartamento en cuarto piso con 4 habitaciones, 2 baños, sala, cocina, patio y balcon', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 79x98 metros', 'Finca con cancha, piscina', 'Sur', 'Itagui', '3370172 - 2867052'),
(7, 'Apartamento para pareja con 1 habitacion, 1 baño, cocina, comedor, sala y patio', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 151x130 metros', 'Finca de 3 pisos con parq', 'Sur', 'Estrella', '3370172 - 2867052'),
(8, 'Apartamento en cuarto piso con 4 habitaciones, 2 baños, sala, cocina, patio y balcon', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 168x144 metros', 'Finca con cancha, piscina', 'Sur', 'Envigado', '3370172 - 2867052'),
(9, 'Apartamento para pareja con 1 habitacion, 1 baño, cocina, comedor, sala y patio', 'Casa en tercer piso con 3 habitaciones, 1 baño, cocina y patio', 'Lote de 151x130 metros', 'Finca de 2 pisos con 4 ha', 'Norte', 'Aranjuez', '3370172 - 2867052'),
(10, 'Apartamento con 3 habitaciones, 1 baño, cocina, patio y sala', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 79x98 metros', 'Finca con cancha, piscina', 'Norte', 'Castilla', '3370172 - 2867052'),
(11, 'Apartamento en sexto piso con 4 habitaciones, 1 baño, cocina, sala y patio', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 200x180 metro', 'Finca de 2 pisos con 5 ha', 'Norte', 'Bello', '3370172 - 2867052'),
(12, 'Apartamento con 3 habitaciones, 1 baño, cocina, patio y sala', 'Casa de 3 pisos con: sala,comedor, 5 habitaciones, 3 baños y patio', 'Lote de 99x109 metros', 'Finca con 3 habitaciones,', 'Norte', 'San Javier', '3370172 - 2867052'),
(13, 'Apartamento en cuarto piso con 4 habitaciones, 2 baños, sala, cocina, patio y balcon', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 151x130 metros', 'Finca con 5 habitaciones,', 'Norte', 'Aranjuez', '3370172 - 2867052'),
(14, 'Apartamento en sexto piso con 4 habitaciones, 1 baño, cocina, sala y patio', 'Casa en tercer piso con 3 habitaciones, 1 baño, cocina y patio', 'Lote de 79x98 metros', 'Finca con cancha, piscina', 'Norte', 'Castilla', '3370172 - 2867052'),
(15, 'Apartamento con 4 habitaciones, 1 baño, sala, cocina, comedor y patio', 'Casa en tercer piso con 3 habitaciones, 1 baño, cocina y patio', 'Lote de 200x180 metro', 'Finca de 3 pisos con 6 ha', 'Norte', 'Bello', '3370172 - 2867052'),
(16, 'Apartamento para pareja con 1 habitacion, 1 baño, cocina, comedor, sala y patio', 'Casa de 2 pisos con 3 habitaciones, 2 baños, cocina, sala, comedor y patio', 'Lote de 99x109 metros', 'Finca con cancha, piscina', 'Norte', 'San Javier', '3370172 - 2867052');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alquiler`
--
ALTER TABLE `alquiler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
