# 🧹 Proyecto Fase 1 - Limpieza básica de dataset con Pandas

## 📄 Descripción
Este proyecto implementa un **pipeline modular** para la limpieza básica de un dataset personal utilizando Pandas en Python.  
Se separaron responsabilidades para mantener el código **modular, mantenible y escalable**, aplicando funciones puras sobre los datos y encapsulando la lectura/escritura de archivos.

## 🗂 Contexto del Dataset
El dataset **EPM8_Personas.csv** contiene información de población que se fue y retornó a Colombia, con registros estructurados en 103 columnas, incluyendo identificadores, fechas y variables categóricas y numéricas.  
El objetivo es limpiar los datos antes de cualquier análisis o modelado posterior.

## 🛠 Limpieza aplicada
El pipeline realiza las siguientes transformaciones:

- Normalización de nombres de columnas (minúsculas, sin espacios)  
- Eliminación de espacios en strings  
- Eliminación de filas duplicadas  
- Eliminación de filas vacías  

## 🚀 Arquitectura Modular del Pipeline

### 1️⃣ `file_io.py`
Encapsula la lectura y escritura de archivos CSV, separando la I/O de la lógica de limpieza.

### 2️⃣ `cleaning.py`
Contiene funciones puras que reciben y retornan DataFrames, aplicando transformaciones sobre los datos:

- Normalización de columnas  
- Limpieza de strings  
- Eliminación de duplicados  
- Eliminación de filas vacías  

### 3️⃣ `main.py`
Orquesta el pipeline:

- Carga el dataset  
- Ejecuta las funciones de limpieza en orden  
- Guarda el dataset limpio  
- Muestra estadísticas antes y después de la limpieza  

Esta separación permite **fácil mantenimiento, pruebas unitarias y escalabilidad**.

## 📂 Estructura del Proyecto
# Estructura del proyecto python_1

1. **src/** – Código fuente
   1.1. `main.py` – Orquestador del pipeline de limpieza  
   1.2. `cleaning.py` – Funciones puras de limpieza de datos  
   1.3. `file_io.py` – Funciones para lectura y escritura de CSV  

2. **data/** – Datos originales y resultados  
   2.1. `EPM8_Personas.csv` – Dataset original  
   2.2. `EPM8_Personas_clean.csv` – Dataset limpio generado  

3. **README.md** – Documentación del proyecto  

4. **.gitignore** – Archivos que Git debe ignorar (temporales, pesados o generados automáticamente)



## 📊 Resumen Ejecutivo
El proyecto automatiza la limpieza de un dataset personal, mejorando la **calidad de los datos** y garantizando un flujo reproducible. La modularización en funciones puras y el registro de pasos mediante decoradores hacen que el código sea **claro, seguro y escalable**.  
El dataset final está listo para análisis estadístico o modelado predictivo.

## ⚡ Cómo usar el proyecto

1. Clonar o descargar el repositorio.  
2. Ejecutar el archivo principal `main.py` dentro de la carpeta `src`:

```bash
python main.py
