import pandas as pd
import os
from sqlalchemy import create_engine
DB_SERVER = os.environ.get('DB_SERVER')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

con = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
df = pd.read_sql('SELECT order_status,COUNT(*) FROM orders GROUP BY order_status', con)
print(df)
