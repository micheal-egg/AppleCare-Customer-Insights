# 🍎 AppleCare Customer Insights Platform

A data engineering and analytics project that simulates how AppleCare-style customer feedback can be ingested, cleaned, stored, and explored to surface actionable insights about customer support quality.

This project focuses on end-to-end data flow — from raw survey input → ETL pipeline → database → API → interactive dashboard.

## 📌 Project Overview

Customer support teams receive large volumes of qualitative feedback in the form of comments alongside structured metrics (ratings, regions, dates).

This project demonstrates how a data engineer can:

Transform raw survey data into a query-ready analytics dataset

Enforce data quality and validation

Expose clean data via a REST API

Enable fast, flexible exploration through a lightweight dashboard

The design mirrors how an AppleCare Customer Insights team might analyze post-support feedback at scale.

## 🛠️ Technologies Used

Python (ETL, API)

Pandas (Data cleaning & transformation)

SQLite (Analytics database)

Flask (REST API & server-side rendering)

HTML / CSS / JavaScript (Dashboard UI)

Git & GitHub (Version control)

## 🚀 How to Run the Project

1. Clone the repo 

    ``` 
    git clone https://github.com/your-username/AppleCare-Customer-Insights.git
    cd AppleCare-Customer-Insights
    ```

2. Create & Activate Virtual Environment 

    ```
    python -m venv venv
    venv\Scripts\activate      
    ```

3.  Install Requirements 

    ``` pip install -r requirements.txt ```

4. Run ETL Pipeline 

    ``` python -m etl.load  ``` 

5. Start the Flask app 

    ` python app/api.py `

6. Open in Browser 

    ` http://127.0.0.1:5000 `


## 📈 What This Project Demonstrates

Practical data engineering fundamentals

ETL design and validation logic

API-driven analytics access

Translating raw data into decision-ready insights

AppleCare-style customer experience analytics
     

