<div align="center">

# 📈 Chronos-NEXUS: 

<p align="center">
  <a href="https://feature-chronos-nexus-6fqvw7hltwhufp8umb6fqu.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit" alt="Live Demo">
  </a>
  <img src="https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Architecture-MLOps--Senior-blue?style=for-the-badge" alt="Architecture">
  <img src="https://img.shields.io/badge/Resilience-99.9%25-orange?style=for-the-badge" alt="Resilience">
</p>

Chronos-NEXUS es una suite analítica de grado industrial diseñada para demostrar la convergencia entre la Ingeniería de Software de alto nivel, IA Agencial y MLOps (Operaciones de Machine Learning).

Aquí tienes un resumen detallado de su propósito y funcionamiento:

# # 1. ¿Qué es Chronos-NEXUS?
Es una plataforma de observabilidad y control para el mercado energético (específicamente crudo). No es solo un panel de visualización, sino una infraestructura robusta que garantiza que los modelos de Inteligencia Artificial sigan siendo precisos y seguros incluso cuando las condiciones del mercado cambian drásticamente.

# # 2. ¿Para qué sirve?
El sistema tiene tres objetivos principales:

Garantizar la Continuidad Analítica: Evita que un modelo de predicción obsoleto tome decisiones erróneas mediante la detección automática de degradación de datos (Concept Drift).
Demostrar Resiliencia Industrial: Utiliza técnicas de programación asíncrona y motores de "fallback" para asegurar que la plataforma nunca deje de funcionar, incluso si las APIs externas o las llaves de IA fallan.
Seguridad Operativa: Implementa capas de protección (Guardrails) para evitar que usuarios malintencionados o errores humanos disparen procesos críticos sin autorización.
3. ¿Qué simula exactamente?
El programa orquesta un ecosistema completo de producción de datos:

Ingesta Concurrente (Engine Asíncrono): Simula la conexión simultánea a múltiples fuentes financieras (como Bloomberg o Reuters) para obtener precios de crudo en tiempo real de manera eficiente y no bloqueante.
Ciclo de Vida MLOps (Shadow Deployment):
Entrena un modelo (Gradient Boosting) para predecir precios.
Monitorea el error del modelo. Si el mercado cambia y el error sube demasiado, el sistema automáticamente entrena un "Modelo en Sombra" (Shadow Model).
Este nuevo modelo compite en silencio con el de producción. Tú puedes decidir si lo promueves manualmente o dejas que el "Modo Autopiloto" lo haga por ti si demuestra ser mejor.
Interfaz Cognitiva (Agente IA): Simula a un Economista Senior con el que puedes hablar. El agente es inteligente: si le pides un pronóstico, no "alucina" una respuesta, sino que invoca las funciones matemáticas del sistema para darte datos reales. Si no hay conexión a internet, tiene un cerebro local de respaldo para seguir asistiendo.
Defensa de Sistema (Guardrails): Simula un ataque de "Prompt Injection". Si intentas engañar al agente para que "fuerce un reentrenamiento" o rompa el sistema, el Middleware de Seguridad intercepta la orden y la bloquea.
En resumen, Chronos-NEXUS simula el cerebro y el escudo de una empresa energética moderna, donde la IA y los modelos matemáticos deben trabajar de forma autónoma pero bajo una estricta supervisión de ingeniería.

---
</div>

## 🎯 ¿Por qué Chronos-NEXUS?

En el mercado energético, un minuto de inactividad o una predicción errónea debido a la degradación de datos (*Concept Drift*) puede costar millones. **Chronos-NEXUS** no es solo un dashboard; es una infraestructura crítica que automatiza la supervivencia de los modelos de IA en producción.

### 🧩 El Problema vs. La Solución Chronos

| El Problema Común ❌ | La Solución Chronos-NEXUS ✅ |
| :--- | :--- |
| El modelo se vuelve obsoleto y nadie se da cuenta. | **Monitoreo de Drift Activo:** Reentrenamiento automático al detectar pérdida de precisión. |
| El despliegue de un nuevo modelo interrumpe el servicio. | **Shadow Deployment:** Validación en paralelo con promoción *Zero-Downtime*. |
| Las APIs externas fallan y la aplicación muere. | **Hybrid Resilience:** Agente con motor de inferencia local de fallback. |
| Vulnerabilidad a inyecciones de prompts maliciosos. | **Middleware de Seguridad:** Guardrails basados en patrones de diseño industriales. |

---

## 🏗️ Arquitectura de Ingeniería (Deep Dive)

### 1. ⚡ Ingesta Asíncrona & Integridad de Datos
Utilizamos `asyncio` para orquestar la ingesta concurrente desde múltiples proveedores financieros. A diferencia de las implementaciones básicas, implementamos **validación en la capa de datos** mediante descriptores y propiedades para garantizar que ningún dato corrupto contamine el pipeline analítico.

### 2. 🔄 MLOps: El Ciclo de Vida Completo
Implementamos un flujo de trabajo de **Despliegue en Sombra (Shadow Deployment)**:
- **Observabilidad:** Seguimiento en tiempo real del MAE (Mean Absolute Error).
- **Gobernanza vs. Autopiloto:** El sistema permite elegir entre promoción manual supervisada o un **Modo Autopiloto (CI/CD Automático)** que promueve el mejor modelo basado en rendimiento.
- **Versioning:** Un Model Registry simplificado para la trazabilidad de experimentos y auditoría de versiones.
- **Promoción Zero-Downtime:** Capacidad de intercambiar modelos en caliente sin afectar la disponibilidad del servicio.

> **Nota de Telemetría:** Al ser un sistema basado en eventos de mercado real, los gráficos de rendimiento comienzan vacíos. Es necesario interactuar con el simulador ("Ejecutar Validación de Salud") para generar la telemetría dinámica necesaria.

### 3. 🤖 Agente de IA de Grado Industrial
No confiamos ciegamente en las APIs externas. Nuestro agente utiliza un **Enrutador Cognitivo** que:
- Invoca funciones de ML propias para evitar alucinaciones.
- Activa un motor de fallback local ante errores de cuota o caídas de red, garantizando una disponibilidad del 99.9%.

---

## 🛠️ Stack Tecnológico

- **Core:** Python 3.12
- **IA/ML:** Scikit-Learn (Gradient Boosting), Groq Cloud (Llama 3.3 70B)
- **Data:** Pandas, NumPy, Plotly
- **Ops:** Streamlit, Asyncio, Pydantic, Dotenv
- **Arquitectura:** Patrones de Diseño (Command, Singleton, ABCs)

---

## 🚀 Instalación y Despliegue

### Entorno Profesional
```bash
# Instalación ultra-rápida con uv
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -r requirements.txt
```

### Ejecución
```bash
streamlit run app_web.py
```

---
<div align="center">
  <sub>Chronos-NEXUS Global - Elevando el Machine Learning a la categoría de Ingeniería.</sub>
</div>
