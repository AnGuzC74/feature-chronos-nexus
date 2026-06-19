# 📈 Chronos-NEXUS: Suite Analítica y Arquitectura MLOps Industrial

Chronos-NEXUS es una plataforma de grado industrial diseñada para el monitoreo, ingesta concurrente y observabilidad automatizada en el mercado energético. Este proyecto demuestra la implementación de flujos de trabajo avanzados de **MLOps**, **Sistemas Agenciales Autónomos (Tool Calling)** y arquitecturas de resiliencia ante la degradación de modelos (*Concept Drift*).

## 🛠️ Pilares Arquitectónicos del Sistema

El sistema está compuesto por módulos altamente desacoplados que interactúan bajo principios de diseño de software limpio:

1. **Ingesta Concurrente Asíncrona (`engine_asincrono.py`):** Motor de comunicación no bloqueante que utiliza `asyncio.gather` para interactuar con múltiples APIs financieras simultáneamente, aplicando encapsulamiento estricto a través de `@property` getters/setters para blindar los datos contra corrupción en origen.
2. **Observabilidad y Ciclo de Vida MLOps (`pipeline_mlops.py`):** Sistema encargado de evaluar el rendimiento del modelo en producción (`GradientBoostingRegressor`) mediante métricas de error en ventanas deslizantes. Implementa **Shadow Deployments (Despliegues en Sombra)** automatizados ante la detección de *Concept Drift*.
3. **Capa Agencial y Tool Calling (`agente_inteligente.py`):** Integración con LLMs de baja latencia a través de Groq Cloud, donde el modelo de lenguaje actúa como enrutador cognitivo autónomo para invocar funciones matemáticas del pipeline en lugar de alucinar respuestas.
4. **Middleware de Seguridad (`guardrails.py`):** Cortafuegos operativo basado en **Clases Abstractas (ABC)** e implementando el *Patrón Comando (Command Pattern)* para interceptar e invalidar ataques de *Prompt Injection* dirigidos a funciones críticas del sistema.

## 🚀 Estrategia de Despliegue en Producción (Shadow Deployment)

A diferencia de las estrategias de software tradicionales como *Canary* o *Rolling*, Chronos-NEXUS mitiga el riesgo financiero analítico operando en sombra:
* El modelo desactualizado mantiene la experiencia de usuario activa.
* El modelo reentrenado computa predicciones en paralelo sobre datos en tiempo real.
* Un orquestador compara el Error Absoluto Medio (MAE) de ambas versiones y permite una promoción *Zero-Downtime* a producción.

## 📦 Configuración e Instalación Local

1. Clonar el repositorio y acceder a la carpeta:
   ```bash
   git clone https://github.com/AnGuzC74/feature-chronos-nexus
   cd chronos_nexus_system
   ```

2. Configuración del entorno:
   ```bash
   uv venv --python 3.12
   source .venv/bin/activate  # En Linux/Mac
   # o
   .venv\Scripts\activate     # En Windows
   uv pip install -r requirements.txt
   ```

3. Credenciales:
   Crear un archivo `.env` con: `GROQ_API_KEY=tu_api_key_de_groq`

4. Ejecución:
   ```bash
   streamlit run app_web.py
   ```

## 🌐 Simulación Online
Esta aplicación está optimizada para ejecutarse en **Streamlit Community Cloud** de forma gratuita, con un motor de fallback local para el agente inteligente en caso de que no haya una API Key configurada.
