import numpy as np
import json
import os
from datetime import datetime
from sklearn.ensemble import GradientBoostingRegressor

class PipelineMLOps:
    def __init__(self):
        self.modelo_produccion = GradientBoostingRegressor(n_estimators=50, random_state=42)
        self.modelo_sombra = None
        self.umbral_error_mae = 2.5
        self._esta_entrenado = False
        self.historial_errores = {"produccion": [], "sombra": []}

        if not os.path.exists("model_registry"):
            os.makedirs("model_registry")

    def simular_evaluacion_concept_drift(self, datos_historicos, precio_real_reciente) -> dict:
        if not self._esta_entrenado:
            self._reentrenar_modelo(datos_historicos, es_sombra=False)
            return {"status": "Entrenamiento Inicial", "drift_detectado": False}

        pred_prod = float(self.modelo_produccion.predict(datos_historicos[-1].reshape(1, -1))[0])
        error_prod = abs(precio_real_reciente - pred_prod)
        self.historial_errores["produccion"].append(error_prod)

        status = "Operación Estable"
        drift_detectado = False

        if error_prod > self.umbral_error_mae:
            drift_detectado = True
            status = "Concept Drift Detectado: Modelo en Sombra Entrenado"
            self._reentrenar_modelo(datos_historicos, es_sombra=True)

        if self.modelo_sombra:
            pred_sombra = float(self.modelo_sombra.predict(datos_historicos[-1].reshape(1, -1))[0])
            error_sombra = abs(precio_real_reciente - pred_sombra)
            self.historial_errores["sombra"].append(error_sombra)
        else:
            self.historial_errores["sombra"].append(None)

        return {
            "status": status,
            "drift_detectado": drift_detectado,
            "error_produccion": error_prod,
            "error_sombra": self.historial_errores["sombra"][-1]
        }

    def _reentrenar_modelo(self, datos, es_sombra=False):
        X = datos[:-1]
        y = np.random.uniform(65.0, 85.0, len(X))

        version = datetime.now().strftime("%Y%m%d_%H%M%S")
        metadata = {
            "version": version,
            "timestamp": datetime.now().isoformat(),
            "algoritmo": "GradientBoostingRegressor",
            "n_estimators": 50,
            "tipo_despliegue": "Shadow" if es_sombra else "Production"
        }

        with open(f"model_registry/model_{version}.json", "w") as f:
            json.dump(metadata, f, indent=4)

        if es_sombra:
            self.modelo_sombra = GradientBoostingRegressor(n_estimators=50, random_state=42)
            self.modelo_sombra.fit(X, y)
        else:
            self.modelo_produccion.fit(X, y)
            self._esta_entrenado = True

    def promover_sombra_a_produccion(self):
        if self.modelo_sombra:
            self.modelo_produccion = self.modelo_sombra
            self.modelo_sombra = None
            return True
        return False

mlops_manager = PipelineMLOps()