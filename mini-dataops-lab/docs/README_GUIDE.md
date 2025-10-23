# Guía rápida (detallada)
Este documento explica paso a paso qué hacer y dónde tomar capturas.

1. S3:
   - Crear buckets.
   - Subir `Global Music Artists.csv` a `raw/.../artist_data/`.
   - Captura: consola S3 mostrando archivos.

2. Lambda:
   - Crear función Python.
   - Variables de entorno: RAW_BUCKET, RAW_PREFIX.
   - Añadir permiso IAM mínimo: s3:PutObject al bucket RAW_BUCKET.
   - Probar Invoke; verificar CloudWatch logs.
   - Captura: Lambda code + CloudWatch log.

3. Glue:
   - Crear Crawler apuntando a raw-*.
   - Ejecutar Crawler => crea database `music_db` y tablas.
   - Crear Glue Job con script `transform/glue_job.py`.
   - Ejecutar job y revisar logs en CloudWatch.
   - Captura: Glue Job run (status) y CloudWatch logs.

4. Evidencias:
   - Pegar capturas en Overleaf en las secciones indicadas.
