import os
import pandas as pd

RAW_DIR = "mini-dataops-lab/raw/"
PROCESSED_DIR = "mini-dataops-lab/processed/"

def procesar_datos():
    print(" Iniciando procesamiento de datos...")

    # Crear carpeta processed si no existe
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Buscar el archivo CSV más reciente en raw/
    csv_files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]
    if not csv_files:
        print(" No se encontraron archivos CSV en raw/. Ejecuta primero ingesta.py")
        return

    latest_file = max(csv_files, key=lambda x: os.path.getctime(os.path.join(RAW_DIR, x)))
    csv_path = os.path.join(RAW_DIR, latest_file)

    print(f" Archivo detectado: {csv_path}")

    # Leer el CSV
    df = pd.read_csv(csv_path)

    # ====== Transformaciones simples ======
    print("🔧 Limpiando datos...")

    # Quitar duplicados
    df_clean = df.drop_duplicates()

    # Eliminar filas con valores nulos (opcional)
    df_clean = df_clean.dropna(how="all")

    # Mostrar un resumen
    print(f" Filas originales: {len(df)} | Filas limpias: {len(df_clean)}")

    # Guardar como parquet
    parquet_path = os.path.join(PROCESSED_DIR, "artists_processed.parquet")
    df_clean.to_parquet(parquet_path, index=False)

    print(f" Archivo procesado guardado en: {parquet_path}")

    return parquet_path

if __name__ == "__main__":
    procesar_datos()
