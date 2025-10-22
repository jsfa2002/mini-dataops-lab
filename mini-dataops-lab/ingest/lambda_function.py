import os
import boto3
import requests
from datetime import datetime

S3_BUCKET = os.environ.get("RAW_BUCKET")  # ej: raw-music-data-JSA
S3_KEY_PREFIX = os.environ.get("RAW_PREFIX", "song_data/")
CSV_URL = "https://raw.githubusercontent.com/selassid/spotify-datasets/main/SpotifyAudioFeaturesApril2019.csv"
# Si Kaggle requiere auth, sube manualmente a S3 y omite la descarga.

s3 = boto3.client("s3")

def lambda_handler(event, context):
    resp = requests.get(CSV_URL, timeout=30)
    resp.raise_for_status()
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    key = f"{S3_KEY_PREFIX}SpotifyAudioFeaturesApril2019_{ts}.csv"
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=resp.content)
    return {"status": "uploaded", "bucket": S3_BUCKET, "key": key}
