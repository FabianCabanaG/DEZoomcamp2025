FROM python:3.9.1

RUN pip install pandas sqlalchemy psycopg2 
RUN apt get wget
#Not installing wget
WORKDIR /app/pipelines

COPY ingest_data.py ingest_data.py

# ENTRYPOINT ["bash"] -- bash default on run
ENTRYPOINT [ "python","ingest_data.py" ]