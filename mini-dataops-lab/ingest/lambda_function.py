import os
from datetime import datetime
import shutil
import os
LOCAL_SOURCE = os.path.join(os.path.dirname(__file__), 'data', 'worldwide_music_artists.csv')

RAW_DIR = "mini-dataops-lab/raw/"

def lambda_handler():
    print("Simulando ingesta de Kaggle CSV...")

    if not os.path.exists(RAW_DIR):
        os.makedirs(RAW_DIR)

    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    dest_path = os.path.join(RAW_DIR, f"worldwide_music_artists_{ts}.csv")

    shutil.copy(LOCAL_SOURCE, dest_path)
    print(f"Archivo copiado a {dest_path}")
    return {"status": "uploaded", "path": dest_path}

if __name__ == "__main__":
    lambda_handler()
