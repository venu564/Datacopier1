from WriteDataPS import read_from_json,write_to_db
import os
import pandas as pd
#from sqlalchemy import create_engine
Root_dir = os.environ.get('BASE_FOLDER')
folders = os.listdir(Root_dir)
Serv = os.environ.get('DB_SERVER')
DB = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
pwd = os.environ.get('DB_PASS')
port = os.environ.get('DB_PORT')

con = f'postgresql://{user}:{pwd}@{Serv}:{port}/{DB}'
#con = create_engine(f'mssql+pyodbc://{user}:{pwd}@{Serv}:{port}/{DB}?Driver=SQL Server')

for folder in folders:
    file_enu = read_from_json(Root_dir,folder)
    for df in file_enu:
        write_to_db(df,con,folder)