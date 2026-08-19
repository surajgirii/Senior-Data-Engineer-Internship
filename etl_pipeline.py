import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(source_url: str) -> pd.DataFrame:
    """Extracts raw dataset from a remote URL endpoint."""
    logging.info("Starting data extraction...")
    df = pd.read_csv(source_url)
    logging.info(f"Successfully extracted {len(df)} raw records.")
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans, validates, and transforms raw trip data."""
    logging.info("Starting data transformation...")
    
    # 1. Handle Missing Values
    df = df.dropna(subset=['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count'])
    
    # 2. Datetime Casting & Derived Metrics
    df['pickup_dt'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_dt'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    
    # Feature Engineering: Calculate Duration in Minutes
    df['trip_duration_min'] = (df['dropoff_dt'] - df['pickup_dt']).dt.total_seconds() / 60.0
    
    # 3. Anomaly Filtering
    df = df[(df['trip_distance'] > 0) & (df['fare_amount'] > 0)]
    df = df[df['trip_duration_min'].between(1, 180)] # Valid trips between 1 min and 3 hrs
    
    # 4. Deduplication
    df = df.drop_duplicates(subset=['pickup_dt', 'dropoff_dt', 'passenger_count', 'fare_amount'])
    
    logging.info(f"Transformation complete. Remaining valid records: {len(df)}.")
    return df

def load_data(df: pd.DataFrame, db_uri: str, table_name: str):
    """Loads transformed dataframe into target PostgreSQL database table."""
    logging.info("Connecting to target database...")
    engine = create_engine(db_uri)
    
    logging.info(f"Loading data into table '{table_name}'...")
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False, chunksize=1000)
    logging.info("Data successfully loaded into database!")

if __name__ == "__main__":
    # Endpoint and Database Configurations
    DATA_URL = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2023-01.csv"
    DATABASE_URI = "postgresql://postgres:password@localhost:5432/nyctaxi_db"
    
    # Pipeline Execution Flow
    raw_data = extract_data(DATA_URL)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, DATABASE_URI, "fact_taxi_trips")
