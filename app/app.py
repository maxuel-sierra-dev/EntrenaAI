
import streamlit as st
import pandas as pd
import sys
from pathlib import Path
from datetime import date, datetime

# =====================================================
# CONFIGURACIÓN
# =====================================================

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.predict import predecir_partido

st.set_page_config(
    page_title="EntrenaAI | Predictor",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# ESTILOS
# =====================================================

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0;
    }

    .subtitle {
        color: #aab4c3;
        font-size: 16px;
        margin-bottom: 25px;
    }

    div[data-testid="stMetric"] {
        background-color: #1c2331;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #303b4d;
    }

    .team-card {
        background-color: #1c2331;
        border: 1px solid #303b4d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }

    .team-name {
        font-size: 20px;
        font-weight: bold;
        color: white;
    }

    .team-info {
        color: #aab4c3;
        font-size: 14px;
    }

    .winner {
        background-color: #163d30;
        border: 1px solid #239b70;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# CARGAR DATOS
# =====================================================

@st.cache_data
def cargar_datos():
    return pd.read_csv(
        ROOT_DIR / "data" / "partidos_2024_limpio.csv"
    )


df = cargar_datos()


# =====================================================
# CATÁLOGO DE EQUIPOS
# =====================================================

equipos_locales = df[
    ["homeTeam", "homeId", "homeClassification", "homeConference"]
].copy()

equipos_locales.columns = [
    "equipo", "id", "clasificacion", "conferencia"
]

equipos_visitantes = df[
    ["awayTeam", "awayId", "awayClassification", "awayConference"]
].copy()

equipos_visitantes.columns = [
    "equipo", "id", "clasificacion", "conferencia"
]

equipos = pd.concat(
    [equipos_locales, equipos_visitantes],
    ignore_index=True
)

equipos = (
    equipos.dropna(subset=["equipo", "id"])
    .drop_duplicates(subset=["equipo"])
    .sort_values("equipo")
    .reset_index(drop=True)
)

nombres_equipos = equipos["equipo"].astype(str).tolist()


# =====================================================
# ENCABEZADO
# =====================================================

st.markdown(
    '<div class="main-title">🏈 EntrenaAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Sistema inteligente de predicción de fútbol americano universitario'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# BARRA LATERAL
# =====================================================

with st.sidebar:
    st.title("🏈 EntrenaAI")
    st.write("Panel de control")
    st.divider()

    st.markdown("### Acerca del proyecto")

    st.write(
        "EntrenaAI utiliza Machine Learning para estimar "
        "las probabilidades de victoria de los equipos."
    )

    st.divider()

    st.markdown("### Modelo utilizado")
    st.write("Regresión Logística")

    st.markdown("### Datos de entrenamiento")
    st.write("Temporada 2024")

    st.divider()

    st.caption("Proyecto académico de Machine Learning")


# =====================================================
# FORMULARIO
# =====================================================

st.header("⚙️ Configurar encuentro")

with st.form("formulario_partido"):

    st.subheader("1. Selección de equipos")

    col1, col2 = st.columns(2)

    with col1:
        equipo_local = st.selectbox(
            "🏠 Equipo local",
            nombres_equipos
        )

    with col2:
        opciones_visitante = [
            equipo for equipo in nombres_equipos
            if equipo != equipo_local
        ]

        equipo_visitante = st.selectbox(
            "✈️ Equipo visitante",
            opciones_visitante
        )

    datos_local = equipos[
        equipos["equipo"] == equipo_local
    ].iloc[0]

    datos_visitante = equipos[
        equipos["equipo"] == equipo_visitante
    ].iloc[0]

    st.subheader("2. Información de los equipos")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div class="team-card">
                <div class="team-name">🏠 {equipo_local}</div>
                <div class="team-info">
                    Clasificación: {datos_local['clasificacion']}<br>
                    Conferencia: {datos_local['conferencia']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="team-card">
                <div class="team-name">✈️ {equipo_visitante}</div>
                <div class="team-info">
                    Clasificación: {datos_visitante['clasificacion']}<br>
                    Conferencia: {datos_visitante['conferencia']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("3. Información del partido")

    col5, col6, col7 = st.columns(3)

    with col5:
        semana = st.number_input(
            "Semana",
            min_value=1,
            max_value=20,
            value=1
        )

    with col6:
        temporada_tipo = st.selectbox(
            "Tipo de temporada",
            sorted(
                df["seasonType"].dropna().astype(str).unique()
            )
        )

    with col7:
        fecha = st.date_input(
            "Fecha del partido",
            value=date.today()
        )

    col8, col9 = st.columns(2)

    with col8:
        neutral = st.selectbox(
            "Campo neutral",
            [False, True]
        )

    with col9:
        conferencia = st.selectbox(
            "Partido de conferencia",
            [False, True]
        )

    hora_por_definir = st.selectbox(
        "¿Hora por definir?",
        [False, True]
    )

    enviar = st.form_submit_button(
        "🏈 GENERAR PREDICCIÓN",
        use_container_width=True
    )


# =====================================================
# PREDICCIÓN
# =====================================================

if enviar:

    partido = pd.DataFrame([{
        "week": semana,
        "seasonType": temporada_tipo,
        "neutralSite": neutral,
        "conferenceGame": conferencia,
        "homeId": datos_local["id"],
        "awayId": datos_visitante["id"],
        "homeClassification": datos_local["clasificacion"],
        "awayClassification": datos_visitante["clasificacion"],
        "homeConference": datos_local["conferencia"],
        "awayConference": datos_visitante["conferencia"],
        "startTimeTBD": hora_por_definir,
        "startDate": fecha
    }])

    try:

        resultado = predecir_partido(partido)

        prob_local = (
            resultado["probabilidad_local"].iloc[0] * 100
        )

        prob_visitante = (
            resultado["probabilidad_visitante"].iloc[0] * 100
        )

        ganador = (
            equipo_local
            if prob_local >= prob_visitante
            else equipo_visitante
        )

        diferencia = abs(prob_local - prob_visitante)

        st.divider()

        st.header("📊 Resultados del análisis")

        st.write(
            f"**{equipo_local}** vs **{equipo_visitante}**"
        )

        # Métricas
        col10, col11 = st.columns(2)

        with col10:
            st.metric(
                f"🏠 {equipo_local}",
                f"{prob_local:.2f}%"
            )

        with col11:
            st.metric(
                f"✈️ {equipo_visitante}",
                f"{prob_visitante:.2f}%"
            )

        # Gráfico
        st.subheader("Comparación de probabilidades")

        grafico = pd.DataFrame({
            "Equipo": [equipo_local, equipo_visitante],
            "Probabilidad (%)": [
                prob_local,
                prob_visitante
            ]
        }).set_index("Equipo")

        st.bar_chart(
            grafico,
            y="Probabilidad (%)",
            height=350
        )

        # Favorito
        st.divider()

        st.subheader("🏆 Pronóstico del modelo")

        st.markdown(
            f"""
            <div class="winner">
                <h2>⭐ Equipo favorito</h2>
                <h1>{ganador}</h1>
                <p>Diferencia de probabilidades: {diferencia:.2f} puntos</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            "Las probabilidades son estimaciones del modelo. "
            "No representan garantías del resultado real. "
            "Modelo entrenado con datos de 2024."
        )

        # Historial de predicciones
        if "historial" not in st.session_state:
            st.session_state.historial = []

        st.session_state.historial.append({
            "Fecha de consulta": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),
            "Equipo local": equipo_local,
            "Equipo visitante": equipo_visitante,
            "Prob. local (%)": round(prob_local, 2),
            "Prob. visitante (%)": round(prob_visitante, 2),
            "Favorito": ganador
        })

    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")


# =====================================================
# HISTORIAL
# =====================================================

if "historial" in st.session_state and st.session_state.historial:

    st.divider()

    st.header("📚 Historial de predicciones")

    historial_df = pd.DataFrame(
        st.session_state.historial
    )

    st.dataframe(
        historial_df,
        use_container_width=True,
        hide_index=True
    )

    csv = historial_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Descargar historial CSV",
        data=csv,
        file_name="historial_entrenaai.csv",
        mime="text/csv"
    )

    if st.button("🗑️ Limpiar historial"):
        st.session_state.historial = []
        st.rerun()


# =====================================================
# PIE DE PÁGINA
# =====================================================

st.divider()

st.caption(
    "EntrenaAI | Proyecto académico de Machine Learning | 2026"
)
