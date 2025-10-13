# Sales Analysis Dashboard

This repository contains an interactive Sales Analysis Dashboard designed to provide comprehensive insights into sales performance across various dimensions. Built using Power BI, this dashboard empowers users to track key metrics, identify trends, and make data-driven decisions.

##  Features

* **Key Performance Indicators (KPIs):** At-a-glance view of Total Sales, Profit %, Total Orders, and Quantity Sold.
* **Sales by Segment:** Breakdown of sales performance across different customer segments (e.g., Home Office, Consumer, Corporate).
* **Sales by Category:** Analysis of sales distribution among product categories (e.g., Office Supplies, Technology, Furniture).
* **Sales by Region:** Geographical sales performance segmented by regions (e.g., South, West, Central, East).
* **Sales by Payment Mode:** Understanding customer payment preferences (e.g., COD, Online, Cards).
* **Total Sales by State:** Detailed sales performance for top-performing states (e.g., California, New York, Texas).
* **Order by State (Map View):** Visual representation of order distribution across the United States.
* **Order by Ship Mode:** Analysis of orders based on shipping methods (e.g., Standard Class, Second Class, First Class, Same Day).
* **Time-based Filtering:** Interactive filters for years (e.g., 2019, 2020) to analyze sales trends over time.

## Getting Started

To view and interact with this dashboard, you will need Microsoft Power BI Desktop or Power BI Service.

### Prerequisites

* **Power BI Desktop:** Download and install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
* **Power BI Service Account (Optional):** If you wish to publish and share the dashboard online.
*  * Use the year filters at the top to change the reporting period.

##  Data Source

The dashboard is currently connected to an internal dataset. For data refresh, ensure you have access to the original data source. Typically, this would be a database (SQL Server, Azure SQL DB), an Excel file, or a cloud service.

* **Expected Data Schema:**
    * `SalesID`: Unique identifier for each sale.
    * `OrderDate`: Date of the order.
    * `ShipMode`: Shipping method (e.g., Standard Class).
    * `Segment`: Customer segment.
    * `Category`: Product category.
    * `Region`: Geographical region.
    * `State`: State of the customer/delivery.
    * `PaymentMode`: Method of payment.
    * `Sales`: Total revenue from the sale.
    * `Profit`: Profit generated from the sale.
    * `Quantity`: Number of units sold.
    * ... (add any other relevant columns used in the dashboard)
 
      <img width="1294" height="744" alt="image" src="https://github.com/user-attachments/assets/ded6e5f1-e439-435f-8297-b4e473b8ff46" />


