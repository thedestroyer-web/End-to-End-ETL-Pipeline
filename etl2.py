
# 1. IMPORTING LIBRARIES


import mysql.connector
import pandas as pd
from decimal import Decimal
import numpy as np



# 2. CONNECTING TO MYSQL DATABASE


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="**************",
    database="ecommerce_dt"
)

print("Connected to MySQL successfully!")



# 3. CREATING CURSOR


cursor = conn.cursor()



# 4. EXTRACTING DATA FROM MYSQL


query = "SELECT * FROM orders"
cursor.execute(query)


# Fetch all records returned by the query
rows = cursor.fetchall()

# Extract column names
columns = [column[0] for column in cursor.description]



# 5. CREATING PANDAS DATAFRAME


df = pd.DataFrame(rows, columns=columns)

print("\nEXTRACTED DATA:")
print(df)



# 6. CREATING ORIGINAL AND WORKING DATA


# Preserve original extracted data
raw_df = df.copy()

# Create a separate DataFrame for cleaning
cleaned_df = df.copy()



# 7. DATA INVESTIGATION-------------


print("\nDATA SHAPE:")
print(cleaned_df.shape)

print("\nCOLUMN NAMES:")
print(cleaned_df.columns)

print("\nDATA TYPES AND INFORMATION:")
cleaned_df.info()

print("\nSTATISTICAL SUMMARY:")
print(cleaned_df.describe())



# 8. MISSING VALUE INVESTIGATION


print("\nMISSING VALUE DETAILS:")
print(cleaned_df.isnull())

print("\nMISSING VALUE COUNT:")
print(cleaned_df.isnull().sum())



# 9. DUPLICATE INVESTIGATION--------


print("\nDUPLICATE RECORD DETAILS:")
print(cleaned_df.duplicated())

print("\nTOTAL DUPLICATE RECORDS:")
print(cleaned_df.duplicated().sum())


#. HANDLING DUPLICATE RECORDS-----------

cleaned_df = cleaned_df.drop_duplicates()

print("\nDATA AFTER REMOVING DUPLICATES:")
print(cleaned_df)


print("\nORIGINAL DATA:")
print(raw_df)

print("\nCURRENT CLEANED DATA:")
print(cleaned_df)

#REPLACING THE NULL VALUES  IN THE AMOUNT COLUMN WITH THE 0----------

cleaned_df["amount"]=cleaned_df["amount"].fillna(0)
print("\nDATA AFTER FILLING MISSING VALUES:")
print(cleaned_df)



# Calculate 10% tax on each order----------

cleaned_df["tax"] = cleaned_df["amount"] * Decimal("0.10")

print("\nDATA AFTER ADDING TAX COLUMN:")
print(cleaned_df)


#CALCULATE FINAL ORDER AMOUNT INCLUDING THE TAX AMOUNT -------

cleaned_df["total_amount"]=cleaned_df["amount"]+cleaned_df["tax"]
print("\n data after adding a calculating total amount")
print(cleaned_df)


#CATEGORIZE ORDERS BASED ON THEIR AMOUNT
cleaned_df["order_category"]=np.where(
    cleaned_df["amount"]>=500,
    "high value",
    "regular "
)

print("\n data after order categorization")
print(cleaned_df)


filtered_orders = cleaned_df.query(
    "amount >= 300 | order_category == 'High Value'"
)

print("\n getting the particular records by filtering with query function")
print(filtered_orders)


#  GROUPBY AND AGGREGATION


# 1. Calculate total sales for each customer
customer_sales = cleaned_df.groupby("customer")["amount"].sum()

print("\nTOTAL SALES BY CUSTOMER:")
print(customer_sales)


# 2. Calculate average order amount for each customer
customer_average = cleaned_df.groupby("customer")["amount"].mean()

print("\nAVERAGE ORDER AMOUNT BY CUSTOMER:")
print(customer_average)


# 3. Count the number of orders placed by each customer
customer_orders = cleaned_df.groupby("customer")["order_id"].count()

print("\nTOTAL ORDERS BY CUSTOMER:")
print(customer_orders)


# 4. Find the maximum order amount for each customer
customer_max = cleaned_df.groupby("customer")["amount"].max()

print("\nMAXIMUM ORDER AMOUNT BY CUSTOMER:")
print(customer_max)


# 5. Find the minimum order amount for each customer
customer_min = cleaned_df.groupby("customer")["amount"].min()

print("\nMINIMUM ORDER AMOUNT BY CUSTOMER:")
print(customer_min)


# . MULTIPLE AGGREGATIONS USING agg()


# Calculate multiple statistics in one operation
customer_summary = cleaned_df.groupby("customer").agg(
    total_sales=("amount", "sum"),
    average_sales=("amount", "mean"),
    maximum_order=("amount", "max"),
    minimum_order=("amount", "min"),
    total_orders=("order_id", "count")
)

print("\nCUSTOMER SALES SUMMARY:")
print(customer_summary)


#  GROUPBY WITH RESET_INDEX()


# Convert customer index back into a normal column
customer_summary = customer_summary.reset_index()

print("\nCUSTOMER SUMMARY AS DATAFRAME:")
print(customer_summary)


#  SORTING DATA USING sort_values()


# Sort orders by amount in ascending order (smallest first)
sorted_orders = cleaned_df.sort_values(
    by="amount",
    ascending=True
)

print("\nORDERS SORTED BY AMOUNT (ASCENDING):")
print(sorted_orders)


# Sort orders by amount in descending order (largest first)
sorted_orders = cleaned_df.sort_values(
    by="amount",
    ascending=False
)

print("\nORDERS SORTED BY AMOUNT (DESCENDING):")
print(sorted_orders)



#  COUNTING VALUES USING value_counts()

# Count how many orders belong to each category
category_counts = cleaned_df["order_category"].value_counts()
category_ncounts = cleaned_df["order_category"].nunique()

print("\nORDER CATEGORY COUNTS:")
print(category_counts)
print(category_ncounts)


# Count how many orders each customer has placed
customer_counts = cleaned_df["customer"].value_counts()

print("\nCUSTOMER ORDER COUNTS:")
print(customer_counts)



#  CHANGING DATA TYPES USING astype()


# Convert order_id into integer type
cleaned_df["order_id"] = cleaned_df["order_id"].astype("int64")

print("\nDATA TYPES AFTER CONVERSION:")
print(cleaned_df.dtypes)



#  RENAMING COLUMNS USING rename()


# Create a separate DataFrame for demonstration
renamed_df = cleaned_df.rename(
    columns={
        "customer": "customer_name",
        "amount": "order_amount"
    }
)

print("\nDATA AFTER RENAMING COLUMNS:")
print(renamed_df)

# 22. REPLACING VALUES USING replace()


# Standardize customer names
# Replace lowercase names with properly capitalized names

cleaned_df["customer"] = cleaned_df["customer"].replace({
    "amit": "Amit",
    "priya": "Priya",
    "rahul": "Rahul"
})

print("\nDATA AFTER REPLACING VALUES:")
print(cleaned_df)



# . REMOVING COLUMNS USING drop()


# Creating  a separate DataFrame
# Remove the tax column from this separate DataFrame

without_tax_df = cleaned_df.drop(
    columns=["tax"]
)

print("\nDATA AFTER REMOVING TAX COLUMN:")
print(without_tax_df)



#  APPLYING CUSTOM FUNCTIONS USING apply()


# Defining a function to categorize order amounts

def classify_order(amount):

    if amount >= 500:
        return "High Value"

    else:
        return "Regular"


# Apply the function to every value in amount column
cleaned_df["order_category"] = cleaned_df["amount"].apply(
    classify_order
)

print("\nDATA AFTER APPLYING CUSTOM FUNCTION:")
print(cleaned_df)



# . MAPPING VALUES USING map()


# Creating  a dictionary to map customer names to customer IDs

customer_mapping = {
    "Amit": 1,
    "Priya": 2,
    "Rahul": 3
}

# Create a new customer_id column using the mapping
cleaned_df["customer_id"] = cleaned_df["customer"].map(
    customer_mapping
)

print("\nDATA AFTER CUSTOMER MAPPING:")
print(cleaned_df)


# . COMBINING DATAFRAMES USING merge()


# Creating  a sample customer information DataFrame

customer_info = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "city": ["Mumbai", "Pune", "Nashik"]
})

# Combining  order data with customer information
merged_df = cleaned_df.merge(
    customer_info,
    on="customer_id",
    how="left"
)

print("\nDATA AFTER MERGING:")
print(merged_df)
print(cleaned_df)


#  COMBINING DATAFRAMES USING concat()


# Create a small sample DataFrame
additional_orders = pd.DataFrame({
    "order_id": [105, 106],
    "customer": ["Amit", "Priya"],
    "amount": [600, 900]
})

# Combining  two DataFrames row-wise
combined_df = pd.concat(
    [cleaned_df, additional_orders],
    ignore_index=True
)

print("\nDATA AFTER CONCATENATION:")
print(combined_df)
print(cleaned_df)



# . FINAL DATA VALIDATION


# Checking  final number of rows and columns
print("\nFINAL DATA SHAPE:")
print(cleaned_df.shape)

# Checking  missing values
print("\nFINAL MISSING VALUE COUNT:")
print(cleaned_df.isnull().sum())

# Checking  duplicate records
print("\nFINAL DUPLICATE COUNT:")
print(cleaned_df.duplicated().sum())

# Checking  final data types
print("\nFINAL DATA TYPES:")
print(cleaned_df.dtypes)

print("\nPANDAS TRANSFORMATION COMPLETED!")

load_df=cleaned_df[
    [
        "order_id",
        "customer",
        "amount",
        "tax",
        "total_amount",
        "order_category"
    ]
]

print(load_df)

records=[tuple(row)
         for row in load_df.itertuples(index=False,name=None)]

print(records)

# SQL INSERT query
insert_query = """
INSERT INTO orders_cleaned
(order_id, customer, amount, tax, total_amount, order_category)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Inserting  all records into MySQL
cursor.executemany(insert_query, records)

# Saving  changes permanently
conn.commit()

print("Data successfully loaded into MySQL!")