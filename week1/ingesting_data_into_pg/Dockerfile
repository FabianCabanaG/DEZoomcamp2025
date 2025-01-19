FROM python:3.9

RUN pip install pandas
WORKDIR /app/pipelines

COPY pipeline.py pipeline_inside.py

# ENTRYPOINT ["bash"] -- bash default on run
ENTRYPOINT [ "python","pipeline_inside.py" ]

# commands to set pg and pgadmin on windows 
winpty docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v //c/Users/facab/Documents/bootcamp/week1/ingesting_data_into_pg/data/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 --network=pgnetwork --name pg-database postgres:13

winpty docker run -it  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com"  -e PGADMIN_DEFAULT_PASSWORD="root"  -p 8080:80  --network=pgnetwork dpage/pgadmin4

#execute ingest data
python ingest_data.py  --user=root --password=root --host=localhost --port=5324 --db=ny_taxi --table_name=yellow_taxi_data --url=${URL}