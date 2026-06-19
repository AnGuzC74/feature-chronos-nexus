import asyncio
import random
import sys
from datetime import datetime

class IndicadorEconomico:
    def __init__(self, nombre: str, valor_inicial: float):
        self._nombre = nombre
        self._valor = valor_inicial
        self._ultima_actualizacion = datetime.now()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor: float):
        if nuevo_valor < 0:
            raise ValueError(f"⚠️ Alerta Crítica: El indicador {self._nombre} no puede registrar valores negativos.")
        self._valor = nuevo_valor
        self._ultima_actualizacion = datetime.now()
        print(f"📈 [DATOS INTERNOS] {self._nombre} actualizado con éxito a: ${self._valor:.2f}")

async def simular_descarga_api_asincrona(fuente: str, retraso: int) -> dict:
    print(f"📡 Abriendo socket asíncrono con: {fuente}...")
    await asyncio.sleep(retraso)
    precio_crudo_simulado = random.uniform(65.0, 85.0)
    print(f"✅ Respuesta recibida y decodificada desde {fuente}")
    return {"fuente": fuente, "precio": precio_crudo_simulado, "timestamp": datetime.now().isoformat()}

async def orquestar_ingesta_concurrente():
    tareas = [
        simular_descarga_api_asincrona("OPEC_API_Cloud", 2),
        simular_descarga_api_asincrona("Bloomberg_Data_Feed", 3),
        simular_descarga_api_asincrona("Reuters_Energy_Broker", 1)
    ]
    resultados = await asyncio.gather(*tareas, return_exceptions=True)

    resultados_limpios = []
    for item in resultados:
        if isinstance(item, Exception):
            resultados_limpios.append({
                "fuente": "Proveedor Caído (Fallback)",
                "precio": 74.50,
                "timestamp": "TIMEOUT_CONTROLADO"
            })
        else:
            resultados_limpios.append(item)
    return resultados_limpios

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(orquestar_ingesta_concurrente())