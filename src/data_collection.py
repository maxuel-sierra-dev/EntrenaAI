
import os
import requests
import pandas as pd


API_URL = "https://api.collegefootballdata.com/games"


def obtener_partidos(temporada=2024):
    """
    Obtiene los partidos de una temporada desde la API.
    """

    api_key = os.getenv("CFBD_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró la variable de entorno CFBD_API_KEY."
        )

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params = {
        "year": temporada
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    datos = response.json()

    return pd.DataFrame(datos)
