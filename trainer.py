import joblib

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from config import (
    MODEL_FILE,
    TEST_SIZE,
    RANDOM_STATE
)

from indicators import FEATURE_COLUMNS


def train_model(df):

    X = df[FEATURE_COLUMNS]

    y = df["signal"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        shuffle=False
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        random_state=RANDOM_STATE
    )

    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(y_test, predictions)

    matrix = confusion_matrix(y_test, predictions)

    return {
        "model": model,
        "scaler": scaler,
        "accuracy": accuracy,
        "report": report,
        "matrix": matrix,
        "feature_importance": model.feature_importances_,
        "X_test": X_test,
        "y_test": y_test,
        "predictions": predictions
    }


def save_model(model, scaler):

    joblib.dump(
        {
            "model": model,
            "scaler": scaler
        },
        MODEL_FILE
    )


def load_model():

    return joblib.load(MODEL_FILE)


def predict_signals(df):

    bundle = load_model()

    model = bundle["model"]

    scaler = bundle["scaler"]

    X = df[FEATURE_COLUMNS]

    X_scaled = scaler.transform(X)

    df["prediction"] = model.predict(X_scaled)

    return df