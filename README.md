# Power BI Analytics Repository

Welcome to the Power BI Analytics repository! This repository contains two distinct Power BI projects, each focusing on different datasets and analytical goals. Below, you'll find an overview of each project, along with instructions on how to use them.

## Projects Included
### 1. Forex Analysis (EUR/USD)

This project focuses on analyzing and forecasting exchange rate data for the EUR/USD currency pair using Python for data processing and Power BI for visualization.
Key Features:

    Data Preparation: Fetch historical exchange rate data using yfinance, handle missing values, and apply logarithmic transformations.

    Exploratory Data Analysis (EDA): Compare original and log-transformed data, create histograms, and calculate summary statistics.

    Modeling: Train a linear regression model to predict future exchange rates.

    Power BI Dashboard: Visualize historical trends, predictions, and model performance metrics (MAE, R²).

Files Included:

    processed_eur_usd_data_with_log.csv: Historical data with transformations.

    future_predictions.csv: Predicted exchange rates.

    metrics.csv: Model performance metrics.

    Forex_Analysis_EUR&USD.pbix: Power BI dashboard file.

How to Use:

    Clone the repository.

    Open the Power BI file (Forex_Analysis_EUR&USD.pbix).

    Explore the interactive dashboard for insights and predictions.

### 2. Global Superstore Sales Analysis

This project analyzes the Global Superstore Dataset, focusing on sales, profit, and customer segmentation. It includes 20 DAX measures, ranging from basic to advanced, to derive key business insights.
Key Features:

    DAX Measures: Includes measures for sales tracking, profit margin, customer segmentation, shipping performance, and forecasting.

    Interactive Visualizations: Create dashboards to visualize sales trends, regional performance, and customer behavior.

    Dataset: Contains transactional data from an international retailer, including sales, profit, discounts, and geographical information.

DAX Measures Included:

    Basic to Intermediate: Total Sales, Total Profit, Profit Margin (%), Year-over-Year Growth (%), etc.

    Upper-Intermediate: Sales Contribution by Region (%), Next Month Sales Projection, Customer Profitability Classification, etc.

How to Use:

    Import the Global Superstore Dataset into Power BI.

    Add the provided DAX measures to the data model.

    Create visualizations and reports based on these measures.

## How to Clone and Use This Repository
### 1. Clone the Repository:

    git clone https://github.com/RRLuis/Power-Bi-Analytics.git

### 2. Navigate to the Project Folder:

  For Forex Analysis:
    cd Power-Bi-Analytics/Forex_Analysis_EUR&USD

  For Global Superstore Sales Analysis:
    cd Power-Bi-Analytics/Global_Superstore_Sales_Analysis
    
### 3. Open the Power BI Files:

    Load the .pbix files in Power BI Desktop.

    Connect to the provided datasets or replace them with your own.

## Tools and Technologies

    Power BI: Data modeling, DAX measures, and interactive dashboards.

    Python (for Forex Analysis): Data fetching, cleaning, and modeling.

    DAX: Intermediate calculations and business logic.

## Future Enhancements

    Forex Analysis: Add more currency pairs or extend the forecasting period.

    Global Superstore Sales Analysis: Build interactive dashboards for sales trends and customer behavior.

## About the Datasets

    Forex Analysis: Historical EUR/USD exchange rates fetched using yfinance.

    Global Superstore Sales Analysis: Dataset available on Kaggle.
    
