
import joblib
import pandas as pd
from pathlib import Path

from src.features import crear_caracteristicas


# Rutas del proyecto
ROOT_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT_DIR / "models"


def cargar_modelos():
    """
    Carga el modelo y el preprocesador guardados.
    """

    modelo = joblib.load(
        MODELS_DIR / "modelo_logistico.joblib"
    )

    preprocesador = joblib.load(
        MODELS_DIR / "preprocesador.joblib"
    )

    return modelo, preprocesador


def predecir_partido(df_partido):
    """
    Predice el resultado de uno o varios partidos.

    1 = Victoria local
    0 = Victoria visitante
    """

    modelo, preprocesador = cargar_modelos()

    # Preparar las características
    X = crear_caracteristicas(df_partido)

    # Aplicar el preprocesamiento
    X_encoded = preprocesador.transform(X)

    # Obtener predicción y probabilidades
    predicciones = modelo.predict(X_encoded)
    probabilidades = modelo.predict_proba(X_encoded)

    # Construir resultados
    resultados = pd.DataFrame({
        "prediccion": predicciones,
        "resultado": [
            "Victoria local" if p == 1
            else "Victoria visitante"
            for p in predicciones
        ],
        "probabilidad_local": probabilidades[:, 1],
        "probabilidad_visitante": probabilidades[:, 0]
    })

    return resultados
