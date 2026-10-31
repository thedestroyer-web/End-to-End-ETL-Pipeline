
# End-to-End-ETL-Pipeline
An ETL Pipeline using the Python,Pandas and MYSQL

## Project Overview

This project demonstrates a beginner-level end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, NumPy and MySQL.

The objective is to extract data from an existing MySQL database, clean and transform it using Python, and load the processed data into a separate MySQL destination table.

## Project Objective

To understand how data moves from a source database through Python-based transformations into a destination database.

## Technologies Used

- Python
- Pandas
- NumPy
- MySQL
- MySQL Connector

## ETL Workflow

### 1. Extract
- Connected Python to MySQL using mysql.connector.
- Retrieved records from the source `orders` table.
- Loaded the extracted data into a Pandas DataFrame.

### 2. Transform
- Inspected the dataset.
- Handled missing values.
- Removed duplicate records.
- Created new columns such as tax and total_amount.
- Categorized orders based on their amount.

### 3. Load
- Converted the transformed DataFrame into records.
- Inserted the processed records into the MySQL destination table using executemany().
- Committed the changes to the database.

## Database Tables

**Source Table:** `orders`

Contains the original order records.

**Destination Table:** `orders_cleaned`

Contains the cleaned and transformed records.

## Project Structure

```text
End-to-End-ETL-Pipeline/
│
├── README.md
├── etl_pipeline.py
├── requirements.txt
│
└── sql/
    └── create_tables.sql

Installation
Install the required Python libraries:
pip install -r requirements.txt
How to Run
Install MySQL and create the database and tables using sql/create_tables.sql.
Update the MySQL connection credentials in the Python script.
Run the ETL pipeline:
python etl_pipeline.py
Key Learning
Through this project, I learned how to connect Python with MySQL, extract database records, perform data cleaning and transformations using Pandas, and load processed data back into MySQL.
Author
Data Science Student | Aspiring Data Engineer

