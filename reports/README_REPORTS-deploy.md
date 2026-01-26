# 📂 Documentación de Deployment y Evaluación MVP

Esta carpeta contiene los reportes técnicos generados durante la fase de implementación y pruebas del MVP de predicción de inserción laboral.

## 📄 Reportes Disponibles

### 1. [Reporte de Implementación y Solución de Bugs](Reporte_Implementacion_y_Bugs.md)
**Archivo origen**: `walkthrough.md`
**Contenido**:
- Detalles de la arquitectura del MVP (FastAPI + XGBoost AFT).
- **Bugs Críticos Corregidos**:
  - `Scale parameter` incorrecto (corregido de 0.487 a 2.855).
  - Uso de `output_margin=True` para obtener μ (log-time) real.
  - Sincronización frontend/backend (percentiles).
- Guía de uso del MVP interactivo.

### 2. [Reporte de Hallazgos Masivos (Advertencias)](Reporte_Hallazgos_Masivos.md)
**Archivo origen**: `mass_prediction_report.md`
**Contenido**:
- Análisis estadístico de 300+ predicciones.
- **Advertencias de Sesgo**: Identificación de patrones sospechosos en la variable Edad (posible artefacto de muestra pequeña).
- Comparativa inicial de tiempos por carrera.

### 3. [Reporte de Configuración Óptima (< 3 Meses)](Reporte_Configuracion_Optima.md)
**Archivo origen**: `configuracion_optima_report.md`
**Contenido**:
- Resultados de la prueba masiva V2 (500 perfiles, excluyendo Desarrollo de Software).
- Identificación de la **ÚNICA** configuración que logra p50 < 3 meses:
  - Carrera: **REDES Y TELECOMUNICACIONES**.
  - Soft Skills: **Todas en 5 (Excelente)**.
- Hallazgo sobre impacto marginal nulo de Tech Skills en perfiles óptimos.

---

## 🚀 Siguientes Pasos: Deployment

Con la validación del MVP y los reportes generados, estamos listos para el despliegue final.

**Plan de Deployment**:
1. Empaquetar aplicación FastAPI (Docker).
2. Configurar servidor de producción (Gunicorn/Uvicorn).
3. Configurar CI/CD básico (opcional).
4. Despliegue en entorno objetivo (Render/Railway/VM).
