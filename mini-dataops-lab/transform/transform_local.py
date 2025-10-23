# transform_local.py
import pandas as pd
import os

RAW_DIR = "mini-dataops-lab/raw/"
PROCESSED_DIR = "mini-dataops-lab/processed/"

# Crear carpeta processed si no existe
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Encontrar CSV de canciones
song_csv = os.path.join(RAW_DIR, "song_data", "SpotifyAudioFeaturesApril2019.csv")
artist_csv = os.path.join(RAW_DIR, "worldwide_music_artists.csv")  # ingesta ya crea timestamped file

# Leer datos
songs_df = pd.read_csv(song_csv)
# Para el artista tomamos el último CSV de ingesta
artist_files = [f for f in os.listdir(RAW_DIR) if f.startswith("worldwide_music_artists")]
latest_artist = sorted(artist_files)[-1]
artists_df = pd.read_csv(os.path.join(RAW_DIR, latest_artist))

# Normalizar artist_name
songs_df['artist_name'] = songs_df['artist_name'].str.lower()
artists_df['artist_name'] = artists_df['artist_name'].str.lower()

# Unir tablas
merged_df = pd.merge(songs_df, artists_df, on='artist_name', how='left')

# Limpiar popularity
merged_df['popularity'] = merged_df['popularity'].clip(lower=0, upper=100)

# Crear energy_ratio
merged_df['energy_ratio'] = merged_df['energy'] / merged_df['duration_ms'].replace(0, pd.NA)

# Guardar Parquet
output_file = os.path.join(PROCESSED_DIR, "processed_music.parquet")
merged_df.to_parquet(output_file, engine='fastparquet', index=False)
print(f"Archivo procesado guardado en {output_file}")
