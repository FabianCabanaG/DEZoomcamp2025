# commands to run pg and pgadmin on windows (Had to use winpty)
winpty docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v //c/Users/facab/Documents/bootcamp/week1/ingesting_data_into_pg/data/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 --network=pgnetwork --name pg-database postgres:13

winpty docker run -it  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com"  -e PGADMIN_DEFAULT_PASSWORD="root"  -p 8080:80  --network=pgnetwork dpage/pgadmin4

# execute ingest_data (I used urllib.request instead of wget.)

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python ingest_data.py  --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table_name=yellow_taxi_data --url=${URL}

# Execute dockerized pipeline ingest_data

docker build -t taxi:v1

docker run taxi:v1 --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table_name=yellow_taxi_data --url=${URL}

docker run -v /d:/app taxi:v1 --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table_name=yellow_taxi_data --url=${URL}
