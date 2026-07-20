import joblib
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    KFold
)

from src.config import PROCESSED_DATA_PATH, MODEL_PATH, X_TEST_PATH, Y_TEST_PATH, BEST_PARAM_PATH

from src.preprocessing import create_preprocessor

## Split data
def split_data(df):

    X = df.drop(columns=["Discount price"])

    y = df["Discount price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    return X_train, X_test, y_train, y_test



## Build Pipeline
def build_pipeline():

    preprocessor = create_preprocessor()

    elastic_net = ElasticNet(
        random_state=42,
        max_iter=5000
    )

    model = TransformedTargetRegressor(
        regressor=elastic_net,
        func=np.log1p,
        inverse_func=np.expm1
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    return pipeline


## Hyperparameter Grid
def get_param_grid():

    param_grid = {

        "model__regressor__alpha": [0.001, 0.01, 0.1, 1, 10],

        "model__regressor__l1_ratio": [0.1, 0.3, 0.5, 0.7, 0.9]
    }

    return param_grid

## Train Model
def train_model(X_train, y_train):

    pipeline = build_pipeline()

    param_grid = get_param_grid()

    cv = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    elastic_net_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=cv,
        scoring="r2",
        n_jobs=-1
    )

    elastic_net_search.fit(
        X_train,
        y_train
    )

    return elastic_net_search


## Save Model
def save_model(model):

    joblib.dump(
        model.best_estimator_,
        MODEL_PATH
    )   

    print(
        "Model saved successfully."
    )


## Main Function
def main():

    df = pd.read_csv(PROCESSED_DATA_PATH)

    X_train, X_test, y_train, y_test = split_data(df)

    # Save test data
    X_test.to_csv(X_TEST_PATH, index=False)
    y_test.to_csv(Y_TEST_PATH, index=False)

    model = train_model(
        X_train,
        y_train
    )

    print(
        "Best Parameters:"
    )

    print(
        model.best_params_
    )

    best_params = pd.DataFrame([model.best_params_])

    best_params.to_csv(
        BEST_PARAM_PATH,
        index=False
    )

    print(
        "Best CV Score:"
    )

    print(
        model.best_score_
    )

    # save_model(model)


if __name__ == "__main__":
    main()