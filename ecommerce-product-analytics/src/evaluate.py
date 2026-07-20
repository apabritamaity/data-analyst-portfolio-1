import numpy as np
import pandas as pd
import numpy as np
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from src.config import (
    MODEL_PATH,
    X_TEST_PATH,
    Y_TEST_PATH,
    REPORT_PATH,
    FEATURE_IMPORTANCE_PATH
)

## Evaluate model
def evaluate_model(y_true, y_pred):

    metrics = {

        "MAE": mean_absolute_error(
            y_true,
            y_pred
        ),

        "RMSE": np.sqrt(
            mean_squared_error(
                y_true,
                y_pred
            )
        ),

        "R2 Score": r2_score(
            y_true,
            y_pred
        )
    }

    return metrics



def save_feature_importance(model):

    feature_names = [
        # Numeric Pipeline
        "Rating",
        "Reviews",
        "ram_gb",
        "storage_gb",
        "discount_pct(%)",
        # Yeo Pipeline
        "Stars",
        # Target Encoder
        "brand",
        # OneHot Encoder
        "storage_type_HDD",
        "storage_type_SSD",
        "processor_brand_Intel",
        # Ordinal Encoder
        "processor_tier",
        # Passthrough
        "is_gaming",
        "processor_generation",
        "premium_brand"
    ]

    coefficients = (
        model.named_steps["model"]
        .regressor_
        .coef_
    )

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Coefficient": coefficients,

        "Importance": np.abs(coefficients)

    })

    importance_df = (
        importance_df
        .sort_values(
            by="Importance",
            ascending=False
        )
    )

    importance_df.to_csv(
        FEATURE_IMPORTANCE_PATH,
        index=False
    )

    print("Feature importance saved successfully.")


## Training vs Testing Comparison
# def compare_train_test(
#     y_train,
#     y_train_pred,
#     y_test,
#     y_test_pred
#     ):


#     train_metrics = evaluate_model(
#         y_train,
#         y_train_pred
#     )

#     test_metrics = evaluate_model(
#         y_test,
#         y_test_pred
#     )

#     results = pd.DataFrame({

#         "Metric": [
#             "R2 Score",
#             "MAE",
#             "RMSE"
#         ],

#         "Train": [
#             train_metrics["r2_score"],
#             train_metrics["mae"],
#             train_metrics["rmse"]
#         ],

#         "Test": [
#             test_metrics["r2_score"],
#             test_metrics["mae"],
#             test_metrics["rmse"]
#         ]
#     })

#     return results

# ## Overfitting Check
# def check_overfitting(
#     train_r2,
#     test_r2
# ):

#     gap = train_r2 - test_r2

#     return {
#         "train_r2": train_r2,
#         "test_r2": test_r2,
#         "gap": gap
#     }



def main():

    print("Loading model...")

    model = joblib.load(MODEL_PATH)

    # df = pd.read_csv(PROCESSED_DATA_PATH)

    X = pd.read_csv(X_TEST_PATH)

    y = pd.read_csv(Y_TEST_PATH).squeeze()

    predictions = model.predict(X)

    metrics = evaluate_model(
        y,
        predictions
    )

    report = pd.DataFrame([metrics])

    report.to_csv(
        REPORT_PATH,
        index=False
    )

    save_feature_importance(model)

    print(report)

    print("\nEvaluation report saved.")


if __name__ == "__main__":

    main()