# End-to-End ETL Pipeline Development

A production-grade Extract, Transform, Load (ETL) pipeline built with Python and PostgreSQL to process, clean, and analyze high-volume NYC Yellow Taxi transactional ride-hailing data.

---

## 📌 Project Overview
This project demonstrates an automated ETL pipeline that ingests raw taxi trip records from a public cloud endpoint, performs robust data cleansing, filters statistical anomalies, derives business metrics (e.g., trip duration in minutes), and loads structured records into a relational database for business intelligence reporting.

---

## 🏗️ Architecture & Pipeline Flow

[ Public CSV / AWS S3 ]
│
 (Extract: HTTP Streaming)
[ Raw Pandas DataFrames ]
│
 (Transform: Data Cleaning & Feature Engineering)
[ Cleaned & Standardized Data ]
│
 (Load: SQLAlchemy Batch Ingestion)
[ PostgreSQL Database (fact_taxi_trips) ]


### Key Workflow Stages:
1. **Extract:** Stream raw CSV partitions from HTTP endpoints directly to memory without local disk overhead.
2. **Transform:**
   - Impute missing values and enforce temporal bounds.
   - Typecast dates (`datetime64[ns]`) and compute dynamic attributes (`trip_duration_min`).
   - Remove negative fare anomalies, zero-distance records, and extreme duration outliers (> 3 hours).
   - Deduplicate using compound key checks.
3. **Load:** Bulk load cleaned records into PostgreSQL using `SQLAlchemy` batch insertion (`chunksize=1000`).

---

## 🛠️ Tech Stack & Prerequisites
- **Language:** Python 3.9+
- **Data Libraries:** `pandas`, `numpy`
- **Database Connection:** `SQLAlchemy`, `psycopg2-binary`
- **Target Database:** PostgreSQL 15+

## Project File Structure
Senior-Data-Engineer-Internship/
├── etl_pipeline.py
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
