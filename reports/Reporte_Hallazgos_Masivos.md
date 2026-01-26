# Informe de Hallazgos - Predicciones Masivas MVP

**Fecha**: 2026-01-26  
**Total Predicciones**: 335 perfiles exitosos (de 350 intentadas)

---

## ⚠️ ADVERTENCIAS CRÍTICAS

### 1. Patrón Sospechoso en Variable Edad

**Hallazgo Observado**:
- Edad 28: p50 = 6.77 meses ✓ MEJOR
- Edad 25: p50 = 8.28 meses
- Edad 22: p50 = 8.37 meses ✗ PEOR

**🚨 PROBLEMA IDENTIFICADO**:
Este patrón NO es necesariamente válido. Puede ser un **artefacto** de:

1. **Tamaño de muestra insuficiente** en entrenamiento
2. **Sesgo de selección** en datos de julio/diciembre 2025
3. **Overfitting** a características específicas de la muestra
4. **Falta de balanceo** en distribución de edad durante entrenamiento

**Evidencia de Sesgo**:
- Diferencia demasiado marcada entre edad 22 vs 28 (24% más lento)
- Patrón NO monotónico (no sigue tendencia clara)
- Puede reflejar composición específica de cohortes, NO causalidad

### 2. Impacto Marginal de Technical Skills

**Hallazgo Observado**:
Con soft skills = 5/5, las habilidades técnicas tuvieron **impacto casi nulo**:

| Technical Skill | p50 Promedio | Diferencia |
|-----------------|--------------|------------|
| React           | 7.80         | ~0.01      |
| Estructura Datos| 7.80         | ~0.01      |
| Top3 Combined   | 7.90         | ~0.10      |

**Interpretación**:
- NO significa que skills técnicas no importan
- Significa que con soft skills perfectos (5/5), el efecto marginal es pequeño
- Posible **multicolinealidad** entre soft/technical skills
- Requiere investigación con variación en soft skills

---

## 📊 Resultados por Carrera (Más Confiables)

### Top 3 Inserción Rápida
1. **DESARROLLO DE SOFTWARE**: 2.6 - 3.6 meses (μ = 1.07)
2. **REDES Y TELECOMUNICACIONES**: 2.6 - 3.6 meses (μ = 1.07)
3. **ADMINISTRACIÓN DE EMPRESAS**: 3.1 - 4.1 meses (μ = 1.24)

### Top 3 Inserción Lenta
1. **INGENIERÍA QUÍMICA**: 18.7 - 24.8 meses (μ = 3.09) ⚠️
2. **INGENIERÍA CIVIL**: 11.7 - 15.2 meses (μ = 2.60)
3. **SOFTWARE**: 5.6 - 6.6 meses (μ = 1.80)

**Nota**: Estos resultados son más confiables porque:
- Mayor cantidad de observaciones por carrera en train
- Patrones consistentes con literatura sobre empleabilidad STEM
- Menor probabilidad de overfitting

---

## ⚙️ Estadísticas Globales

- **μ promedio**: 1.74 (rango: 0.85 - 3.19)
- **p50 promedio**: 7.81 meses
- **p50 mejor caso**: 2.62 meses
- **p50 peor caso**: 24.76 meses
- **Factor variación**: 9.5× entre mejor/peor caso

---

## 🔍 Hallazgos sobre Género

- **Femenino**: p50 = 7.63 meses
- **Masculino**: p50 = 7.99 meses
- **Diferencia**: -0.36 meses (4.7% más rápido F vs M)

**⚠️ Advertencia**: 
- Diferencia marginal, podría ser ruido estadístico
- Requiere test de significancia
- No implica causalidad

---

## 🚨 LIMITACIONES CRÍTICAS DEL ESTUDIO

### 1. Sesgo de Muestra
- **Solo perfiles con soft skills = 5/5**
- No exploramos variación S1-S7 (1-5)
- Resultados NO generalizables a toda población

### 2. Tamaño de Muestra
- Solo 50 perfiles base × 7 variaciones técnicas
- Muestra pequeña para detectar efectos marginales
- Posible overfitting a características específicas

### 3. Censura en Datos Originales
- Target variable: 0-6 meses observados + censura
- Predicciones >6 meses pueden ser extrapolaciones
- Incertidumbre aumenta con tiempos largos

### 4. Colinealidad
- Carreras correlacionan con skills técnicas específicas
- Dificulta atribuir efectos causales
- Ejemplo: SOFTWARE → estructura de datos

---

## 📌 RECOMENDACIONES URGENTES

### 1. Investigar Variable Edad
```python
# ACCIÓN REQUERIDA
- Revisar distribución de edad en datos de entrenamiento
- Verificar si hay transformación/balanceo de edad
- Comparar distribución train vs predicciones
- Considerar reentrenar con edad balanceada
```

### 2. Validar con Datos Reales
- Comparar predicciones con seguimiento 2026 (cuando disponible)
- Identificar casos donde modelo falla
- Refinar features basándose en errores

### 3. Ampliar Espacio de Exploración
- Variar soft skills (grid 1-5 en S1-S7)
- Probar perfiles mixtos (alto técnico + bajo soft, viceversa)
- Aumentar muestra a 1000+ combinaciones

### 4. Análisis Estadístico Formal
- Tests de significancia para diferencias observadas
- Intervalos de confianza para predicciones
- Análisis de sensibilidad

---

## 💡 CONCLUSIONES PRELIMINARES

### LO QUE SABEMOS CON CONFIANZA:
✅ DESARROLLO DE SOFTWARE tiene inserción más rápida  
✅ INGENIERÍA QUÍMICA tiene inserción más lenta  
✅ Existe alta variabilidad entre carreras (factor 9.5×)  

### LO QUE ES INCIERTO:
❓ Efecto real de edad (posible artefacto de muestra)  
❓ Impacto marginal de technical skills (necesita más exploración)  
❓ Diferencia género (marginal, necesita test estadístico)  

### LO QUE REQUIERE INVESTIGACIÓN:
🔬 Distribución y procesamiento de Edad en entrenamiento  
🔬 Tamaño de muestra por combinación edad-carrera  
🔬 Validación externa con datos 2026  
🔬 Exploración completa del espacio soft skills (1-5)  

---

## 📁 Archivos Generados

- `mass_predictions_results.csv` (335 filas)
- `analysis_careers_boxplot.png`
- `analysis_mu_vs_p50.png`
- `analysis_softskills_heatmap.png`
- `analysis_mu_distribution.png`

---

**NOTA FINAL**: Este informe presenta hallazgos DESCRIPTIVOS. Se requiere análisis estadístico formal antes de hacer afirmaciones CAUSALES sobre efectos de variables.
