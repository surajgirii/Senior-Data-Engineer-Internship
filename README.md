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
### Key Workflow Stages:
1. **Extract:** Stream raw CSV partitions from HTTP endpoints directly into memory without local disk storage overhead.
2. **Transform:**
   - Handle missing values and enforce temporal consistency.
   - Typecast fields (`datetime64[ns]`) and calculate derived attributes (`trip_duration_min`).
   - Filter out statistical anomalies (negative fares, zero-distance trips) and extreme duration outliers (> 3 hours).
   - Perform deduplication using compound key logic.
3. **Load:** Bulk-load cleaned output into PostgreSQL using `SQLAlchemy` transactional batch insertion (`chunksize=1000`).

---

## 🛠️ Tech Stack & Prerequisites
- **Language:** Python 3.9+
- **Data Processing:** `pandas`, `numpy`
- **Database Connection:** `SQLAlchemy`, `psycopg2-binary`
- **Target Database:** PostgreSQL 15+

---

## 📂 Repository Structure


├── etl_pipeline.py    # Main ETL pipeline script
├── schema.sql         # PostgreSQL database DDL & indices
├── requirements.txt   # Python dependencies
├── .gitignore         # Files to exclude from version control
└── README.md          # Project documentation
