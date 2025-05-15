import numpy as np
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable, KafkaError
from pymongo import MongoClient
from sqlalchemy import create_engine, inspect
from sqlalchemy import text
import math
import json
import time
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


def get_db_engine():
    return create_engine(
        "postgresql://{}:{}@{}/{}".format(
            "postgres", "postgres", "postgres:5432", "covid_db"
        )
    )


def return_insert_query(message):
    val = message.value
    date = val["Date"]
    confirmed = val["Confirmed"]
    recovered = val["Recovered"]
    deaths = val["Deaths"]
    increase_rate = val["Increase rate"]
    if date == None:
        date = "NULL"
    if confirmed == None:
        confirmed = "NULL"
    if recovered == None:
        recovered = "NULL"
    if deaths == None:
        deaths = "NULL"
    if np.isnan(increase_rate):
        increase_rate = "NULL"
    insert_query = f"""INSERT INTO covid.covid_data (DATE, Confirmed, Recovered, Deaths, Increase_Rate) VALUES ('{date}', {confirmed}, {recovered}, {deaths}, {increase_rate})"""

    return insert_query


connection_not_successful = True

while connection_not_successful:
    try:
        consumer = KafkaConsumer(
            "covid-data",  # Topic to subscribe to
            bootstrap_servers="kafka:29092",  # Connect to the Kafka broker
            auto_offset_reset="earliest",  # Start reading at the beginning of the topic
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(
                v.decode("utf-8")
            ),  # Deserialize JSON data
        )
        print("Connection to Kafka broker successful!")
        connection_not_successful = False

        mongo_client = MongoClient(
            "mongodb://mongodb:27017/", username="mongo", password="mongopass"
        )
        print("Connection to MongoDB successful!")
        db = mongo_client.covid_data
        col = db.covid_data

    except (NoBrokersAvailable, KafkaError) as e:
        print(e)
        time.sleep(2)

while True:
    try:
        db_engine = get_db_engine()
        db_engine_conn = db_engine.connect()
        if db_engine:
            print("|||||| Connected to PostgreSQL database ||||||")
            break
    except Exception as e:
        LOGGER.warning(
            f"++++ Retrying connection to the database because of the issue {str(e)}++++"
        )

print("Starting Kafka consumer...")
try:
    for message in consumer:
        # Log received message
        logging.info(f"Received: {message.value}")

        # Insert into MongoDB
        try:
            col.insert_one(message.value)
            logging.info("Data inserted into MongoDB")
        except Exception as e:
            logging.error(f"Failed to insert data into MongoDB: {e}")
            continue

        # Prepare and execute PostgreSQL insertion
        try:
            insert_query = return_insert_query(message)

            # Transaction management for PostgreSQL
            with db_engine.connect() as connection:
                with connection.begin():
                    connection.execute(text(insert_query))
                    logging.info("Data inserted into PostgreSQL")

                # Optional: Fetch and print rows (for debugging)
                result = connection.execute(text("SELECT * FROM covid.covid_data"))
                rows = result.fetchall()
                logging.info(f"Fetched rows: {rows}")
        except Exception as e:
            logging.error(f"Failed to insert data into PostgreSQL: {e}")
            continue

        # Inspect schema (optional debugging)
        try:
            inspection = inspect(db_engine)
            schemas = inspection.get_schema_names()
            logging.info(f"Available schemas: {schemas}")
        except Exception as e:
            logging.error(f"Failed to inspect database schema: {e}")
except Exception as e:
    logging.critical(f"Critical error in Kafka consumer loop: {e}")
finally:
    logging.info("Kafka consumer stopped.")
