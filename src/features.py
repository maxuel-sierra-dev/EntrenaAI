
import pandas as pd


# Características utilizadas durante el entrenamiento
FEATURES = [
    "week",
    "seasonType",
    "neutralSite",
    "conferenceGame",
    "homeId",
    "awayId",
    "homeClassification",
    "awayClassification",
    "homeConference",
    "awayConference",
    "startTimeTBD",
    "month",
    "dayOfWeek"
]


def crear_caracteristicas(df):
    """
    Prepara las características para el modelo EntrenaAI.
    """

    df = df.copy()

    # Convertir fecha
    df["startDate"] = pd.to_datetime(df["startDate"])

    # Extraer características temporales
    df["month"] = df["startDate"].dt.month
    df["dayOfWeek"] = df["startDate"].dt.dayofweek

    # Seleccionar las 13 características del entrenamiento
    X = df[FEATURES].copy()

    # Rellenar valores faltantes de las variables categóricas
    columnas_categoricas = [
        "seasonType",
        "neutralSite",
        "conferenceGame",
        "homeId",
        "awayId",
        "homeClassification",
        "awayClassification",
        "homeConference",
        "awayConference",
        "startTimeTBD"
    ]

    X[columnas_categoricas] = (
        X[columnas_categoricas].fillna("Unknown")
    )

    return X
