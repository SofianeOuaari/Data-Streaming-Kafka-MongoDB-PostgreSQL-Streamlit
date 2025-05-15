# Data-Streaming-Kafka-MongoDB-PostgreSQL-Streamlit
📊 Data Streaming Pipeline: Kafka + MongoDB + PostgreSQL + Streamlit
A complete data streaming pipeline using time-series COVID-19 data. The project ingests data through Apache Kafka, stores it in both MongoDB (NoSQL) and PostgreSQL (SQL), and visualizes insights via an interactive Streamlit dashboard. Includes automated EDA with YData Pandas Profiling.


## Project Overview 
- Sending data from a Kafka Producer. 
- Receiving the data through a Kafka Consumer. 
- Using Apache Kafka as the messaging backbone for the data streaming. 
- Running all components in isoaled Docker containers. 


## Dataset
The data used for this project is downloaded from Kaggle entitled "Real-time Covid 19 Data" (link: https://www.kaggle.com/datasets/gauravduttakiit/covid-19). The exact filename of the dataset used is: worldwide-aggregate.csv

## Project structure 
```bash
.
├── consumer
│   ├── consumer_covid_data.py
│   ├── Dockerfile
│   └── requirements.txt
├── dashboard
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yaml
├── init.sql
├── producer
│   ├── data
│   │   └── worldwide-aggregate.csv
│   ├── Dockerfile
│   ├── requirements.txt
│   └── stream_covid_data.py
└── README.md
```
## Installation
1. Clone the repository:
```bash
 git clone https://github.com/SofianeOuaari/Real-Time-Time-Series-Covid-Data-Streaming-using-Python-Docker-and-Kafka.git
```

2. Run the containers: 
```bash
 docker-compose up --build
```
3. To stop the containers: 
```bash
docker-compose down
```

4. To stop the containers with their volumes: 
```bash
docker-compose down -v
```

## Kafka UI 


You can access the Kafka UI by visiting: ``` http://localhost:8080/ ```

## Mongo Express

You can access the Mongo Express UI by visiting: ``` http://localhost:8081 ```
## Streamlit Dashboard 

You can acces the Streamlit dashboard by visiting: ``` http://localhost:8502/ ```

## Pg Admin
You can access the PostgreSQL Admin page by visiting: ``` http://localhost:5000/ ```