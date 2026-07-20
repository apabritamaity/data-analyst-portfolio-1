import joblib
import pandas as pd

from src.config import (
    MODEL_PATH,
    PROCESSED_DATA_PATH,
    PREDICTION_PATH,
    X_TEST_PATH,
    Y_TEST_PATH
)

## Model Loading
def load_model():

    return joblib.load(MODEL_PATH)

## Prediction
def predict(model, X):

    return model.predict(X)

## Main function
def main():

    print("Loading model...")

    model = load_model()

    df = pd.read_csv(PROCESSED_DATA_PATH)

    # X = df.drop(columns=["Discount price"])
    X = pd.read_csv(X_TEST_PATH)
    y = pd.read_csv(Y_TEST_PATH)

    predictions = predict(model, X)

    prediction_df = X.copy()

    prediction_df["Actual Price"] = y.values

    prediction_df["Predicted Price"] = predictions

    prediction_df["Residual"] = (
        prediction_df["Actual Price"] - prediction_df["Predicted Price"]
    )

    prediction_df["Absolute Error"] = (
        prediction_df["Residual"].abs()
    )

    prediction_df["Percentage Error"] = (
        prediction_df["Absolute Error"]/prediction_df["Actual Price"]
    ) * 100

    prediction_df.to_csv(
        PREDICTION_PATH,
        index=False
    )

    print("Predictions saved successfully.")


if __name__ == "__main__":

    main()