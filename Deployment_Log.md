# 🚀 Bitácora de Despliegue (Deployment Log)

Este documento registra paso a paso el proceso de empaquetado y despliegue del modelo predictivo MVP.

## 📅 Historial de Acciones

### [2026-01-26] Cambio de Estrategia: Vercel (Serverless)
- **Motivo**: Requerimiento de ambiente gratuito sin gestión de servidores.
- **Acción**: Abandonar Docker en favor de Vercel Python Runtime.
- **Configuración**: Creado `vercel.json` para enrutamiento.

---

## 🛠️ Pasos Realizados

1. [x] **Consolidación de Reportes**: Archivos de análisis movidos a `reports/`.
2. [x] **Estructura de Carpetas**: App lista en `app/`.
3. [x] **Dependencias**: `requirements.txt` optimizado.
4. [x] **Configuración Vercel**: Generado `vercel.json`.
5. [ ] **Verificación**: Validar estructura para Vercel CLI.

---

## 📦 Estructura del Despliegue (Vercel)

```text
06_Deployment/
├── app/                # Código fuente
│   ├── main.py
│   └── ...
├── vercel.json         # Configuración de rutas
├── requirements.txt    # Dependencias (se instalan automágicamente)
└── reports/            
```

⚠️ **Nota sobre Límites**: El tamaño de XGBoost puede ser un reto en el plan gratuito (250MB límite). Si falla, la alternativa gratuita con Docker es **Render**.
