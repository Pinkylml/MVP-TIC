# 📂 Documentación de Deployment y Evaluación MVP

Esta carpeta contiene los reportes técnicos generados durante la fase de implementación y pruebas del MVP.

## 📄 Reportes Disponibles

### 1. [Reporte de Implementación y Solución de Bugs](Reporte_Implementacion_y_Bugs.md)
**Archivo origen**: `walkthrough.md`
- Detalles de la arquitectura MVP (FastAPI + XGBoost AFT).
- Bugs críticos corregidos (Scale parameter, output margin).

### 2. [Reporte de Hallazgos Masivos (Advertencias)](Reporte_Hallazgos_Masivos.md)
**Archivo origen**: `mass_prediction_report.md`
- Análisis inicial de ~335 perfiles.
- Advertencias sobre sesgos en variable edad.

### 3. [Reporte de Configuración Óptima (< 3 Meses)](Reporte_Configuracion_Optima.md)
**Archivo origen**: `configuracion_optima_report.md`
- **Resultados Finales**: Excluyendo "Desarrollo de Software".
- Análisis por rangos (0-1m, <3m, <4m).
- Identificación de **Redes y Telecomunicaciones** como la opción más rápida.

### 4. [Informe Final de Despliegue](INFORME_FINAL_DEPLOY.md)
**Archivo origen**: `INFORME_FINAL_DEPLOY.md`
- URL de Producción: **https://mvp-tic.onrender.com**
- Detalles de la plataforma (Render Free Tier) y notas sobre Cold Starts.

---

## 🚀 Deployment

Los reportes validan el modelo para su despliegue final.
Próximos pasos: Disfrutar del MVP en producción.
