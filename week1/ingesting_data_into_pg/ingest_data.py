#!/usr/bin/env python
# coding: utf-8
from time import time 
import pandas as pd
from sqlalchemy import create_engine
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name,iterator=True, chunksize=100000)
    df  = next(df_iter)
    df['tpep_dropoff_datetime'] = pd.to_datetime(df.tpep_dropoff_datetime)
    df['tpep_pickup_datetime'] = pd.to_datetime(df.tpep_pickup_datetime)

    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')
    df.to_sql(name=table_name,con=engine,if_exists='append')

    while True:
        t_start = time()
        df  = next(df_iter)
        df['tpep_dropoff_datetime'] = pd.to_datetime(df.tpep_dropoff_datetime)
        df['tpep_pickup_datetime'] = pd.to_datetime(df.tpep_pickup_datetime)
        df.to_sql(name=table_name,con=engine,if_exists='append')
        t_end = time()
        time_taken = t_end - t_start
        print(f'inserted another chunk... {time_taken}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='user for postgress')
    parser.add_argument('--password', help='password for postgress')
    parser.add_argument('--host', help='host for postgress')
    parser.add_argument('--port', help='port for postgress')
    parser.add_argument('--db', help='db for postgress')
    parser.add_argument('--table_name', help='table_name for postgress')
    parser.add_argument('--url', help='url for postgress')
    args = parser.parse_args()
    main(args)