CREATE DATABASE IF NOT EXISTS ecommerce_dt;

USE ecommerce_dt;

-- Original source table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT,
    customer VARCHAR(100),
    amount DECIMAL(10,2)
);

-- Final destination table
CREATE TABLE IF NOT EXISTS orders_cleaned (
    order_id INT,
    customer VARCHAR(100),
    amount DECIMAL(10,2),
    tax DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    order_category VARCHAR(50)
);
