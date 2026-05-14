# AI-Powered E-Commerce Product Analytics Dashboard

## Project Overview

This project analyzes Flipkart laptop data to generate business insights related to:

- product pricing
- discounts
- customer ratings
- brand performance
- laptop specifications
- market segmentation

The project combines:
- Data Analytics
- Machine Learning
- Business Intelligence
- Dashboard Development

The goal is to build an AI-powered e-commerce analytics dashboard using Python and Power BI.

---

# Business Problem

E-commerce companies need to understand:

- which products perform better
- how pricing affects customer interest
- which brands dominate the market
- how discounts influence buying behavior
- which laptop specifications impact pricing

Traditional reporting systems only show historical data and often fail to provide predictive insights.

This project solves these challenges by combining analytics with machine learning to generate intelligent business insights.

---

# Project Goals

The main goals of this project are:

- Analyze laptop market trends
- Understand pricing behavior
- Compare brand performance
- Analyze discount strategies
- Build business intelligence dashboards
- Predict laptop pricing using machine learning
- Generate AI-powered business insights

---

# Tech Stack

## Programming
- Python

## Libraries
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Dashboard
- Power BI

## Environment
- Jupyter Notebook
- VS Code

---

# Dataset Information

The dataset contains Flipkart laptop product data including:

- Brand
- Product Name
- Processor
- RAM
- Storage
- Ratings
- Original Price
- Discount Price
- Discount Percentage

---

# Project Workflow

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Machine Learning Model
    ↓
Prediction Generation
    ↓
Power BI Dashboard
```

---

# Project Structure

```text
ecommerce-product-analytics/
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
│
├── artifacts/
│   ├── models/
│   ├── predictions/
│   ├── reports/
│   ├── figures/
│
├── dashboard/
│   ├── ecommerce_dashboard.pbix
│
├── requirements.txt
│
└── README.md
```

---

# Exploratory Data Analysis (EDA)

The project performs multiple business-oriented analyses including:

- Brand-wise price analysis
- RAM vs Price analysis
- Storage vs Price analysis
- Processor analysis
- Discount analysis
- Customer rating analysis
- Market segmentation analysis

---

# Machine Learning Component

## Objective

Predict laptop prices based on:

- brand
- RAM
- storage
- processor
- ratings
- product specifications

---

# ML Workflow

## 1. Data Preprocessing
- missing value handling
- datatype conversion
- feature extraction

## 2. Feature Engineering
- RAM extraction
- storage extraction
- processor categorization
- categorical encoding

## 3. Model Training
Machine learning models used:
- Linear Regression
- Random Forest Regressor

## 4. Model Evaluation
Evaluation metrics:
- MAE
- RMSE
- R² Score

## 5. Prediction Generation
The trained model predicts laptop pricing for business intelligence analysis.

---

# Dashboard Features

The Power BI dashboard includes:

## Executive Dashboard
- Total Products
- Average Price
- Average Discount
- Average Rating

## Pricing Dashboard
- Brand-wise pricing
- Price distribution
- Product comparison

## Product Analysis Dashboard
- RAM analysis
- Storage analysis
- Processor analysis

## Customer Insights Dashboard
- Rating trends
- Product popularity
- Discount impact

## AI-Powered Insights Dashboard
- Predicted laptop prices
- Price trend analysis
- Feature importance analysis
- Product intelligence insights

---

# Example Business Insights

Some insights generated from the project:

- Premium brands have higher average pricing
- Higher RAM configurations increase laptop price
- SSD laptops are generally more expensive
- Mid-range products receive higher customer engagement
- Discounts significantly affect customer interest

---

# Future Improvements

Possible future enhancements:

- Deep learning-based price prediction
- Real-time dashboard updates
- Customer sentiment analysis
- Recommendation system
- Streamlit deployment
- API-based prediction service

---

# Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Data Visualization
- Business Intelligence
- Dashboard Development
- E-Commerce Analytics

---

# Author

AMARESH MAITY

AI Engineer | Data Analyst | ML Developer