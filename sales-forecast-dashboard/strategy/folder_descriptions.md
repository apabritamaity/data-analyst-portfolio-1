Your concern is correct.

A professional project should avoid:

* duplicate code
* repeated logic
* messy notebooks
* random scripts

You should separate:

* experimentation
* production code
* outputs
* assets

That is how industry projects are organized.

---

# Real Industry Structure

```text id="n1e6d2"
sales-forecast-dashboard/
│
├── data/
│
├── notebooks/
│
├── src/
│
├── outputs/
│
├── dashboard/
│
├── models/
│
├── requirements.txt
│
└── README.md
```

Now understand the responsibility of each folder.

---

# 1. notebooks/

(Purpose: Research & Experimentation)

This folder is for:

* analysis
* experimentation
* visualization
* trying models
* understanding data

Think:

> “data scientist working area”

NOT production code.

---

# What Should Be Inside notebooks/

Example:

```text id="qutgnj"
notebooks/
│
├── 01_data_understanding.ipynb
├── 02_data_cleaning.ipynb
├── 03_eda.ipynb
├── 04_feature_engineering.ipynb
├── 05_model_training.ipynb
├── 06_model_evaluation.ipynb
```

---

# Responsibilities of Each Notebook

---

## 01_data_understanding.ipynb

Purpose:
Understand dataset.

Do:

* shape
* columns
* data types
* missing values
* duplicates

---

## 02_data_cleaning.ipynb

Purpose:
Experiment with cleaning.

Do:

* null handling
* encoding
* formatting
* date conversion

After finalized:
move reusable logic to `src/`.

---

## 03_eda.ipynb

Purpose:
Visualization & insights.

Do:

* trends
* distributions
* correlations
* category analysis

This notebook creates business insights.

---

## 04_feature_engineering.ipynb

Purpose:
Create ML features.

Example:

* month
* quarter
* season
* lag features

---

## 05_model_training.ipynb

Purpose:
Experiment with models.

Try:

* Linear Regression
* Random Forest
* XGBoost

Compare performance.

---

## 06_model_evaluation.ipynb

Purpose:
Evaluate model.

Metrics:

* RMSE
* MAE
* R²

Visuals:

* actual vs predicted

---

# Important Rule

Notebook = experimentation only.

Once finalized:
move clean reusable code into `src/`.

This is industry practice.

---

# 2. src/

(Purpose: Production Code)

This is the MOST important folder.

Think:

> “clean reusable pipeline code”

---

# What Should Be Inside src/

Example:

```text id="6yxkl1"
src/
│
├── preprocessing.py
├── feature_engineering.py
├── train_model.py
├── predict.py
├── evaluate.py
├── utils.py
```

---

# Responsibilities

---

## preprocessing.py

Contains:

* data cleaning functions
* preprocessing pipeline

Example:

```python id="5q34ic"
def clean_data(df):
    ...
```

---

## feature_engineering.py

Contains:

* reusable feature generation

Example:

```python id="u4gzsz"
def create_time_features(df):
    ...
```

---

## train_model.py

Contains:

* train final model
* save trained model

Example:

```python id="n9l6i3"
joblib.dump(model, "models/model.pkl")
```

---

## predict.py

Contains:

* load model
* generate future predictions

Example:

```python id="y90rhi"
future_predictions.csv
```

---

## evaluate.py

Contains:

* RMSE
* MAE
* plots
* metrics

---

## utils.py

Contains:
shared helper functions.

Example:

* file loading
* logging
* date utilities

---

# Key Industry Principle

## notebooks/

= thinking & experimentation

## src/

= reusable production code

This separation is extremely important.

---

# 3. outputs/

(Purpose: Generated Results)

This folder stores:

* generated files
* predictions
* charts
* reports

NOT source code.

---

# What Should Be Inside outputs/

Example:

```text id="rkkg8e"
outputs/
│
├── predictions/
│   ├── sales_forecast.csv
│
├── reports/
│   ├── model_metrics.txt
│
├── figures/
│   ├── sales_trend.png
│   ├── forecast_plot.png
```

---

# Responsibilities

---

## predictions/

Stores:

* generated prediction CSVs

Example:

```text id="sz9kxf"
future_sales_predictions.csv
```

---

## reports/

Stores:

* evaluation reports
* metrics

---

## figures/

Stores:

* exported plots
* charts
* visuals for README

---

# 4. models/

(Purpose: Saved Trained Models)

Example:

```text id="w5q38y"
models/
│
├── sales_forecast_model.pkl
```

Contains:

* serialized ML models

---

# 5. dashboard/

(Purpose: Power BI Files)

Example:

```text id="2t2qoi"
dashboard/
│
├── sales_dashboard.pbix
```

Contains:

* Power BI dashboard

---

# Real Workflow of Your Project

This is VERY important.

---

# PHASE 1 — Exploration

Inside notebooks:

* understand dataset
* clean data
* analyze trends
* experiment

---

# PHASE 2 — Productionize

Move reusable logic into:

```text id="7b2ayg"
src/
```

Now your project becomes clean.

---

# PHASE 3 — Generate Outputs

Run:

```bash id="vqvsk6"
python src/train_model.py
python src/predict.py
```

This creates:

* models
* prediction CSVs
* reports

---

# PHASE 4 — Dashboard

Power BI reads:

```text id="v2drx8"
outputs/predictions/sales_forecast.csv
```

Then visualize:

* forecasts
* KPIs
* trends

---

# Common Beginner Mistake

Bad approach:

* everything inside one notebook

Professional approach:

* notebooks for experimentation
* src for reusable code
* outputs for generated artifacts

---

# Final Recommended Structure

```text id="dpm2w4"
sales-forecast-dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
│   ├── evaluate.py
│   ├── utils.py
│
├── models/
│   ├── sales_model.pkl
│
├── outputs/
│   ├── predictions/
│   ├── reports/
│   ├── figures/
│
├── dashboard/
│   ├── sales_dashboard.pbix
│
├── requirements.txt
│
└── README.md
```

This structure is professional and portfolio-quality.
