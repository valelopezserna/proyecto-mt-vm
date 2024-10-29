-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-10-2019 a las 01:11:31
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
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id` int(11) NOT NULL,
  `apartamento` varchar(200) DEFAULT NULL,
  `casas` varchar(200) DEFAULT NULL,
  `lotes` varchar(200) DEFAULT NULL,
  `fincas` varchar(200) DEFAULT NULL,
  `zona` varchar(5) DEFAULT NULL,
  `barrio` varchar(10) DEFAULT NULL,
  `contacto` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id`, `apartamento`, `casas`, `lotes`, `fincas`, `zona`, `barrio`, `contacto`) VALUES
(1, 'Apartamento para pareja con 1 habitacion, 1 baño, sala, cocina y patio', 'Casa en tercer piso con 3 habitaciones, 1 baños, cocina, comedor y balcon', 'Lote de 151x130 metros', 'Finca de 3 pisos con parqueadero, piscina, jacuzzi, 5 habitaciones, 3 baños,cocina, sala, comedor, patio y cancha', 'Sur', 'Sabaneta', '3370172 - 2867052'),
(2, 'Apartamento con 3 habitaciones, 1 baño, cocina, sala, comedor y zotano', 'Casa de 2 pisos con 3 habitaciones, 1 baño, comedor, cocina, sala y ventanal', 'Lote de 79x98 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Sur', 'Sabaneta', '3370172 - 2867052'),
(3, 'Apartamento de 2 pisos con 3 habitaciones, 1 baño, comedor, sala, biblioteca y patio', 'Casa en tercer piso con 3 habitaciones, 1 baños, cocina, comedor y balcon', 'Lote de 200x180 metro', 'Finca de 3 pisos con parqueadero, piscina, jacuzzi, 5 habitaciones, 3 baños,cocina, sala, comedor, patio y cancha', 'Sur', 'Itagui', '3370172 - 2867052'),
(4, 'Apartamento en tercer piso con 4 habitaciones, 1 baño, comedor, sala, balcon y patio', 'Casa de 2 pisos con 3 habitaciones, 1 baño, comedor, cocina, sala y ventanal', 'Lote de 99x109 metros', 'Finca de dos pisos con 6 habitaciones, 4 baños, cocina, patio, comedor, piscina y salon social', 'Sur', 'Itagui', '3370172 - 2867052'),
(5, 'Apartamento en tercer piso con 4 habitaciones, 1 baño, comedor, sala, balcon y patio', 'Casa en primer piso con 4 habitaciones, 2 baños, patio, sala, comedor y zotano ', 'Lote de 100x98 metros', 'Finca de 3 pisos con parqueadero, piscina, jacuzzi, 5 habitaciones, 3 baños,cocina, sala, comedor, patio y cancha', 'Sur ', 'Estrella', '3370172 - 2867052'),
(6, 'Apartamento de 2 pisos con 3 habitaciones, 1 baño, comedor, sala, biblioteca y patio', 'Casa de tres pisos con 5 habitaciones, 3 baños, patio, zotano, sala y biblioteca ', 'Lote de 200x190 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Sur', 'Estrella', '3370172 - 2867052'),
(7, 'Apartamento con 3 habitaciones, 1 baño, cocina, sala, comedor y zotano', 'Casa de tres pisos con 5 habitaciones, 3 baños, patio, zotano, sala y biblioteca ', 'Lote de 120x220 metros', 'Finca de 3 pisos con 6 habitaciones, 3 baños, cocina, comedor, sala, billar y cancha', 'Sur', 'Envigado', '3370172 - 2867052'),
(8, 'Apartamento para pareja con 1 habitacion, 1 baño, sala, cocina y patio', 'Casa de 2 pisos con 3 habitaciones, 1 baño, comedor, cocina, sala y ventanal', 'Lote de 79x98 metros', 'Finca de dos pisos con 6 habitaciones, 4 baños, cocina, patio, comedor, piscina y salon social', 'Sur', 'Envigado', '3370172 - 2867052'),
(9, 'Apartamento con 3 habitaciones, 1 baño, cocina, sala, comedor y zotano', 'Casa en tercer piso con 3 habitaciones, 1 baños, cocina, comedor y balcon', 'Lote de 99x109 metros', 'Finca de 3 pisos con 6 habitaciones, 3 baños, cocina, comedor, sala, billar y cancha', 'Norte', 'Aranjuez', '3370172 - 2867052'),
(10, 'Apartamento de 2 pisos con 3 habitaciones, 1 baño, comedor, sala, biblioteca y patio', 'Casa de 2 pisos con 3 habitaciones, 1 baño, comedor, cocina, sala y ventanal', 'Lote de 105x103 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Norte', 'Aranjuez', '3370172 - 2867052'),
(11, 'Apartamento para pareja con 1 habitacion, 1 baño, sala, cocina y patio', 'Casa en primer piso con 4 habitaciones, 2 baños, patio, sala, comedor y zotano ', 'Lote de 79x98 metros', 'Finca de dos pisos con 6 habitaciones, 4 baños, cocina, patio, comedor, piscina y salon social', 'Norte', 'Castilla', '3370172 - 2867052'),
(12, 'Apartamento en tercer piso con 4 habitaciones, 1 baño, comedor, sala, balcon y patio', 'Casa en tercer piso con 3 habitaciones, 1 baños, cocina, comedor y balcon', 'Lote de 99x109 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Norte', 'Castilla', '3370172 - 2867052'),
(13, 'Apartamento con 3 habitaciones, 1 baño, cocina, sala, comedor y zotano', 'Casa de tres pisos con 5 habitaciones, 3 baños, patio, zotano, sala y biblioteca ', 'Lote de 120x220 metros', 'Finca de 3 pisos con 6 habitaciones, 3 baños, cocina, comedor, sala, billar y cancha', 'Norte', 'Bello', '3370172 - 2867052'),
(14, 'Apartamento para pareja con 1 habitacion, 1 baño, sala, cocina y patio', 'Casa en primer piso con 4 habitaciones, 2 baños, patio, sala, comedor y zotano ', 'Lote de 79x98 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Norte', 'Bello', '3370172 - 2867052'),
(15, 'Apartamento en tercer piso con 4 habitaciones, 1 baño, comedor, sala, balcon y patio', 'Casa de tres pisos con 5 habitaciones, 3 baños, patio, zotano, sala y biblioteca ', 'Lote de 105x103 metros', 'Finca de 3 pisos con 6 habitaciones, 3 baños, cocina, comedor, sala, billar y cancha', 'Norte', 'Envigado', '3370172 - 2867052'),
(16, 'Apartamento para pareja con 1 habitacion, 1 baño, sala, cocina y patio', 'Casa de 2 pisos con 3 habitaciones, 1 baño, comedor, cocina, sala y ventanal', 'Lote de 120x220 metros', 'Finca con cancha, piscina, parqueadero, 5 habitaciones, 3 baños, cocina, sala y 2 patio', 'Norte', 'Envigado', '3370172 - 2867052');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
