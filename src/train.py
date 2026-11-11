
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression


# Rutas del proyecto
ROOT_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT_DIR / "models"

# Cargar los datos de entrenamiento previamente preparados
datos = joblib.load(MODELS_DIR / "datos_entrenamiento.joblib")

X_train = datos["X_train"]
y_train = datos["y_train"]

# Crear y entrenar el modelo
modelo = LogisticRegression(
    max_iter=2000,
    random_state=42
)

modelo.fit(X_train, y_train)

# Guardar modelo entrenado
joblib.dump(
    modelo,
    MODELS_DIR / "modelo_logistico.joblib"
)

print("Modelo entrenado correctamente.")
print("Modelo guardado en models/modelo_logistico.joblib")
