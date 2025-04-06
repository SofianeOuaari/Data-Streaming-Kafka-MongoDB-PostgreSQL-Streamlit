# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app
COPY . /app/

# Install Kafka Python library
RUN pip install --no-cache-dir -r requirements.txt


# Command to wait for Kafka to be ready and then start the consumer
CMD ["python","-u" ,"consumer_covid_data.py"]