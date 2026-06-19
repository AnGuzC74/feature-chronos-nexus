# 📈 Chronos-NEXUS: El Estandar de Oro para MLOps Industrial

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Un modelo en un Jupyter Notebook no es un producto. Chronos-NEXUS es la respuesta a cómo llevar el Machine Learning al mundo real de forma resiliente, segura y escalable."**

---

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

### 1. Ingesta Asíncrona & Integridad de Datos
Utilizamos `asyncio` para orquestar la ingesta concurrente desde múltiples proveedores financieros. A diferencia de las implementaciones básicas, implementamos **validación en la capa de datos** mediante descriptores y propiedades para garantizar que ningún dato corrupto contamine el pipeline analítico.

### 2. MLOps: El Ciclo de Vida Completo
Implementamos un flujo de trabajo de **Despliegue en Sombra (Shadow Deployment)**:
- **Observabilidad:** Seguimiento en tiempo real del MAE (Mean Absolute Error).
- **Versioning:** Un Model Registry simplificado para la trazabilidad de experimentos.
- **Promoción:** Capacidad de intercambiar modelos en caliente sin afectar la disponibilidad.

### 3. Agente de IA de Grado Industrial
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

## 👨‍💻 Sobre el Desarrollador

Este proyecto es una demostración de capacidades avanzadas en **MLOps, Ingeniería de Software e IA**. Mi enfoque es construir sistemas que no solo funcionen, sino que sean robustos ante el caos de los entornos de producción reales.

**¿Buscas un Ingeniero que entienda el puente entre los datos y el negocio?**
¡Hablemos!

---
*Chronos-NEXUS Global - Elevando el Machine Learning a la categoría de Ingeniería.*
