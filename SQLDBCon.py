def main():
    import pyodbc as po

    server = 'localhost,1433'
    database = 'itversity_retail_db'
    username = 'retail_user'
    password = 'itversity'
    cnxn = po.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT *FROM users;")
    row = cursor.fetchone()
    while row:
        print(row[1])
        row = cursor.fetchone()

if __name__ == "__main__":
    main()