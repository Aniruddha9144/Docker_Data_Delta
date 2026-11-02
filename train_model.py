import joblib
from pathlib import Path
from sklearn.linear_model import LinearRegression

# Define project directory
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"


def train_model():

    study_hours = [
        [1], [2], [3], [4], [5],
        [6], [7], [8], [9], [10]
    ]

    student_score = [
        35, 40, 50, 55, 60,
        68, 75, 80, 90, 95
    ]

    model = LinearRegression()

    model.fit(study_hours, student_score)

    joblib.dump(model, MODEL_PATH)

    print("ML Model Trained Successfully.")
    print(f"Model Saved At: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()