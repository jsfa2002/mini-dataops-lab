import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lectura desde Glue Catalog (suponiendo Crawler ya creó tablas 'songs' y 'artists')
songs_df = glueContext.create_dynamic_frame.from_catalog(
    database="music_db", table_name="songs"
).toDF()

artists_df = glueContext.create_dynamic_frame.from_catalog(
    database="music_db", table_name="artists"
).toDF()

joined = songs_df.join(artists_df, F.lower(songs_df.artist_name) == F.lower(artists_df.artist_name), how="left")

joined = joined.withColumn("popularity",
                           F.when((F.col("popularity").isNull()) | (F.col("popularity") < 0) | (F.col("popularity") > 100),
                                  F.lit(None)).otherwise(F.col("popularity")))

joined = joined.withColumn("energy_ratio",
                           F.when(F.col("duration_ms").isNull() | (F.col("duration_ms") == 0), None)
                           .otherwise(F.col("energy") / F.col("duration_ms")))

out = joined.select("track_id", "track_name", "artist_name", "popularity", "energy", "duration_ms", "energy_ratio")

processed_path = "s3://processed-music-data-JSA/processed/"
out.write.mode("overwrite").parquet(processed_path)

job.commit()
