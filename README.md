# PySpark E-commerce Order Analytics Pipeline
This project demonstrates a basic data engineering pipeline using PySpark to process and analyze simulated e-commerce order data. It showcases data ingestion, transformation, business logic implementation, and output generation.
## Features
- Cleans and transforms raw order data
- Computes business metrics: top-selling products, total revenue, repeat customers
- Uses PySpark DataFrame API and SQL
- Modular script structure for easy expansion
## Technologies
- Python
- PySpark
- Hive-compatible output (optional)
- Git for version control
## How to Run
1. Clone the repo:
   git clone https://github.com/sudhanyagandhi/pyspark-ecommerce-analytics.git
   cd pyspark-ecommerce-analytics
2. Place raw CSV files in the `data/` folder.
3. Run the script:
   spark-submit scripts/order-pipeline.py
## To Do
- Add logging and performance tracking
- Extend to cloud platforms (GCP/Azure)
- Add unit tests
## Author
Sudhanya — Senior Data Engineer
