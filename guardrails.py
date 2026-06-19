from abc import ABC, abstractmethod

class HerramientaAgente(ABC):
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass

    @property
    @abstractmethod
    def nivel_permiso(self) -> str:
        pass

    @abstractmethod
    def ejecutar(self, **kwargs) -> str:
        pass

class HerramientaReentrenamiento(HerramientaAgente):
    @property
    def nombre(self) -> str:
        return "forzar_reentrenamiento_sistema"

    @property
    def nivel_permiso(self) -> str:
        return "CRÍTICO"

    def ejecutar(self, **kwargs) -> str:
        return "🔒 Guardrail Activo: Intento de ejecución de comando CRÍTICO abortado. Requiere token MFA del Arquitecto de Datos."

class MiddlewareSeguridad:
    def __init__(self):
        self.herramientas = {
            "forzar_reentrenamiento_sistema": HerramientaReentrenamiento()
        }

    def verificar_y_ejecutar(self, nombre_funcion: str) -> str:
        if nombre_funcion in self.herramientas:
            herramienta = self.herramientas[nombre_funcion]
            if herramienta.nivel_permiso == "CRÍTICO":
                return herramienta.ejecutar()
        return None

guardrail_manager = MiddlewareSeguridad()