from pathlib import Path
from file_io import read_csv, write_csv
from cleaning import (
    normalize_column_names,
    remove_duplicates,
    drop_empty_rows,
    strip_strings,
)

def main() -> None:
    """
    Pipeline de limpieza para el dataset personal.
    Pasos:
    1. Cargar CSV
    2. Mostrar estadísticas iniciales
    3. Normalizar nombres de columnas
    4. Limpiar espacios en strings
    5. Eliminar duplicados
    6. Eliminar filas vacías
    7. Guardar CSV limpio
    8. Mostrar estadísticas finales
    """
    base_path = Path(__file__).resolve().parent.parent

    input_path = base_path / "data" / "EPM8_Personas.csv"
    output_path = base_path / "data" / "EPM8_Personas_clean.csv"

    # 1️⃣ Leer dataset
    df = read_csv(input_path)

    # 2️⃣ Mostrar estadísticas iniciales
    print("=== Estadísticas iniciales ===")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    print(f"Duplicados: {df.duplicated().sum()}")
    print(f"Valores nulos:\n{df.isnull().sum()}\n")

    # 3️⃣ Pipeline de limpieza
    df = normalize_column_names(df)
    df = strip_strings(df)
    df = remove_duplicates(df)
    df = drop_empty_rows(df)

    # 4️⃣ Guardar CSV limpio
    write_csv(df, output_path)

    # 5️⃣ Mostrar estadísticas finales
    print("\n=== Estadísticas finales ===")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    print(f"Duplicados: {df.duplicated().sum()}")
    print(f"Valores nulos:\n{df.isnull().sum()}\n")

    print("Cleaning finished. Primeras 5 filas:")
    print(df.head())

if __name__ == "__main__":
    main()
