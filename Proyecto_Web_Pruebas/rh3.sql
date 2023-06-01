-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-05-2023 a las 09:37:47
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agregar_requisicion`
--

CREATE TABLE `agregar_requisicion` (
  `idrequisicion` int(100) NOT NULL,
  `folio` int(100) NOT NULL,
  `fecha_ela` date NOT NULL,
  `puesto_cubrir` varchar(100) NOT NULL,
  `nombre_solicita` varchar(100) NOT NULL,
  `fecha_reclutamiento` date NOT NULL,
  `fecha_inicio_vacante` date NOT NULL,
  `numerodevaca` int(100) NOT NULL,
  `tipo_vacante` varchar(100) NOT NULL,
  `estado` int(100) NOT NULL,
  `idArea` int(100) NOT NULL,
  `idVacantess` int(100) NOT NULL,
  `idPublicado` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `agregar_requisicion`
--

INSERT INTO `agregar_requisicion` (`idrequisicion`, `folio`, `fecha_ela`, `puesto_cubrir`, `nombre_solicita`, `fecha_reclutamiento`, `fecha_inicio_vacante`, `numerodevaca`, `tipo_vacante`, `estado`, `idArea`, `idVacantess`, `idPublicado`) VALUES
(57, 402, '2023-05-16', 'INGENIERIA', 'IAN', '2023-05-24', '2023-05-19', 5, 'INFORMAL', 1, 2, 3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL,
  `descripcion` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `descripcion`) VALUES
(1, 'DIRECCION GENERAL'),
(2, 'ADMINISTRACION Y RECURSOS HUMANOS'),
(3, 'PRODUCCION'),
(4, 'FINANZAS Y CONTABILIDAD'),
(5, 'MERCADOTECNIA'),
(6, 'INFORMATICA - SISTEMAS COMPUTACIONALES');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autorizacion`
--

CREATE TABLE `autorizacion` (
  `folio` int(100) NOT NULL,
  `puesto_cubrir` varchar(100) NOT NULL,
  `numerodevaca` int(100) NOT NULL,
  `revisado` varchar(100) NOT NULL,
  `autorizado` varchar(100) NOT NULL,
  `nombre_puesto` varchar(100) NOT NULL,
  `solicitud_puesto` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `autorizacion`
--

INSERT INTO `autorizacion` (`folio`, `puesto_cubrir`, `numerodevaca`, `revisado`, `autorizado`, `nombre_puesto`, `solicitud_puesto`) VALUES
(0, '', 0, 'LUIS', 'DIEGO', 'OKEI', 0),
(0, '', 0, 'LUIS', 'DIEGO', 'INGENIERIA', 0),
(0, '', 0, '', '', '', 0),
(0, '', 0, 'DIEGO', 'IAN', 'INGENIERIA', 0),
(0, '', 0, '', '', '', 0),
(0, '', 0, 'LUIS', 'DIEGO', 'INGENIERIA', 0),
(0, '', 0, 'sads', 'sada', 'asdas', 43),
(0, '', 0, 'IAN', 'DIEGO', 'INGENIERIA', 44),
(0, '', 0, 'IAN', 'LEO', 'INGENIERIA', 45),
(0, '', 0, 'LUIS', 'LEO', 'INGENIERIA', 46),
(0, '', 0, '', '', '', 49),
(0, '', 0, 'rtr', '', 'sfsdf', 48),
(0, '', 0, '', '', '', 50),
(0, '', 0, 'LEO', 'GABY', 'INGENIERIA', 51),
(0, '', 0, '', '', '', 52),
(0, '', 0, '', '', '', 54),
(0, '', 0, '', '', '', 55),
(0, '', 0, 'OKEI', 'IAN', 'MECATRONICA', 56),
(0, '', 0, 'IAN', 'DIEGO', 'DERECHO', 57);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `idCarrera` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `descripcion`) VALUES
(1, 'NO APLICA'),
(2, 'ADMINISTRACION DE EMPRESAS'),
(3, 'ADMINISTRACIÓN DE PRODUCCIÓN Y SERVICIOS'),
(4, 'ADMINISTRACIÓN FINANCIERA'),
(5, 'COMERCIO INTERNACIONAL'),
(6, 'COMERCIO ELECTRONICO'),
(7, 'COMUNICACION'),
(8, 'CONTADOR '),
(9, 'DERECHO'),
(10, 'ECONOMIA'),
(11, 'GESTION TURISTICA'),
(12, 'LOGISTICA EMPRESARIAL'),
(13, 'MERCADOTECNIA'),
(14, 'SISTEMAS COMPUTACIONALES Y AFINES'),
(15, 'INDUSTRIAL'),
(16, 'ELECTRICA'),
(17, 'ROBOTICA'),
(18, 'RELACIONES INDUSTRIALES'),
(19, 'PSICOLOGIA'),
(20, 'ELECTRONICA'),
(21, 'GESTION EMPRESARIAL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docto_solic`
--

CREATE TABLE `docto_solic` (
  `idDoctoSolic` int(11) NOT NULL,
  `descripcion` varchar(70) NOT NULL,
  `original` varchar(2) NOT NULL,
  `numCopias` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `docto_solic`
--

INSERT INTO `docto_solic` (`idDoctoSolic`, `descripcion`, `original`, `numCopias`) VALUES
(1, 'Solicitud de empleo', 'SI', 1),
(2, 'CURRICULUM VITAE con fotografía', 'SI', 1),
(3, 'Carta de presentación', 'SI', 1),
(4, 'Carta de recomendación', 'SI', 1),
(5, 'Comprobante de domicilio reciente', 'NO', 2),
(6, 'Acta de nacimiento', 'SI', 1),
(7, 'Número del seguro social', 'NO', 2),
(8, 'CURP', 'NO', 2),
(9, 'Credencial para votar', 'NO', 2),
(10, 'Licencia automovilista', 'NO', 2),
(11, 'Licencia chofer', 'NO', 2),
(12, 'Certificado Carrera Comercial o Técnica', 'NO', 2),
(13, 'Certificado Preparatoria o Equivalente', 'NO', 2),
(14, 'Certificado Licenciatura o Equivalente', 'NO', 2),
(15, 'Constancia de Estudios', 'SI', 2),
(16, 'Carta de Pasante Carrera Técnica', 'NO', 2),
(17, 'Carta de Pasante Licenciatura', 'NO', 2),
(18, 'Carta de Pasante Posgrado', 'NO', 2),
(19, 'Cédula Profesional', 'NO', 2),
(20, 'Título Licenciatura', 'NO', 2),
(21, 'Título Posgrado', 'NO', 2),
(22, 'Certificado Médico', 'SI', 2),
(23, 'Antecedentes No penales', 'Si', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `idEscolaridad` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idEscolaridad`, `descripcion`) VALUES
(1, 'NO APLICA / NO REQUERIDA '),
(2, 'PREPARATORIA'),
(3, 'CARRERA TÉCNICA O COMERCIAL'),
(4, 'BACHILLERATO TÉCNICO O ESPECIALIZADO'),
(5, 'TÉCNICO SUPERIOR UNIVERSITARIO'),
(6, 'LICENCIATURA / INGENIERÍA / PROFESIONAL'),
(7, 'MAESTRIA'),
(8, 'DOCTORADO'),
(9, 'kinder según andrei');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_civil`
--

CREATE TABLE `estado_civil` (
  `idEstadoCivil` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estado_civil`
--

INSERT INTO `estado_civil` (`idEstadoCivil`, `descripcion`) VALUES
(1, 'INDISTINTO'),
(2, 'SOLTERO'),
(3, 'CASADO'),
(4, 'UNION LIBRE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grado_avance`
--

CREATE TABLE `grado_avance` (
  `idGradoAvance` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `grado_avance`
--

INSERT INTO `grado_avance` (`idGradoAvance`, `descripcion`) VALUES
(1, 'NO APLICA'),
(2, 'CURSANDO'),
(3, 'TERMINADO'),
(4, 'INCONCLUSO'),
(5, 'PASANTE'),
(6, 'TITULADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `idHabilidad` int(11) NOT NULL,
  `descripcion` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`idHabilidad`, `descripcion`) VALUES
(1, 'NO REQUERIDAS'),
(2, 'FACILIDAD DE PALABRA'),
(3, 'MANEJO DE CONFLICTOS'),
(4, 'CAPACIDAD PARA TRABAJAR BAJO PRESION'),
(5, 'CAPACIDAD DE TRABAJO EN EQUIPO'),
(6, 'TOMA DE DECISIONES'),
(7, 'PENSAMIENTO CREATIVO'),
(8, 'PENSAMIENTO CRITICO'),
(9, 'MANEJO DE EMOCIONES'),
(10, 'PROACTIVIDAD'),
(11, 'PROFESIONALIDAD'),
(12, 'ESCUCHA ACTIVA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `idIdioma` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `descripcion`) VALUES
(1, 'NO REQUERIDO'),
(2, 'INGLES BASICO'),
(3, 'INGLES INTERMEDIO'),
(4, 'INGLES AVANZADO'),
(5, 'JAPONES BASICO'),
(6, 'JAPONES CONVERSACIONAL'),
(7, 'JAPONES ESCRITO Y CONVERSACIONAL'),
(9, 'ALEMAN AVANZADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediopublic`
--

CREATE TABLE `mediopublic` (
  `idMedioPublic` int(11) NOT NULL,
  `descripcion` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `mediopublic`
--

INSERT INTO `mediopublic` (`idMedioPublic`, `descripcion`) VALUES
(1, 'Convocatoria en áreas estratégicas de la empresa'),
(2, 'Sitio web de la empresa'),
(3, 'Servicio estatal de empleo'),
(4, 'Redes sociales para empleo'),
(5, 'Agencia particular de empleo'),
(6, 'Radio'),
(7, 'Televisión'),
(8, 'Periódico Digital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicacion_detalle`
--

CREATE TABLE `publicacion_detalle` (
  `idPublicado` int(100) NOT NULL,
  `fecha_inicio_publicacion` date NOT NULL,
  `fecha_conclusion_publicacion` date NOT NULL,
  `guardado` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `publicacion_detalle`
--

INSERT INTO `publicacion_detalle` (`idPublicado`, `fecha_inicio_publicacion`, `fecha_conclusion_publicacion`, `guardado`) VALUES
(5, '2023-05-12', '2023-05-24', 0),
(4, '2023-05-16', '2023-05-06', 0),
(5, '2023-05-11', '2023-05-17', 0),
(3, '2023-05-17', '2023-05-30', 0),
(4, '0000-00-00', '0000-00-00', 0),
(4, '2023-05-23', '2023-05-04', 0),
(6, '2023-05-10', '2023-05-17', 0),
(3, '2023-05-19', '2023-05-15', 0),
(2, '2023-05-12', '2023-05-16', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicado`
--

CREATE TABLE `publicado` (
  `idPublicado` int(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `publicado`
--

INSERT INTO `publicado` (`idPublicado`, `descripcion`) VALUES
(1, 'TELEVISION'),
(2, 'RADIO'),
(3, 'REDES SOCIALES'),
(4, 'PERIODICO DIGITAL'),
(5, 'PERIODICO'),
(6, 'SITIO WEB DE LA EMPRESA'),
(7, 'AREAS DE LAS EMPRESAS'),
(8, 'OTRO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'V009', 2, 'SUPERVISOR DE TIENDA ', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'VENTAS AL PÚBLICO', 'VENDER', '18 A 45 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(3, 'v0008', 3, 'OBRERO', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'maquilar', 'trabajar', '18 A 45 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(4, 'v010', 6, 'PROGRAMADOR', 'LIDER DE PROYECTO', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 10000, 'DE LEY', 'ELABORACION DE SISTEMAS COMPUTACIONALES', 'PROGRAMAR, ANALISIS DE SISTEMAS', '18 a 70 años', 'Indistinto', 1, 3, 5, 14, '2 AÑOS', 'PROGRAMACION EN LENGUAJES JAVA, PYTHO, MANEJO DE BASES DE DATOS ', 'DE COMPUTO', 'NO NECESARIOS', 'NO NECESARIOS', 'NO ESPECIFICADAS', 'AGRADABLES'),
(5, 'p001', 5, 'JEFE DE MERCADOTECNIA', 'GERENTE', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 6500, 'DE LEY', 'COORDINAR A PERSONAL DE MERCADOTECNIA', 'CORDINACIÓN', '25 A 50', 'Indistinto', 1, 3, 4, 13, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto_has_habilidad`
--

INSERT INTO `puesto_has_habilidad` (`idPuesto`, `idHabilidad`) VALUES
(3, 4),
(3, 5),
(4, 5),
(4, 7),
(4, 8),
(4, 10),
(4, 11),
(5, 2),
(5, 3),
(5, 4),
(5, 5),
(5, 6),
(5, 7),
(5, 8),
(5, 9),
(5, 10),
(5, 11),
(5, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`) VALUES
(3, 1),
(4, 2),
(5, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacante`
--

CREATE TABLE `vacante` (
  `idVacantess` int(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vacante`
--

INSERT INTO `vacante` (`idVacantess`, `descripcion`) VALUES
(1, 'NO REQUERIDO'),
(2, 'BAJA '),
(3, 'INCAPACIDAD'),
(4, 'LICENCIA O PERMISO'),
(5, 'NUEVA CREACION'),
(6, 'DEFUNCION'),
(7, 'OTRO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacantes`
--

CREATE TABLE `vacantes` (
  `idVacantes` int(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vacantes`
--

INSERT INTO `vacantes` (`idVacantes`, `descripcion`) VALUES
(1, 'NO REQUERIDO'),
(2, 'BAJA'),
(3, 'INCAPACIDAD'),
(4, 'LICENCIA O PERMISO'),
(5, 'NUEVA CREACION'),
(6, 'DEFUNCION'),
(7, 'OTRO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacantes_generadas_por`
--

CREATE TABLE `vacantes_generadas_por` (
  `idrequisicion` int(100) NOT NULL,
  `idVacantes` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agregar_requisicion`
--
ALTER TABLE `agregar_requisicion`
  ADD PRIMARY KEY (`idrequisicion`);

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idCarrera`);

--
-- Indices de la tabla `docto_solic`
--
ALTER TABLE `docto_solic`
  ADD PRIMARY KEY (`idDoctoSolic`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`idEscolaridad`);

--
-- Indices de la tabla `estado_civil`
--
ALTER TABLE `estado_civil`
  ADD PRIMARY KEY (`idEstadoCivil`);

--
-- Indices de la tabla `grado_avance`
--
ALTER TABLE `grado_avance`
  ADD PRIMARY KEY (`idGradoAvance`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`idHabilidad`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`idIdioma`);

--
-- Indices de la tabla `mediopublic`
--
ALTER TABLE `mediopublic`
  ADD PRIMARY KEY (`idMedioPublic`);

--
-- Indices de la tabla `publicado`
--
ALTER TABLE `publicado`
  ADD PRIMARY KEY (`idPublicado`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);

--
-- Indices de la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD PRIMARY KEY (`idPuesto`,`idHabilidad`),
  ADD KEY `idHabilidad` (`idHabilidad`);

--
-- Indices de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD PRIMARY KEY (`idPuesto`,`idIdioma`),
  ADD KEY `idIdioma` (`idIdioma`);

--
-- Indices de la tabla `vacante`
--
ALTER TABLE `vacante`
  ADD PRIMARY KEY (`idVacantess`);

--
-- Indices de la tabla `vacantes`
--
ALTER TABLE `vacantes`
  ADD PRIMARY KEY (`idVacantes`);

--
-- Indices de la tabla `vacantes_generadas_por`
--
ALTER TABLE `vacantes_generadas_por`
  ADD PRIMARY KEY (`idrequisicion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agregar_requisicion`
--
ALTER TABLE `agregar_requisicion`
  MODIFY `idrequisicion` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idCarrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `docto_solic`
--
ALTER TABLE `docto_solic`
  MODIFY `idDoctoSolic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  MODIFY `idEscolaridad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `estado_civil`
--
ALTER TABLE `estado_civil`
  MODIFY `idEstadoCivil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `grado_avance`
--
ALTER TABLE `grado_avance`
  MODIFY `idGradoAvance` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `idHabilidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `idIdioma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `mediopublic`
--
ALTER TABLE `mediopublic`
  MODIFY `idMedioPublic` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `publicado`
--
ALTER TABLE `publicado`
  MODIFY `idPublicado` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vacante`
--
ALTER TABLE `vacante`
  MODIFY `idVacantess` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `vacantes`
--
ALTER TABLE `vacantes`
  MODIFY `idVacantes` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `vacantes_generadas_por`
--
ALTER TABLE `vacantes_generadas_por`
  MODIFY `idrequisicion` int(100) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
