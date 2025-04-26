Red Sox Game Tracker (ETL + Grafana Dashboard)

About
This project tracks the Boston Red Sox 2025 season by extracting game data using the MLB StatsAPI, storing it in a PostgreSQL database, and visualizing team performance using Grafana.

Features
- ETL Pipeline (Python) using MLB StatsAPI
- PostgreSQL Database Storage
- Grafana Dashboards:
  - Wins and Losses
  - Run differential over time
  - Home vs Away Records
  - Opponent Win/Loss Analysis

How It Works
1. Python ETL script extracts and loads game data into PostgreSQL.
2. Grafana visualizes real-time game performance.
3. PostgreSQL automatically updates as more games are played.

Setup
- Python 3.13
- PostgreSQL
- Grafana

Author
- Built by Miguel Luyao
