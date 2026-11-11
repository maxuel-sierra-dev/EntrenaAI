
import pandas as pd


def limpiar_datos(df):
    """
    Limpia los datos de los partidos.
    """

    df = df.copy()

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Conservar partidos con resultados disponibles
    df = df.dropna(subset=["homePoints", "awayPoints"])

    # Excluir partidos empatados
    df = df[df["homePoints"] != df["awayPoints"]].copy()

    return df


def crear_variable_objetivo(df):
    """
    Crea homeWin a partir del resultado del partido.
    1 = Victoria local
    0 = Victoria visitante
    """

    df = df.copy()

    df["homeWin"] = (
        df["homePoints"] > df["awayPoints"]
    ).astype(int)

    return df
