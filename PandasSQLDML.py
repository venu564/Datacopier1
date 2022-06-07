def main():
    import pyodbc as po
    import pandas as pd
    from sqlalchemy import create_engine
    engine = create_engine('mssql+pyodbc://retail_user:itversity@localhost:1433/itversity_retail_db')
    user = [
        {'user_first_name' : 'Tom', 'user_last_name' : 'Jerry'},
        {'user_first_name' : 'Timon', 'user_last_name' : 'Pumba'}
    ]
    df = pd.DataFrame(user)

    # parameters
    DB = {'servername': 'localhost',
          'database': 'itversity_retail_db',
          'port' : '1433',
          'user' : 'retail_user',
          'password' : 'itversity',
          'driver': 'driver=SQL Server'}

    # create the connection
    engine = create_engine('mssql+pyodbc://' + DB['user']+':'+DB['password']+'@'+DB['servername'] + ':'+DB['port']+'/' + DB['database'] + "?" + DB['driver'])
    print(engine)
    df.to_sql('users',engine, if_exists='append',index =False)
    print(pd.read_sql('SELECT*FROM users',engine))

if __name__=='__main__':
    main()
