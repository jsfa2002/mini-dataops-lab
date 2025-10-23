# Mini-DataOps-Lab (AWS) - Entrega
Repositorio con los archivos necesarios para el Laboratorio Práctico Clase 6: Implementando un Mini-Pipeline de DataOps (stack AWS).
Contenido:
- infra/
- ingest/
- transform/
- docs/
- overleaf/

***Instrucciones rápidas***
1. Ajusta los nombres de buckets en los scripts para incluir tus iniciales.
2. Si el dataset en Kaggle no es público, sube manualmente los CSV a tu bucket `raw-...`.
3. Usa este README como guía paso a paso. Aquí hay un checklist de evidencias al final.

--- 

## Estructura del repositorio
```
mini-dataops-lab/
├─ infra/
├─ ingest/
│  └─ lambda_function.py
├─ transform/
│  └─ glue_job.py
├─ docs/
│  └─ README_GUIDE.md
└─ overleaf/
   └─ informe.tex
```

## Pasos para la entrega (resumen)
1. Crear buckets S3:
   - raw-music-data-<tus-iniciales>
   - processed-music-data-<tus-iniciales>
2. Subir `Global Music Artists.csv` a `raw/.../artist_data/` (puedes hacerlo con la consola S3).
3. Crear función Lambda con `ingest/lambda_function.py`. Configurar variables de entorno `RAW_BUCKET` y `RAW_PREFIX`.
4. Probar Lambda (Invoke) — verificar en CloudWatch logs.
5. Crear AWS Glue Crawler apuntando a `raw-*` para crear tablas `songs` y `artists` en un Database (p.ej. music_db).
6. Crear Glue Job con `transform/glue_job.py`. Ejecutar y verificar salida en `processed` bucket.
7. Tomar capturas y pega en el Overleaf (archivo `overleaf/informe.tex`).
8. Subir scripts al repo y generar PR si trabajas en equipo.

## Checklist de evidencias (pone esto en tu Overleaf en las secciones indicadas)
- [ ] Screenshot: Buckets S3 mostrando `raw-` y `processed-`.
- [ ] Screenshot: Lambda console con el código y ejecución exitosa.
- [ ] Screenshot: EventBridge rule (o schedule) configurada.
- [ ] Screenshot: Glue Crawler configurado y ejecutado.
- [ ] Screenshot: Glue Job run con status SUCCEEDED y logs en CloudWatch.
- [ ] Link: Repositorio con commits (README + scripts).
- [ ] Archivo Parquet en `processed-music-data-.../processed/`.

---

Si quieres, puedo añadir IaC (CloudFormation) o los scripts `az`/`aws` CLI. 
