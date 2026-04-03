# Project Nebula: E-Commerce Data Orchestration

## Overview
Project Nebula is a hybrid data pipeline designed for a scaling online shop. It demonstrates the integration of local Python processing with cloud-scale Spark computing.

## Tech Stack
* **Orchestration:** Dagster (Software-Defined Assets)
* **Compute:** * *Local:* Python (Pandas) inside Docker for lightweight ETL.
    * *Cloud:* Databricks (PySpark) for heavy-duty analytics.
* **Infrastructure:** Docker & Docker Compose.
* **Language:** Python 3.11+

## Pipeline Architecture
1. **Ingest (Local):** Python scripts extract raw order JSONs/CSVs and perform schema validation.
2. **Transform (Databricks):** High-volume sales data is offloaded to Databricks for window functions and complex aggregations.
3. **Load:** Final silver/gold tables are prepared for BI tools.

## Getting Started
`docker-compose up -d`