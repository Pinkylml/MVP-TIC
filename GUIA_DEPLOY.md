# 🚀 Guía de Despliegue (Production Deployment Guide)

Esta guía detalla los pasos exactos para poner en línea el MVP de predicción de empleabilidad.

**Prioridad**: Intentaremos **Vercel** primero (más rápido, sin esperas de carga). Si falla por tamaño, usaremos **Render** (más robusto con Docker).

---

## 🌩️ Opción A: Vercel (Recomendada)

Vercel es ideal porque no tiene "Cold Starts" lentos como Render en el plan gratuito.

### Requisitos Previos
1. Tener una cuenta en [Vercel.com](https://vercel.com).
2. Tener este proyecto subido a un repositorio Git (GitHub/GitLab/Bitbucket).

### Pasos
1. **Subir código**: Haz push de la carpeta `06_Deployment` a tu repo (o deployar todo el repo y especificar la carpeta raíz).
   
2. **Importar Proyecto en Vercel**:
   - Ve al Dashboard de Vercel → "Add New..." → "Project".
   - Selecciona tu repositorio.
   
3. **Configuración de Root Directory**:
   - En la sección "Root Directory", haz clic en "Edit".
   - Selecciona la carpeta `06_Deployment` (o donde hayas guardado los archivos finales).
   - **IMPORTANTE**: Asegúrate de que `vercel.json` y `requirements.txt` estén en la raíz de despliegue.

4. **Variables de Entorno (Opcional)**:
   - Si tu aplicación las necesita, añádelas aquí (ej. API Keys). Para este MVP básico no son obligatorias.

5. **Deploy**:
   - Dale clic a **Deploy**.

### ⚠️ Posible Error de Tamaño (Size Limit)
XGBoost es pesado. Si ves el error: `Image size size exceeded the limit (250MB)`, entonces Vercel no soportará nuestras librerías.
👉 **Solución**: Pasa a la Opción B (Render).

---

## 🐳 Opción B: Render (Plan de Respaldo)

Si Vercel falla, Render con Docker es la solución segura. Aunque tiene "Cold Starts" (tarda ~30s en despertar si nadie lo usa), soporta cualquier tamaño de librería.

### Pasos
1. **Crear Web Service en Render**:
   - Ve a [Dashboard de Render](https://dashboard.render.com/) → New → Web Service.
   - Conecta tu repositorio Git.

2. **Configuración**:
   - **Root Directory**: `06_Deployment` (o la ruta donde está el `Dockerfile`).
   - **Runtime**: Selecciona **Docker** (Render detectará automáticamente el `Dockerfile`).
   - **Plan**: Free.

3. **Deploy**:
   - Render construirá la imagen (tardará unos minutos la primera vez).
   - Verás el log "Building Docker image...".
   - Cuando termine, te dará una URL tipo `https://tic-mvp.onrender.com`.

### 💡 Tip para Cold Starts
Para evitar que se "duerma" en Render gratuito, puedes usar servicios como [UptimeRobot](https://uptimerobot.com/) para hacerle ping a tu URL cada 5 minutos. Esto lo mantendrá despierto (aunque puede consumir tus horas gratuitas mensuales más rápido).
