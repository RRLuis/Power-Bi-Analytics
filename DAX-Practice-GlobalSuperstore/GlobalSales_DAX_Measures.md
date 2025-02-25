-- ============================

SAMPLE OF DAX MEASURES APPLIED TO "GLOBAL SUPERSTORE" DATASET

Data Source: https://www.kaggle.com/datasets/shekpaul/global-superstore

-- ============================

-- 1. Total Sales
Total Sales = SUM('Orders'[Sales])

-- 2. Total Profit
Total Profit = SUM('Orders'[Profit])

-- 3. Profit Margin (%): Calculates profit as a percentage of total sales.
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

-- 4. Total Orders: Counts the unique number of orders placed.
Total Orders = DISTINCTCOUNT('Orders'[Order ID])

-- 5. Average Order Value: Average sales revenue per order
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)

-- 6. Sales per Customer: Determines the average sales per unique customer.
Sales per Customer = DIVIDE([Total Sales], DISTINCTCOUNT('Orders'[Customer ID]), 0)

-- 7. Delayed Shipments Count
Delayed Shipments Count = COUNTROWS(FILTER('Orders', 'Orders'[Ship Date] > 'Orders'[Order Date]))

-- 8. Year-over-Year Sales Growth: Calculates the sales increase or decrease compared to the previous year.
YoY Sales Growth = 
VAR PreviousYearSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Orders'[Order Date]))
RETURN [Total Sales] - PreviousYearSales

-- 9. Year-over-Year Growth (%): Percentage change in sales from the previous year.
YoY Growth % = DIVIDE([YoY Sales Growth], CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Orders'[Order Date])), 0)

-- 10. Country Sales Ranking: Assigns a rank to each country based on total sales.
Country Sales Rank = RANKX(ALL('Orders'[Country]), [Total Sales], , DESC)

-- 11. Cumulative Sales by Year
Cumulative Sales = 
CALCULATE([Total Sales],
    FILTER(ALLSELECTED('Orders'[Order Date]),
    'Orders'[Order Date] <= MAX('Orders'[Order Date])
    )
)

-- 12. Top 5 Selling Categories
Top 5 Categories Sales = 
IF(
    RANKX(ALL('Orders'[Category]), [Total Sales], , DESC) <= 5, [Total Sales]
)

-- 13. Previous Month Sales
Previous Month Sales = 
CALCULATE([Total Sales], PREVIOUSMONTH('Orders'[Order Date]))

-- 14. Month-over-Month Sales Difference
MoM Sales Difference = [Total Sales] - [Previous Month Sales]

-- 15. High Stock Product Sales: Filters sales for products with stock greater than 100.
High Stock Product Sales = 
CALCULATE([Total Sales], FILTER('Orders', 'Orders'[Stock] > 100))


-- 16. Sales Contribution by Region (%)
Sales Contribution Region % = 
VAR TotalSales = [Total Sales]
VAR RegionSales = SUM('Orders'[Sales])
RETURN DIVIDE(RegionSales, TotalSales, 0)

-- 17. Next Month Sales Projection (Moving Average): Estimates the next month’s sales based on a 3-month moving average.
Next Month Sales Projection = 
VAR Sales3Months = 
    AVERAGEX(
        DATESINPERIOD('Orders'[Order Date], MAX('Orders'[Order Date]), -3, MONTH),
        [Total Sales]
    )
RETURN Sales3Months

-- 18. Customer Profitability Classification: Classifies customers as profitable or non-profitable based on their total profit.
Customer Profitability = 
VAR AverageProfit = AVERAGE('Orders'[Profit])
VAR CustomerProfit = SUM('Orders'[Profit])
RETURN IF(CustomerProfit > AverageProfit, "Profitable Customer", "Non-Profitable Customer")


-- 19. Top-Selling Category Sales (Dynamic): retrieves sales for the highest-selling product category.
Top Selling Category Sales = 
VAR TopCategory = 
    TOPN(1, SUMMARIZE('Orders', 'Orders'[Category], "Sales", [Total Sales]), [Total Sales], DESC)
RETURN 
    CALCULATE([Total Sales], 'Orders'[Category] IN TopCategory)


-- 20. Customer Purchase Segmentation: Categorizes customers based on their total purchase value.
Customer Segmentation = 
VAR SalesPerCustomer = SUM('Orders'[Sales])
RETURN SWITCH(
    TRUE(),
    SalesPerCustomer >= 5000, "High-Value Customer",
    SalesPerCustomer >= 2000, "Medium-Value Customer",
    "Low-Value Customer"
)
