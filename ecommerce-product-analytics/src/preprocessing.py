import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    FunctionTransformer,
    PowerTransformer,
    StandardScaler,
    OneHotEncoder,
    OrdinalEncoder,
    TargetEncoder
)


## Rating
def clean_rating(df):

    df["Rating"] = (
        df["Rating"]
        .str.replace("Ratings", "", regex=True)
        .str.replace(",", "")
        .str.replace("NIL", "0")
        .astype(float)
    )

    return df

## Reviews
def clean_reviews(df):

    df["Reviews"] = (
        df["Reviews"]
        .str.replace("Reviews", "", regex=True)
        .str.replace(",", "")
        .str.replace("NIL", "0")
        .astype(float)
    )

    return df

## Stars
def clean_stars(df):

    df["Stars"] = (
        df["Stars"]
        .str.replace("NIL", "0")
        .astype(float)
    )

    return df


def clean_dataset(df):

    """
    Clean rating, reviews and stars columns
    """

    df = clean_rating(df)

    df = clean_reviews(df)

    df = clean_stars(df)

    return df



## Create Numeric Pipeline

def create_numeric_pipeline():

    numeric_pipeline = Pipeline([
        ("log_transform", FunctionTransformer(np.log1p, validate=False)),
        ("scaler", StandardScaler())
    ])

    return numeric_pipeline

 ## Create Yeo Pipeline
def create_yeo_pipeline():

    yeo_pipeline = Pipeline([
        ("yeo_transform", PowerTransformer(method='yeo-johnson')),
        ("scaler", StandardScaler())
    ])

    return yeo_pipeline

## Create Main Preprocessor

def create_preprocessor():

    numeric_pipeline = create_numeric_pipeline()

    yeo_pipeline = create_yeo_pipeline()

    
    preprocessor = ColumnTransformer(

        transformers=[
            ("numeric_pipeline", numeric_pipeline, ["Rating", "Reviews", "ram_gb", "storage_gb", "discount_pct(%)"]),
            ("yeo_pipeline", yeo_pipeline, ["Stars"]),

            ## TARGET ENCODING for brand (Keeps it as 1 column)
            ("target_enc", TargetEncoder(smooth="auto", cv=5, target_type='continuous'), ["brand"]),

            ("OneHotEncoding", OneHotEncoder(
                drop='first',
                min_frequency=6,          # Categories appearing < 6 times become 'Other'
                handle_unknown='infrequent_if_exist', 
                sparse_output=False
                ), ["storage_type", "processor_brand"]
            ),

            ("OrdinalEncoding",OrdinalEncoder(categories=[["Entry", "Mid", "High", "Ultra", "Other"]]),["processor_tier"])
        ],
        
        remainder='passthrough'
    )

    return preprocessor


# if __name__ == "__main__":

#     preprocessor = create_preprocessor()

#     print(preprocessor)