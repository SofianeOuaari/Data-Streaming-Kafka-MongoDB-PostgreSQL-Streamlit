# Data-Streaming-Kafka-MongoDB-PostgreSQL-Streamlit
📊 Data Streaming Pipeline: Kafka + MongoDB + PostgreSQL + Streamlit
A complete data streaming pipeline using time-series COVID-19 data. The project ingests data through Apache Kafka, stores it in both MongoDB (NoSQL) and PostgreSQL (SQL), and visualizes insights via an interactive Streamlit dashboard. Includes automated EDA with YData Pandas Profiling.


![alt text](attachments/Architecture_Workflow_MLOps.jpg)
## Project Overview 
- Sending data from a Kafka Producer. 
- Receiving the data through a Kafka Consumer. 
- Using Apache Kafka as the messaging backbone for the data streaming. 
- Running all components in isoaled Docker containers. 
- Analyzing the received using a ydata Profiling Report. 
- Update the Streamlit app each time new data is received.


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
 git clone https://github.com/SofianeOuaari/Data-Streaming-Kafka-MongoDB-PostgreSQL-Streamlit.git
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
![alt text](attachments/Kafka_UI.png)

## Mongo Express

You can access the Mongo Express UI by visiting: ``` http://localhost:8081 ```
![alt text](attachments/MongoDB_UI_1.png)
![alt text](attachments/MongoDB_UI_2.png)
## Streamlit Dashboard 

You can acces the Streamlit dashboard by visiting: ``` http://localhost:8502/ ```
![alt text](attachments/Ydata_Profiling_Summary.png)
![alt text](attachments/Streamlit_Dashboard_1.png)
![alt text](attachments/Streamlit_Dashboard_2.png)
![alt text](attachments/Streamlit_Dashboard_3.png)
![alt text](attachments/Streamlit_dashboard_4.png)
## Pg Admin
You can access the PostgreSQL Admin page by visiting: ``` http://localhost:5000/ ```
![alt text](attachments/PostgreSQL.png)