# ⚡ Real-Time Product Event Monitoring Pipeline

A complete real-time data pipeline using **Kafka**, **Spark Structured Streaming**, **ClickHouse**, and **Grafana**.  
This project simulates product activity events and visualizes them in real-time dashboards.

---

## 🚀 Tech Stack

- Kafka (event ingestion)  
- Spark Structured Streaming (processing)  
- ClickHouse (storage)  
- Grafana (visualization)  
- Docker (local orchestration)

---

## 📁 Project Structure

```
real-time-product-monitoring/
├── clickhouse-init/
│   └── create_table.sql
├── data-generator/
│   └── generate.py
├── spark-app/
│   └── app.py
├── grafana-provisioning/
│   └── grafana-clickhouse.yaml
├── docker-compose.yml
├── .gitignore
├── README.md
```

---

## 🛠️ How to Run

1. **Start the full stack:**

```bash
docker-compose up --build
```

2. **Access services:**

- Kafka: `localhost:9092`  
- ClickHouse: `localhost:8123`  
- Grafana: `localhost:3000`

3. **Open Grafana**  
Login with:
- **Username**: `admin`  
- **Password**: `admin`  

→ View dashboards in real-time 📊

---

## 👏 Credits

Built by **Harika Kuruba**
