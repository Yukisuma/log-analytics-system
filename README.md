# Log Analytics System

## Overview
A scalable log analytics system built using Flask and PostgreSQL to efficiently store, search, and analyze large volumes of logs.

---

## Features
- Full-text search using PostgreSQL (GIN indexing)
- Pagination for efficient data retrieval
- Time-based filtering
- Log level filtering (INFO, ERROR, WARNING)
- Handles 100K+ log records efficiently

---

## Tech Stack
- Python (Flask)
- PostgreSQL
- psycopg2

---

## Architecture
- Logs are stored in PostgreSQL  
- Indexed using full-text search (GIN)  
- Flask API handles querying and filtering  
- Supports scalable querying with pagination  

---

## API Endpoints

### Get Logs (Paginated)

/logs?page=1&limit=5


 ###  Sample Output:
```json
[
  {
    "id": 1,
    "timestamp": "2026-04-01 10:00:00",
    "level": "INFO",
    "message": "Server started"
  }
]
```

### Search Logs
- /search?keyword=database


### Filter by Level
- /search?level=ERROR

### Combined Filters
- /search?keyword=database&level=ERROR

### Time Filter
- /search?start=2026-04-01 10:00:00&end=2026-04-01 10:10:00

### How to Run

1. Clone the repository

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Database Setup
- Install PostgreSQL and open pgAdmin
- Create a database:
```sql
CREATE DATABASE logs_db;
```
- Create table:
```sql
CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    level TEXT,
    message TEXT
);
```
- sample data using:
python `load_logs.py`

5. Run
python `app.py`

## Environment Variables :

Create a `.env` file:

DB_NAME=logs_db  
DB_USER=postgres  
DB_PASSWORD=your_password  

### Future Improvements
- Real-time log streaming
- Dashboard UI
- Distributed log storage


### Author
Yubhashana Shinde