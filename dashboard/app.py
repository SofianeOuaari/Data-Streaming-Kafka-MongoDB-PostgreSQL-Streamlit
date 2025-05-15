import streamlit as st
from sqlalchemy import create_engine, inspect, text
import psycopg2
import time
import logging
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

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


def get_db_connection():
    conn = psycopg2.connect(
        dbname="covid_db",
        user="potsgres",
        password="postgres",
        host="postgres",  # PostgreSQL container name as hostname
        port="5432",
    )
    return conn


st.title("Covid-19 Data Dashboard")

st.video("https://www.youtube.com/watch?v=BtN-goy9VOY")
time.sleep(25)

while True:
    try:
        db_engine = get_db_engine()
        db_engine_conn = db_engine.connect()
        if db_engine:
            print("|||||| Connected to PostgreSQL database ||||||")
            st.write("Connected to the database")
            break
    except Exception as e:
        LOGGER.warning(
            f"++++ Retrying connection to the database because of the issue {str(e)}++++"
        )


placeholder = st.empty()
while True:
    with placeholder.container():
        container = st.empty()
        df = pd.read_sql_query("SELECT * FROM covid.covid_data", con=db_engine_conn)
        st.dataframe(df)
        profile = ProfileReport(df, title="Profiling Report")
        st_profile_report(profile)
        time.sleep(30)
