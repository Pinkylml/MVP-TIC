# 🎯 Informe de Configuraciones de Inserción Rápida (< 3 meses)

**Fecha**: 2026-01-26
**Objetivo**: Identificar configuraciones óptimas de inserción laboral (< 4 meses) excluyendo explícitamente *Desarrollo de Software*.

---

## ⏱️ Análisis por Rangos de Tiempo

### 🟢 Rango 0 - 1 Mes
**Resultados**: **0 perfiles**.
El modelo no predice inserción inmediata para ninguna configuración. El tiempo mínimo absoluto es **2.62 meses**.

### 🟡 Rango < 3 Meses (La "Zona de Oro")
Solo **1 carrera** logra entrar aquí:
- **REDES Y TELECOMUNICACIONES** (30 perfiles)
  - **Requisito Crítico**: Soft Skills **EXCELENTES (5/5)**
  - **Edad**: 28-30 años

### 🟠 Rango < 4 Meses (Zona Competitiva)
Se suman dos carreras más, pero la exigencia de perfil se mantiene alta:

| Carrera | Cantidad | Condición Obligatoria |
|---------|----------|-----------------------|
| 1. REDES Y TELECOMUNICACIONES | 50 | Soft Skills 5/5 |
| 2. COMPUTACIÓN | 30 | Soft Skills 5/5 |
| 3. ADMINISTRACIÓN DE EMPRESAS | 30 | Soft Skills 5/5 |

**Nota**: Ningún perfil con habilidades "Muy Buenas" (4/4) logra entrar en este rango. La excelencia en competencias blandas es el diferenciador clave.

---

## 🏆 Ranking de Velocidad Promedio

| Pos | Carrera | Tiempo Promedio (Meses) | Rango Observado |
|-----|---------|-------------------------|-----------------|
| 1 | **REDES Y TELECOMUNICACIONES** | **3.82** | 2.6 - 5.6 |
| 2 | ADMINISTRACIÓN DE EMPRESAS | 4.41 | 3.1 - 6.6 |
| 3 | COMPUTACIÓN | 4.86 | 3.6 - 7.1 |
| 4 | ECONOMÍA | 5.78 | 4.6 - 7.1 |
| 5 | SOFTWARE | 7.07 | 5.6 - 9.6 |
| 6 | INGENIERÍA CIVIL | 16.64 ⚠️ | 11.7 - 26.3 |
| 7 | INGENIERÍA QUÍMICA | 22.21 🐢 | 18.7 - 25.8 |

---

## 🐢 Análisis de los "Más Lentos" (> 25 meses)

Los peores escenarios de inserción (superando los 2 años) se concentran en:
1. **Carreras**: Ingeniería Civil e Ingeniería Química.
2. **Perfil**: Jóvenes (22 años) con Soft Skills sub-óptimas (4/4 o inferior).
3. **Penalización**: El modelo castiga severamente la falta de experiencia (edad) y brechas en habilidades blandas en estas ingenierías tradicionales.

---

## 📋 La Configuración Ganadora Detallada (p50 = 2.62 meses)

Para alcanzar el **mínimo histórico** (2.62 meses), se requiere esta configuración exacta:

### 1. Carrera
**REDES Y TELECOMUNICACIONES** (Exclusivo).

### 2. Soft Skills (Todas en 5)
| Variable | Nivel |
|----------|-------|
| S1 (Comunicación) | Excelente |
| S2 (Compromiso Ético)| Excelente |
| S3 (Trabajo Equipo) | Excelente |
| S4 (Resp. Social) | Excelente |
| S5 (Gestión Proyectos)| Excelente |
| S6 (Aprendizaje Dig.) | Excelente |
| S7 (Inglés) | Excelente |

### 3. Demografía
- **Edad**: 28-30 años.
- **Género**: Indiferente.

### 4. Habilidades Técnicas
**Impacto Marginal**: En este nivel de optimización, añadir tecnologías específicas (React, Simulación) **no reduce más el tiempo**. La carrera y las soft skills dominan la predicción favorable.

---

## 💡 Conclusión Ejecutiva

1. **Sin Desarrollo de Software**, la opción líder indiscutible es **Redes y Telecomunicaciones**.
2. **La excelencia paga**: Bajar de 5/5 a 4/5 en soft skills tiene un costo de tiempo significativo, sacando a los candidatos del rango < 4 meses.
3. **Brecha Generacional**: Los graduados jóvenes (22-23) enfrentan proyecciones sistemáticamente más lentas, sugiriendo que la experiencia o madurez (proxy de edad) es valorada por el modelo.
