def read_from_json(Root_Dir, folder):
    import os
    import pandas as pd
    file_name = os.listdir(f'{Root_Dir}/{folder}')[0]
    fp = f'{Root_Dir}/{folder}/{file_name}'
    file_enu = pd.read_json(fp,lines=True, chunksize=1000)
    return file_enu

def write_to_db(df,con,folder):
    df.to_sql(folder,con, if_exists='append',index=False)

if __name__=="__main__":
    import os
    import pandas as pd
    from sqlalchemy import create_engine
    Root_dir = os.environ.get('BASE_FOLDER')
    folder = os.environ.get('TABLE_NAME')
    file_enu = read_from_json(Root_dir,folder)

    Serv = os.environ.get('DB_SERVER')
    DB = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    pwd = os.environ.get('DB_PASS')
    port = os.environ.get('DB_PORT')
    con = f'postgresql://{user}:{pwd}@{Serv}:{port}/{DB}'

    for df in file_enu:
        write_to_db(df,con,folder)