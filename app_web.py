import streamlit as st
import pandas as pd
import numpy as np
import asyncio
import os
import json
from engine_asincrono import orquestar_ingesta_concurrente
from agente_inteligente import inicializar_agente_con_herramientas
from pipeline_mlops import mlops_manager
from guardrails import guardrail_manager

st.set_page_config(page_title="Chronos-NEXUS Global", layout="wide", page_icon="📈")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; color: #0f172a; }
    div[data-testid="stMetric"] { background-color: #ffffff !important; border: 2px solid #cbd5e1 !important; padding: 20px !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Chronos-NEXUS: Suite Analítica e Infraestructura MLOps")
st.markdown("### 🇻🇪 Control y Observabilidad del Mercado Energético - Grado Industrial")

if 'datos_mercado' not in st.session_state:
    st.session_state.datos_mercado = np.random.uniform(60, 80, (20, 2))
if 'logs_seguridad' not in st.session_state:
    st.session_state.logs_seguridad = []

col_izq, col_der = st.columns([1, 1])

with col_izq:
    st.header("⚡ Ingesta Asíncrona (Concurrencia)")
    if st.button("🚀 Disparar Ingesta Paralela (Asyncio)", use_container_width=True):
        with st.spinner("Abriendo sockets concurrentes..."):
            resultados = asyncio.run(orquestar_ingesta_concurrente())
            for res in resultados:
                st.info(f"📍 {res['fuente']} | Crudo Base: ${res['precio']:.2f}")

with col_der:
    st.header("🤖 Interfaz Cognitiva Agencial")
    pregunta = st.text_input("Hazle una consulta analítica al Agente (o intenta hackearlo pidiendo reentrenar):")
    if pregunta:
        if "reentrenar" in pregunta.lower() or "forzar" in pregunta.lower():
            bloqueo = guardrail_manager.verificar_y_ejecutar("forzar_reentrenamiento_sistema")
            st.error(bloqueo)
            st.session_state.logs_seguridad.append(f"🚨 Intento de Prompt Injection detectado para la acción 'reentrenar'")
        else:
            with st.spinner("El agente evalúa herramientas..."):
                respuesta_agente = inicializar_agente_con_herramientas(pregunta)
                st.success(respuesta_agente)

st.markdown("---")
st.header("⚙️ Observabilidad MLOps: Shadow Deployment & Model Drift")

col_m1, col_m2 = st.columns([2, 1])

with col_m1:
    precio_real_mercado = st.slider("Simular Variación del Precio Real de Mercado ($ USD):", min_value=50.0, max_value=95.0, value=78.5)

    if st.button("⚡ Ejecutar Validación de Salud del Modelo", use_container_width=True):
        res_mlops = mlops_manager.simular_evaluacion_concept_drift(st.session_state.datos_mercado, precio_real_mercado)
        st.metric(label="Estado del Pipeline", value=res_mlops["status"])

        if res_mlops["drift_detectado"]:
            st.warning("🔄 Shadow Model Desplegado: El nuevo modelo está computando predicciones en paralelo para mitigar el riesgo.")

        if mlops_manager.modelo_sombra:
            df_errores = pd.DataFrame({
                "Error Prod (MAE)": mlops_manager.historial_errores["produccion"],
                "Error Sombra (MAE)": mlops_manager.historial_errores["sombra"]
            }).dropna()
            st.line_chart(df_errores)

            if st.button("🚀 Promover Modelo en Sombra a Producción (Zero-Downtime)", use_container_width=True):
                if mlops_manager.promover_sombra_a_produccion():
                    st.success("🎯 ¡Modelo en Sombra promovido con éxito! Pesos actualizados en producción sin caída del servicio.")

with col_m2:
    st.subheader("📁 Model Registry (Metadatos)")
    if os.path.exists("model_registry"):
        archivos = os.listdir("model_registry")
        for arc in archivos[-3:]:
            with open(f"model_registry/{arc}", "r") as f:
                meta = json.load(f)
                st.caption(f"📦 Versión: {meta['version']} | {meta['tipo_despliegue']}")

    if st.session_state.logs_seguridad:
        st.subheader("🛡️ Logs del Middleware de Seguridad")
        for log in st.session_state.logs_seguridad[-2:]:
            st.code(log, language="text")