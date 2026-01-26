# Walkthrough: MVP de Predicción de Inserción Laboral

## Resumen
Se implementó un MVP web que permite predecir el tiempo de inserción laboral de graduados STEM usando el modelo XGBoost-AFT entrenado.

## 🔧 Problemas Críticos Resueltos

### 1. Bug del Scale Parameter
**Problema**: El modelo estaba prediciendo tiempos absurdos (165+ meses) debido a un scale incorrecto.
- ❌ **Valor incorrecto**: `SCALE = 0.487`
- ✅ **Valor correcto**: `SCALE = 2.8551127078884506`

**Archivo corregido**: [`core/loader.py`](file:///home/desarrollo03/Documentos/UNIVERSIDAD/TIC/TIC-workspacev4-definitive/06_evaluating/mvp_app/core/loader.py#L11)

### 2. Uso Incorrecto de predict()
**Problema Identificado** (gracias al colega de entrenamiento):
- `booster.predict()` devuelve **tiempo transformado** (no log-time)
- `booster.predict(output_margin=True)` devuelve **μ (log-time real)**

**Solución Aplicada**: [`core/engine.py:54`](file:///home/desarrollo03/Documentos/UNIVERSIDAD/TIC/TIC-workspacev4-definitive/06_evaluating/mvp_app/core/engine.py#L54)
```python
mu = self._get_booster().predict(dmatrix, output_margin=True)[0]
```

### 3. Frontend-Backend Format Mismatch
**Problema**: JavaScript esperaba `percentiles.p50_median` pero backend retornaba `percentiles.p50`
**Solución**: Actualizado JavaScript (línea 218) para coincidir con formato del backend.

### 4. Scale Hardcodeado en Frontend
**Archivo**: `templates/index.html:245`
**Cambio**: Actualizado display de 0.487 → 2.8551

## Entendimiento del Target Variable

**Contexto importante** (de `02_Data_Understanding/Reporte_Final_Data_Understanding-part1.md`):
- La encuesta se realiza **6 meses después** de terminar las materias
- La escala de tiempo está **INVERTIDA**:
  - `T_Lower=0, T_Upper=1`: Inserción **rápida** (empleo antes de 6 meses) ✅
  - `T_Lower=4, T_Upper=6`: Inserción **tardía** (empleo cerca del límite) ⏱️
  - `T_Lower=6, T_Upper=∞`: **Censura** (sin empleo aún) ❌

## Fórmula AFT Correcta

Del notebook evaluación (línea 482):
```python
z = (np.log(t) - μ) / σ
S(t) = 1 - Φ(z)
```

Donde:
- **μ** = log-tiempo predicho (obtenido con `output_margin=True`)
- **σ** = 2.8551 (scale del modelo)
- **S(t)** = Probabilidad de NO haber conseguido empleo hasta tiempo t

## 🎯 Nueva Funcionalidad: Exploración SHAP

### Top Features Añadidas
Basado en SHAP beeswarm plot (Top 20), se añadieron controles para:

**Habilidades Técnicas** (binarias 0/1):
1. react, revit
2. estructura de datos, estructuras  
3. simulación, simulación de procesos
4. telefonía ip, voz sobre ip
5. finanzas, mercados financieros
6. arquitectura de computadoras
7. optimización, optimización de procesos
8. análisis de datos, análisis de materiales...
9. etl, latex, lte
10. logística, supply chain

**Soft Skills** (escala 1-5):
- Ya existían sliders para S1-S7

### Interpretación SHAP
**Eje SHAP > 0**: Aumenta μ → Aumenta log(T) → **Mayor tiempo hasta empleo** (peor) ⬆️  
**Eje SHAP < 0**: Reduce μ → Reduce log(T) → **Menor tiempo** (mejor) ⬇️

**Efecto Multiplicativo**: 
- SHAP = +0.70 → exp(0.70) ≈ **2.0× más tiempo**
- SHAP = -1.00 → exp(-1.0) ≈ **0.37× el tiempo**

### Implementación
- **Frontend**: Sección expandible `<details>` con checkboxes para cada skill
- **JavaScript**: Recolecta valores (0/1) y los envía con el request
- **Backend**: Los recibe como features adicionales en el input dictionary

## Cambios Realizados

### 1. Estructura del Proyecto
- Creada aplicación FastAPI en `mvp_app/`
- Estructura modular: `api/`, `core/`, `static/`, `templates/`

### 2. Backend (FastAPI)
- **`main.py`**: Servidor FastAPI con endpoint `/predict`
- **`api/schemas.py`**: Validación de entrada + carga automática de career vectors
- **`core/engine.py`**: Motor de predicción con fórmula AFT correcta
- **`core/loader.py`**: ⚠️ **CORREGIDO** - Scale actualizado a 2.8551
- **`core/career_vectors.py`**: Carga los 69 features técnicos por carrera

### 3. Frontend
- **`templates/index.html`**: 
  - Interfaz base con soft skills sliders
  - Nueva sección SHAP expandible con top technical skills
  - JavaScript actualizado para recolectar y enviar technical skills
- **Visualización**: Curva S(t) con Chart.js

### 4. Integración de Career Vectors
- Creado `core/career_vectors.py` para cargar vectores técnicos desde CSV
- `Vectores_Academicos_69d.csv` → `mvp_app/data/`
- Automáticamente carga 69 features técnicas según carrera seleccionada
- Total: 103 features enviadas al modelo (9 base + 69 técnicas + ~24 carreras one-hot)

## Valores Esperados 

Con el scale y output_margin correctos, las predicciones deberían mostrar:
- **μ (log-time)**: Entre -0.7 y 2.0 aproximadamente
- **p50 (mediana)**: 3-5 meses
- **p75**: 4-6 meses
- **p90**: 5-7 meses

## Uso del MVP

1. **Ajustar Soft Skills** (S1-S7): Escala 1-5
2. **Ingresar Demografía**: Edad, Género, Carrera
3. **[NUEVO] Explorar SHAP**: Expandir sección y activar habilidades técnicas top
4. **Predecir**: Observar cómo cambian tiempos con diferentes combinaciones
5. **Interpretar**: μ alto = más tiempo, SHAP features muestran impacto marginal
