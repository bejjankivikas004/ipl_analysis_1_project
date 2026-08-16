# IPL Analysis – 

## 📌 Project Overview

The **IPL Analysis** project is a Data Engineering and Sports Analytics project focused on cleaning, transforming, storing, and analyzing Indian Premier League (IPL) match data.

An **ETL pipeline using Python, Pandas, and NumPy** is used to process raw CSV data. The cleaned data is stored in **MySQL** for SQL-based analysis, and **Matplotlib** is used to create visualizations and dashboards.

The project provides insights into **team wins, average runs per match, no-result matches, runs distribution, wickets per match, and high-scoring matches**.

---

## 🎯 Objectives

- Perform ETL activities using Python, Pandas, and NumPy.
- Clean and transform raw IPL datasets.
- Remove duplicate records and handle missing values.
- Apply business rules to maintain data quality.
- Store cleaned data in MySQL.
- Perform SQL-based IPL analytics.
- Identify teams with the highest number of wins.
- Calculate average runs per match.
- Analyze matches with no result.
- Analyze runs and wickets distribution.
- Identify high-scoring matches.
- Create visualizations using Matplotlib.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **MySQL**
- **MySQL Connector/Python**
- **Matplotlib**
- **Seaborn**
- **Git**
- **GitHub**

---

## 🔄 ETL Pipeline Flow

```text
CSV Files (Dirty Data)
        ↓
Python ETL (Pandas + NumPy)
        ↓
Data Cleaning & Transformation
  - Deduplication
  - Null Handling
  - Data Validation
  - Business Rules
        ↓
Clean MySQL Tables
        ↓
SQL Analytics
        ↓
Matplotlib Visualizations
        ↓
IPL Analysis Dashboard
