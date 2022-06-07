def main():
    import pyodbc as po
    import pandas as pd

    server = 'localhost,1433'
    database = 'itversity_retail_db'
    username = 'retail_user'
    password = 'itversity'
    cnxn = po.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = "SELECT*FROM users"
    df = pd.read_sql(query,cnxn)
    print(df)
if __name__ == "__main__":
    main()