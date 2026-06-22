<div align="center">

# 📈 Chronos-NEXUS: Arquitectura de Simulación MLOps

<p align="center">
  <a href="https://feature-chronos-nexus-6fqvw7hltwhufp8umb6fqu.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit" alt="Live Demo">
  </a>
  <img src="https://img.shields.io/badge/Status-Architecture--Demo-blue?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Data-Synthetic--Simulated-orange?style=for-the-badge" alt="Data">
  <img src="https://img.shields.io/badge/Logic-Shadow--Deployment-success?style=for-the-badge" alt="Logic">
</p>

Chronos-NEXUS es un proyecto demostrativo diseñado para ilustrar la convergencia técnica entre **Ingeniería de Software**, **IA Agencial** y **MLOps**. Su objetivo principal es servir como "sandbox" para patrones de diseño aplicados a sistemas de Machine Learning resilientes.

---
</div>

## 🛠️ Enfoque Técnico: Simulación vs. Realidad

Este sistema no es una herramienta de trading real ni procesa datos financieros auténticos. Es una **simulación técnica** que implementa los siguientes componentes:

### 1. 🔄 Ciclo de Vida MLOps (Shadow Deployment)
Implementado en `pipeline_mlops.py`:
- **Modelo:** `GradientBoostingRegressor` (Scikit-Learn).
- **Datos:** Generación sintética mediante `numpy` y `random` para simular variaciones de mercado.
- **Shadowing:** El sistema entrena un "Shadow Model" cuando detecta degradación del MAE (Mean Absolute Error).
- **Gobernanza:** Permite la promoción manual o automática (Autopiloto) del modelo en sombra a producción.
- **Registro:** Persistencia de metadatos de versiones en archivos JSON (`model_registry/`).

### 2. ⚡ Ingesta Asíncrona (Concurrencia)
Implementado en `engine_asincrono.py`:
- Utiliza `asyncio` y `asyncio.gather` para orquestar "descargas" simultáneas de múltiples fuentes financieras simuladas.
- Manejo de excepciones con lógica de **Fallback controlado** para simular resiliencia ante caídas de red.

### 3. 🤖 Agente de IA Híbrido (Tool Calling)
Implementado en `agente_inteligente.py`:
- **Enrutador:** Intenta conexión con la API de Groq (Llama 3.3).
- **Fallback Local:** Si la API falla o no hay credenciales, activa un motor de respuestas basado en **heurísticas y expresiones regulares** para garantizar la continuidad de la demo.
- **Function Calling:** El agente invoca funciones reales de predicción del sistema para evitar alucinaciones.

### 4. 🛡️ Middleware de Seguridad (Guardrails)
Implementado en `guardrails.py`:
- **Patrón Command:** Encapsula acciones críticas en objetos de comando.
- **Abstracción:** Utiliza clases base abstractas (`ABC`) para definir herramientas seguras.
- **Intercepción:** Bloquea intentos de "Prompt Injection" que buscan forzar reentrenamientos no autorizados.

---

## 🏗️ Stack Tecnológico

- **Core:** Python 3.12 (Tipado estricto)
- **IA/ML:** Scikit-Learn
- **Data:** Pandas, NumPy, Plotly
- **Interface:** Streamlit
- **Async:** Asyncio

---

## 🚀 Instalación para Evaluación Técnica

```bash
# Recomendado: Uso de 'uv' para gestión de dependencias
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt

# Ejecución
streamlit run app_web.py
```

---
<div align="center">
  <sub>Chronos-NEXUS - Demostración de Arquitectura e Ingeniería MLOps.</sub>
</div>
