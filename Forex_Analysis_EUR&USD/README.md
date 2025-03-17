# Exchange Rate Analysis and Forecasting (Python and Power Bi)
## Project Overview

This project focuses on analyzing and visualizing exchange rate data for a currency pair (USD/EUR) using Python for data processing, modeling, and Power BI for interactive dashboard creation. The workflow includes data preparation, exploratory data analysis (EDA), logarithmic transformations, regression modeling, and forecasting future exchange rates. The final deliverable is an interactive Power BI dashboard that presents insights, predictions, and model performance metrics.

## Objective

Build an end-to-end workflow to:

    Analyze historical exchange rate data.

    Perform EDA with a focus on logarithmic transformations.

    Develop a regression model to predict future exchange rates (3 periods).

    Visualize insights and predictions in an interactive Power BI dashboard.

## Project Steps

### 1. Data Preparation

    Fetch historical exchange rate data for the last 2 years using the yfinance API.

    Save the raw data as a CSV file.

    Handle missing values.

    Ensure proper date formatting.

    Include a 7-day rolling average as a column.

    Create a copy of the original dataframe with the date column as the index.

### 2. Exploratory Data Analysis (EDA)

    Compare original exchange rates with their logarithmic transformations.

    Evaluate trends, variability, and distributions.

    Create distribution histograms for original and log-transformed data.

    Calculate summary statistics (mean, median, standard deviation, etc.).

    Compute monthly averages using group-by functionality.

    Remove duplicates.

### 3. Modeling

    Train a linear regression model to predict future log-transformed exchange rates.

    Perform back-transformation to interpret predictions in the original scale.

    Save predictions and evaluation metrics (R², MAE, etc.).

### 4. Dashboard Design

    Import processed data into Power BI.

    Create an interactive dashboard with:

        Comparisons of original and log-transformed trends.

        Historical data visualizations and scatter plots for correlations.

        Predicted exchange rates and model performance metrics.

        Filters for exploration by date or other dimensions.

## Deliverables

    Python Script Files (.py): "Forex-Analysis-EURUSD_Script_File.py"

    PDF with Executed Code: "Forex-Analysis-EURUSD-Executed_Code_Notebook.pdf"

    Power BI File (.pbix): "Forex_Analysis_EURUSD_Dashboard.pbix"

## Tools and Technologies

    Python Libraries:

        yfinance: Fetching exchange rate data.

        pandas, numpy: Data manipulation.

        matplotlib, seaborn: Data visualization.

        scikit-learn: Regression modeling.

    Power BI:
	Data loading and transformation (Power Query).
 
 	Creation of a date table and relationships between tables.
  
  	Development of measures and calculated columns using DAX.
   
  	Design of interactive visualizations:
    		Line charts for historical trends and predictions.
    		Histograms for distribution analysis.
    		Cards for model performance metrics (MAE, R²).
  			Implementation of filters for dynamic exploration.

## How to Use This Project

### 1. Clone the Repository:
    git clone https://github.com/RRLuis/Power-Bi-Analytics.git

    -Navigate to project folder
    
    cd Power-Bi-Analytics/Forex_Analysis_EUR&USD

### 2. Install Dependencies:
    pip install -r requirements.txt

### 3. Run the Python Script:
        Execute the script to fetch data, perform EDA, and train the model.

        Save the processed data and predictions.

### 4. Open the Power BI File:

        Load the processed data into Power BI.
	
		Files to Upload to Power BI and How They Are Connected

        			processed_eur_usd_data_with_log.csv: Contains historical exchange rates with logarithmic transformations.

        			future_predictions.csv: Contains predicted exchange rates for 3 future periods.

        			metrics.csv: Contains model performance metrics (MAE, R²).

    		How They Are Connected:

        			Relationship: Connect processed_eur_usd_data_with_log and future_predictions using the Date column.

        			Metrics Table: No relationship needed; use it directly for displaying MAE and R² in cards.

        Explore the interactive dashboard.

 ![image alt](https://github.com/RRLuis/Power-Bi-Analytics/blob/main/Forex_Analysis_EUR&USD/Forex_Analysis_db_diagram.png?raw=true)


## Project Structure

exchange-rate-analysis/

│

├── data/

│   ├── raw_eur_usd_data.csv          # Raw exchange rate data

│   ├── processed_eur_usd_data.csv    # Processed data with transformations

│   └── future_predictions.csv        # Predicted exchange rates

│

├── scripts/

│   ├── data_preparation.py           # Data fetching and cleaning

│   ├── eda.py                        # Exploratory data analysis

│   └── modeling.py                   # Regression modeling and predictions

│

├── dashboard/

│   └── exchange_rate_dashboard.pbix  # Power BI dashboard

│

├── README.md                         # Project documentation

└── requirements.txt                  # Python dependencies



## Key Insights

    Logarithmic Transformation: Helps stabilize variance and normalize data distribution.

    Regression Model: Predicts future exchange rates with evaluation metrics (R², MAE).

    Power BI Dashboard: Provides interactive visualizations for historical trends, predictions, and model performance.

