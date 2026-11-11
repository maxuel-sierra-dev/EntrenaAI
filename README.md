# 🏈 EntrenaAI
### Sistema de predicción de resultados de fútbol americano universitario mediante Machine Learning

## 1. Descripción del proyecto

**EntrenaAI** es un proyecto de Machine Learning desarrollado para analizar partidos de fútbol americano universitario y estimar la probabilidad de victoria del equipo local o visitante.

El sistema utiliza datos históricos de partidos de la temporada 2024 para preparar un conjunto de datos, realizar análisis exploratorio, construir características, entrenar modelos de clasificación y generar predicciones.

Además, incorpora una interfaz web desarrollada con Streamlit que permite seleccionar dos equipos, configurar las características de un encuentro y visualizar las probabilidades estimadas por el modelo.

## 2. Objetivos

- Obtener y preparar datos históricos de fútbol americano universitario.
- Realizar limpieza y transformación de los datos.
- Analizar las características y distribuciones del conjunto de datos.
- Construir variables para el entrenamiento de modelos.
- Entrenar y evaluar algoritmos de Machine Learning.
- Comparar el rendimiento de los modelos mediante métricas de clasificación.
- Generar predicciones de nuevos encuentros.
- Desarrollar una interfaz web sencilla para interactuar con el sistema.

## 3. Tecnologías utilizadas

| Tecnología | Utilización |
|---|---|
| Python | Lenguaje principal |
| Pandas | Manipulación y limpieza de datos |
| NumPy | Operaciones numéricas |
| Matplotlib | Visualización de datos |
| Seaborn | Análisis exploratorio |
| Scikit-learn | Entrenamiento y evaluación |
| Joblib | Almacenamiento de modelos |
| Streamlit | Desarrollo de la interfaz web |
| Jupyter Notebook | Desarrollo y documentación experimental |
| Requests | Solicitudes a la API |

## 4. Fuente de datos

Los datos corresponden a partidos de fútbol americano universitario de la temporada 2024.

Se utilizó la API de **CollegeFootballData** como fuente de información.

El conjunto de datos contiene información relacionada con:

- Identificadores de los equipos.
- Equipo local y equipo visitante.
- Fecha del encuentro.
- Semana de competición.
- Tipo de temporada.
- Clasificación de los equipos.
- Conferencias.
- Puntuaciones finales.
- Información adicional de los partidos.

El conjunto inicial contenía aproximadamente 3,801 registros.

Después del proceso de limpieza y filtrado se trabajó con aproximadamente 3,786 partidos completos y sin empates.

## 5. Estructura del proyecto

```text
EntrenaAI/
│
├── app/
│   └── app.py
│
├── data/
│   ├── external/
│   ├── processed/
│   ├── raw/
│   ├── partidos_2024.csv
│   └── partidos_2024_limpio.csv
│
├── notebooks/
│   ├── 01_recoleccion_datos.ipynb
│   ├── 02_limpieza_datos.ipynb
│   ├── 03_analisis_exploratorio.ipynb
│   ├── 04_ingenieria_caracteristicas.ipynb
│   ├── 05_entrenamiento_modelos.ipynb
│   └── 06_predicciones.ipynb
│
├── models/
│   ├── preprocesador.joblib
│   ├── datos_entrenamiento.joblib
│   └── modelo_logistico.joblib
│
├── reports/
│
├── src/
│   ├── __init__.py
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   └── predict.py
│
├── tests/
│
└── README.md
```

## 6. Desarrollo del proyecto

El desarrollo se organizó en diferentes etapas.

### 6.1 Recolección de datos

Se obtuvieron los registros históricos de partidos universitarios correspondientes a la temporada 2024.

La información se almacenó en archivos CSV para facilitar su procesamiento y análisis posterior.

### 6.2 Limpieza de datos

Se realizaron las siguientes operaciones:

- Eliminación de registros duplicados.
- Identificación de valores faltantes.
- Eliminación de partidos incompletos.
- Exclusión de encuentros empatados.
- Revisión de los tipos de datos.
- Preparación de la variable objetivo.

Se creó la variable objetivo `homeWin`:

- `1`: victoria del equipo local.
- `0`: victoria del equipo visitante.

Esta variable se calculó comparando los puntos finales de ambos equipos.

### 6.3 Análisis exploratorio (EDA)

Se realizó un análisis exploratorio para comprender el comportamiento del conjunto de datos.

Se analizaron:

- Distribución de las victorias locales y visitantes.
- Estadísticas descriptivas.
- Valores faltantes.
- Distribuciones de las variables.
- Relaciones entre características.
- Comportamiento general de los partidos.

### 6.4 Ingeniería de características

Se seleccionaron características disponibles antes del encuentro para evitar utilizar información que solamente se conoce después del partido.

Entre las variables utilizadas se encuentran:

- `week`
- `seasonType`
- `neutralSite`
- `conferenceGame`
- `homeId`
- `awayId`
- `homeClassification`
- `awayClassification`
- `homeConference`
- `awayConference`
- `startTimeTBD`
- `month`
- `dayOfWeek`

También se transformaron las variables categóricas mediante One-Hot Encoding, utilizando `OneHotEncoder` con `handle_unknown="ignore"`.

Las variables numéricas se conservaron mediante el preprocesador de Scikit-learn.

### 6.5 Entrenamiento de modelos

Se prepararon los datos para entrenar y evaluar modelos de clasificación.

La división se realizó de forma temporal:

- Entrenamiento: semanas 1 a 12.
- Prueba: semanas 13 a 16.

Se evaluó inicialmente Regresión Logística y Random Forest.

La Regresión Logística obtuvo el mejor resultado entre los modelos evaluados hasta esta etapa.

## 7. Evaluación del modelo

Se utilizaron las siguientes métricas:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Matriz de confusión.

### Resultados obtenidos

| Métrica | Regresión Logística |
|---|---:|
| Accuracy | 68.06 % |
| Precision | 70.51 % |
| Recall | 84.53 % |
| F1-score | 76.88 % |

La Regresión Logística fue seleccionada como modelo principal de la versión actual de la aplicación.

Estos resultados corresponden al conjunto de prueba de la temporada 2024 y no garantizan el mismo rendimiento en temporadas futuras.

## 8. Sistema de predicciones

El proyecto cuenta con un módulo de predicción ubicado en:

`src/predict.py`

Este módulo permite:

1. Cargar el modelo entrenado.
2. Cargar el preprocesador.
3. Recibir los datos de un encuentro.
4. Transformar las características.
5. Generar una predicción.
6. Obtener las probabilidades de victoria de ambos equipos.

El resultado se interpreta de la siguiente manera:

- Victoria local.
- Victoria visitante.
- Probabilidad estimada del equipo local.
- Probabilidad estimada del equipo visitante.

## 9. Interfaz web

Se desarrolló una interfaz utilizando Streamlit.

La aplicación permite:

- Seleccionar el equipo local.
- Seleccionar el equipo visitante.
- Consultar automáticamente su clasificación y conferencia.
- Introducir la semana del partido.
- Seleccionar el tipo de temporada.
- Indicar si el encuentro se juega en campo neutral.
- Indicar si es un partido de conferencia.
- Introducir la fecha del encuentro.
- Generar una predicción.

La interfaz también presenta:

- Probabilidades de ambos equipos.
- Gráfico comparativo.
- Equipo favorito según el modelo.
- Diferencia entre las probabilidades.
- Historial de predicciones de la sesión.
- Opción de descargar el historial en CSV.

## 10. Instalación y ejecución

### Requisitos

- Python 3.10 o superior.
- Visual Studio Code (recomendado).
- Entorno virtual de Python.

### Crear el entorno virtual

Desde la carpeta principal del proyecto:

```bash
python -m venv .venv
```

### Activar el entorno virtual en Windows

```powershell
.venv\Scripts\activate
```

### Instalar las dependencias

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit requests jupyter
```

### Ejecutar la aplicación

Desde la carpeta principal `EntrenaAI`:

```bash
python -m streamlit run app/app.py
```

La aplicación estará disponible normalmente en:

```text
http://localhost:8501
```

## 11. Archivos importantes

| Archivo | Descripción |
|---|---|
| `partidos_2024.csv` | Datos originales |
| `partidos_2024_limpio.csv` | Datos preparados |
| `modelo_logistico.joblib` | Modelo entrenado |
| `preprocesador.joblib` | Transformación de características |
| `datos_entrenamiento.joblib` | Datos preparados para entrenamiento y prueba |
| `app.py` | Interfaz web |
| `predict.py` | Funciones para generar predicciones |

## 12. Limitaciones actuales y mejoras futuras

El proyecto constituye una primera versión funcional de un sistema de predicción.

Se identifican las siguientes oportunidades de mejora:

- Incorporar y evaluar LightGBM para completar la comparación de algoritmos.
- Desarrollar características históricas de rendimiento de los equipos.
- Implementar calibración de probabilidades.
- Evaluar el Brier Score.
- Seleccionar y validar un umbral de clasificación.
- Evaluar el sistema utilizando varias temporadas.
- Incorporar datos más recientes.
- Permitir probar los modelos mediante archivos CSV.

Las predicciones actuales utilizan un modelo entrenado con datos de 2024. Por tanto, las estimaciones de encuentros futuros deben interpretarse como resultados experimentales y no como probabilidades validadas para temporadas posteriores.

## 13. Conclusión

EntrenaAI permitió desarrollar un flujo de trabajo de Machine Learning aplicado al análisis de fútbol americano universitario.

Durante el desarrollo se trabajó con recolección de datos, limpieza, análisis exploratorio, ingeniería de características, entrenamiento de modelos, evaluación, almacenamiento de modelos e implementación de una interfaz web.

La aplicación demuestra cómo un modelo de clasificación puede integrarse en una herramienta interactiva que permite introducir información de un encuentro y obtener estimaciones de sus posibles resultados.

El proyecto también establece una base para futuras mejoras en la calidad de los datos, la ingeniería de características y el rendimiento predictivo.

---

**Proyecto académico: EntrenaAI**  
**Área:** Machine Learning y Ciencia de Datos  
**Lenguaje:** Python  
**Interfaz:** Streamlit  
**Datos utilizados:** Temporada 2024