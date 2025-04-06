# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the producer script and the wait-for-it script into the container
COPY stream_covid_data.py /app/

RUN mkdir data

COPY data/ /app/data/
COPY requirements.txt /app/

# Install Kafka Python library
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u" ,"stream_covid_data.py"]
