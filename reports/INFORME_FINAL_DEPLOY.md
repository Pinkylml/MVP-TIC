# 🚀 Informe Final de Despliegue (MVP Versión RSF)

**Fecha**: 2026-01-28
**Estado**: ✅ EN PRODUCCIÓN (Actualizado)

## 🌐 Acceso al Sistema

El MVP ha sido actualizado al modelo **Random Survival Forest (RSF)** y está accesible en:

👉 **URL**: **[https://mvp-tic.onrender.com](https://mvp-tic.onrender.com)**

---

## 🏗️ Detalles Técnicos (Nueva Versión)

- **Plataforma**: Render (Dockerizado)
- **Modelo**: Random Survival Forest (C-index: 0.6983)
- **Tecnologías**: Python 3.11 + FastAPI + Scikit-Survival
- **Cambios Clave**: 
    - Pipeline de escalamiento (`StandardScaler`) integrado.
    - Mapeo de carreras estandarizado.
    - Curvas de supervivencia directas (no paramétricas).

### ⚠️ Nota sobre Resultados
Debido a que el modelo fue entrenado con un seguimiento limitado (6 meses), el sistema predice hasta ese horizonte temporal. Si un perfil tiene una inserción lenta, los indicadores mostrarán ">6 meses" o se limitarán a ese valor por la alta censura del estudio original.

---

## 📦 Entregables en Carpeta `06_Deployment/`

1. **Modelos**: Carpeta `app/models/` (model.joblib, scaler.joblib, metadata.json).
2. **Datos**: Carpeta `app/data/` (mapeo_carrera.json).
3. **Reportes**: Carpeta `reports/` (GUIA_DEPLOY.md, INFORME_VALIDACION_DOCKER.md).

---

## 🔮 Siguientes Pasos
El sistema es estable. Para futuras versiones, se recomienda ampliar el horizonte temporal de los datos de entrenamiento para predecir inserciones más allá de los 6 meses.
