Real-Time Product Event Monitoring Pipeline
====================================================
What does this program do?
This project simulates real-time product interaction events (like "view", "add to cart", "purchase") and processes them using Kafka, Spark Structured Streaming, ClickHouse, and Grafana, all orchestrated with Docker Compose. It is ideal for real-time analytics use cases in e-commerce or product behavior tracking.

---
Prerequisites
Docker Desktop installed and running on your machine
👉 Download Docker for Mac/Windows

🪜 Step-by-Step Instructions
📥 1. Download the Code
Go to the GitHub repository

Click the green “Code” button → select “Download ZIP”

Unzip the downloaded file to your Desktop or any folder

2. Install Dependencies
Your project uses multiple components and technologies, each with its own dependencies. Here's how to install them.

✅ A. Python Dependencies (for generate.py)
This script needs the Kafka Python client:
In Terminal, install:
bash
Copy
Edit
pip3 install kafka-python
This lets generate.py send events to Kafka.

✅ B. Apache Spark Dependencies (for app.py)
Spark is run inside a Docker container (Bitnami Spark image), which comes pre-installed with:
PySpark
Required libraries for structured streaming
If you want to run it locally (without Docker), you would need:
bash
Copy
Edit
brew install apache-spark
✅ C. Docker Services (for the rest of the stack)
Docker handles all services (Kafka, Spark, ClickHouse, Grafana), so you don’t need to install these separately.
You just need to install:

📦 Docker Desktop:
👉 Download Docker for Mac/Windows
Once installed, you're ready to run everything using:
bash
Copy
Edit
docker-compose up --build
This automatically sets up all internal dependencies via Docker images.

📦 3. What Each Component Does
generate.py
Simulates random product interaction events and sends them to a Kafka topic.

app.py (Spark App)
Consumes Kafka stream, parses the data, and writes it to ClickHouse.
ClickHouse
Fast, columnar database used to store processed event data.
Grafana
Visualizes real-time data from ClickHouse via preconfigured dashboards.
Docker Compose
Launches all services (Kafka, Spark, ClickHouse, Grafana) in one command.

▶️ 4. Run the Project
Open Terminal

Navigate to the project folder:
bash
Copy
Edit
cd ~/Desktop/real-time-product-monitoring
Start the entire pipeline:
bash
Copy
Edit
docker-compose up --build

🌐 5. Access the Services
Grafana Dashboard:
http://localhost:3000
Login: admin / admin

ClickHouse Web UI (optional):
http://localhost:8123

📊 6. View Real-Time Product Events
Open Grafana → select the ClickHouse data source

View dashboards to monitor product activity in real-time


👏 Credits

Built by **Harika Kuruba**
