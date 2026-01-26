# 🧪 Informe de Pruebas Pre-Deploy y Recursos

**Estado**: ✅ CÓDIGO VALIDADO
La aplicación inicia correctamente con la nueva estructura de carpetas.

## 📊 Estimación de Recursos

### Memoria RAM (Runtime)
El contenedor necesitará aproximadamente **350MB - 500MB** de RAM para funcionar.
- **Carga Base (Python + FastAPI)**: ~60MB
- **Librerías (XGBoost, Pandas, Scipy)**: ~250MB (al importar)
- **Modelo en memoria**: ~20MB
- **Margen de seguridad**: ~100MB

**Veredicto**:
- **Render Free Tier (512MB)**: ✅ Debería funcionar, pero está cerca del límite. Si se cierra sola, es por memoria (`OOM Killed`).
- **Vercel Functions (1024MB)**: ✅ Sin problemas de RAM, pero riesgo de límite de tamaño de paquete (250MB disco).

### Espacio en Disco (Build)
La imagen Docker completa pesará entre **800MB y 1.2GB**.
- **Base (Python Slim)**: ~150MB
- **Dependencias (site-packages)**: ~600MB (XGBoost y Numpy/Scipy son pesados).
- **Código y Modelo**: ~20MB

---

## 🧹 Limpieza de Requirements
El `requirements.txt` actual es el mínimo necesario para las funciones implementadas:
- `fastapi`, `uvicorn`: Servidor web.
- `xgboost`: Motor del modelo.
- `pandas`: Procesamiento de datos (obligatorio por `engine.py`).
- `scipy`, `numpy`: Cálculos matemáticos (curva AFT normal).

**No se pueden eliminar más paquetes** sin reescribir `engine.py` para usar matemáticas puras (lo cual sería riesgoso ahora).

## ✅ Conclusión
El Docker está **listo para construir**. 
Si tienes poco espacio local, **NO ejecutes `docker build` en tu máquina**. Deja que la nube (Render) haga el build por ti.
