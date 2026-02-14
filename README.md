# Proyecto Fase 1 - Limpieza básica de dataset con Pandas

## Descripción
Este proyecto realiza la limpieza básica de un dataset personal usando Pandas en Python.  
Se modulariza la limpieza en funciones puras dentro de archivos separados.

## Dataset
Archivo utilizado: `EPM8_Personas.csv`  
Ubicación: carpeta `data/` (subida al repositorio)

## Limpieza aplicada
- Normalización de nombres de columnas (minúsculas, sin espacios)
- Eliminación de espacios en strings
- Eliminación de filas duplicadas
- Eliminación de filas vacías

## Cómo usar el proyecto

1. Clonar o descargar el repositorio.  
2. Ejecutar el archivo principal `main.py` dentro de la carpeta `src` con:


python main.py


## Resumen Ejecutivo

Este proyecto implementa un pipeline modular para la limpieza básica de un dataset personal utilizando la biblioteca Pandas en Python. El proceso automatizado mejora la calidad de los datos mediante la normalización de nombres de columnas, limpieza de espacios en texto, eliminación de duplicados y eliminación de filas vacías. La modularización en funciones puras facilita mantenimiento, pruebas y reutilización. El resultado es un dataset limpio listo para análisis posteriores o modelado.

## Estructura del Proyecto


##Estructura
python_1/
│
├── src/ # Código fuente
│ ├── main.py # Orquestador del pipeline de limpieza
│ ├── cleaning.py # Funciones puras de limpieza de datos
│ ├── file_io.py # Funciones para lectura y escritura de archivos CSV
│
├── data/ # Datos originales y resultados
│ ├── EPM8_Personas.csv # Dataset original
│ ├── EPM8_Personas_clean.csv # Dataset limpio generado
│
├── README.md # Documentación del proyecto
└── .gitignore # Archivos ignorados por Git


## Arquitectura Modular del Pipeline

- **`file_io.py`**  
  Encapsula funciones para leer y escribir archivos CSV, desacoplando la I/O del procesamiento.

- **`cleaning.py`**  
  Contiene funciones puras que reciben y retornan DataFrames, sin efectos secundarios, para limpiar los datos:  
  - Normalización de columnas (minúsculas, sin espacios)  
  - Limpieza de strings (eliminar espacios)  
  - Eliminación de duplicados  
  - Eliminación de filas vacías

- **`main.py`**  
  Orquesta la ejecución del pipeline:  
  - Carga el dataset  
  - Aplica las funciones de limpieza en orden  
  - Guarda el dataset limpio  
  - Muestra estadísticas antes y después para validar resultados

Esta separación clara mejora la mantenibilidad, facilita pruebas unitarias y escalabilidad futura.

## Contexto de la Base de Datos

El dataset **EPM8_Personas.csv** contiene información personal estructurada en 103 columnas con registros de individuos (identificadores, fechas, variables categóricas y numéricas). Los datos provienen de un proyecto o encuesta relacionada con personas, donde se requiere limpieza para eliminar inconsistencias, duplicados y valores nulos antes de análisis estadístico o modelado predictivo.
