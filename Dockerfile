FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_HOST=db

# Run SQL scripts to create tables inside container
RUN apt-get update && apt-get install -y default-mysql-client
COPY init.sql /docker-entrypoint-initdb.d/

# Run app.py
CMD ["python", "run.py"]