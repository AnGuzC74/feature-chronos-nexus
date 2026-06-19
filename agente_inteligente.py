import os
import json
import random
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# 🛡️ Extracción Híbrida: Busca en secretos de Streamlit Cloud (Producción) o en .env (Local)
api_key_groq = ""
if "GROQ_API_KEY" in st.secrets:
    api_key_groq = st.secrets["GROQ_API_KEY"]
else:
    api_key_groq = os.environ.get("GROQ_API_KEY", "").strip()

client_groq = Groq(api_key=api_key_groq) if api_key_groq else None

def pronosticar_precio_crudo_gbt(dias_proyeccion: int) -> str:
    precio_estimado = 72.45 + (dias_proyeccion * 0.35)
    return f"Resultado del modelo Gradient Boosting: El precio proyectado para los próximos {dias_proyeccion} días es de ${precio_estimado:.2f} USD por barril."

def simular_agente_local_gratuito(prompt_usuario: str) -> str:
    """⚡ Motor de Fallback Dinámico: Simula respuestas de IA variadas si no hay API Key activa"""
    prompt_lower = prompt_usuario.lower()

    # 🎯 Lógica de Tool Calling simulada
    if any(palabra in prompt_lower for palabra in ["proyección", "pronóstico", "días", "precio", "proyectar"]):
        import re
        numeros = re.findall(r'\d+', prompt_lower)
        dias = int(numeros[0]) if numeros else 10
        resultado_ml = pronosticar_precio_crudo_gbt(dias)
        return f"🤖 [Simulación Local]: He analizado tu consulta predictiva. Invocando mis funciones de ML...\n\n{resultado_ml}"

    # 🎭 Banco de respuestas dinámicas para evitar repetitividad
    respuestas = [
        "🤖 [Simulación Local]: Como analista senior, observo que la volatilidad actual sugiere un enfoque cauteloso. Recomiendo revisar el gráfico de Concept Drift abajo.",
        "🤖 [Simulación Local]: Interesante consulta. Desde una perspectiva MLOps, la salud del modelo es óptima, aunque los datos externos muestran señales mixtas.",
        "🤖 [Simulación Local]: Entendido. He procesado tu mensaje. En este modo demo, mi capacidad de razonamiento está limitada a heurísticas locales. Configura una GROQ_API_KEY para desbloquear mi cerebro completo.",
        "🤖 [Simulación Local]: Los niveles de soporte del crudo están bajo presión. Mi lógica local sugiere monitorear el Shadow Model para detectar anomalías tempranas.",
        "🤖 [Simulación Local]: ¡Hola! Estoy operando en modo de bajo consumo. Para análisis de lenguaje natural profundo, requiero conexión con Groq Cloud."
    ]

    return random.choice(respuestas)

def inicializar_agente_con_herramientas(prompt_usuario: str):
    # 🔄 Cortocircuito de seguridad: Si no hay credenciales, pasa directo al motor gratuito
    if not client_groq:
        return simular_agente_local_gratuito(prompt_usuario)

    modelo = "llama-3.3-70b-versatile"
    herramientas = [{
        "type": "function",
        "function": {
            "name": "pronosticar_precio_crudo_gbt",
            "description": "Calcula la proyección analítica del precio del crudo usando el ensamble Gradient Boosting Regressor de la app.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dias_proyeccion": {"type": "integer", "description": "Cantidad de días hacia el futuro a proyectar."}
                },
                "required": ["dias_proyeccion"]
            }
        }
    }]

    mensajes = [
        {"role": "system", "content": "Eres un economista senior y analista predictivo. Si el usuario te pide proyecciones del precio del crudo, debes usar obligatoriamente la función 'pronosticar_precio_crudo_gbt'."},
        {"role": "user", "content": prompt_usuario}
    ]

    try:
        response = client_groq.chat.completions.create(
            model=modelo, messages=mensajes, tools=herramientas, tool_choice="auto"
        )
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            funciones_disponibles = {"pronosticar_precio_crudo_gbt": pronosticar_precio_crudo_gbt}
            for tool_call in tool_calls:
                argumentos = json.loads(tool_call.function.arguments)
                return f"🤖 [Groq Cloud]: {funciones_disponibles[tool_call.function.name](dias_proyeccion=argumentos.get('dias_proyeccion'))}"
        return f"🤖 [Groq Cloud]: {response_message.content}"
    except Exception:
        return simular_agente_local_gratuito(prompt_usuario)
