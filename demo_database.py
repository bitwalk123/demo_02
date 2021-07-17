import os
import pandas as pd
import sqlite3

# local python files
from demo_parser import FileParser


class DBObj:
    name_db: str = None
    name_tbl: str = 'data'
    key_time: str = None
    list_param: list = None

    def __init__(self, name_db: str, file_obj: FileParser):
        self.name_db = name_db

        # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
        #  due to demonstration purpose, database file is deleted and create
        #  everytime when you run this application and reading fi;e for data.
        if os.path.exists(self.name_db):
            os.remove(self.name_db)

        # obtain data from file object
        df: pd.DataFrame = file_obj.get_data()

        # Time Data
        self.key_time = df.columns[0:1].values.tolist()[0]

        # Parameters
        self.list_param = df.columns[1:len(df.columns) - 1].values.tolist()

        # database creation
        self.create_db(df, self.name_db)

    # -----------------------------------------------------------------------------
    #  create_db
    #  create SQLite database
    #
    #  argument
    #    df: pd.DataFrame
    #    name_db: str - database name
    #
    #  return
    #    (none)
    # -----------------------------------------------------------------------------
    def create_db(self, df: pd.DataFrame, name_db: str):
        con: sqlite3.Connection = sqlite3.connect(name_db)
        df.to_sql('data', con, if_exists='append', index=False)
        con.close()

    # -------------------------------------------------------------------------
    #  get_df_all
    #  get all data in dataframe
    #
    #  argument
    #    (none)
    #
    #  return
    #    pd.DataFrame - all data in dataframe
    # -------------------------------------------------------------------------
    def get_df_all(self) -> pd.DataFrame:
        df: pd.DataFrame = self.get_df_from_db_all(self.name_db, self.name_tbl)
        return df

    # -------------------------------------------------------------------------
    #  get_params
    #  get list of parameter name
    #
    #  argument
    #    (none)
    #
    #  return
    #    list - list of parameter name
    # -------------------------------------------------------------------------
    def get_params(self) -> list:
        return self.list_param

    # -------------------------------------------------------------------------
    #  get_trend_data
    #  get data with timestamp for specific parameter
    #
    #  argument
    #    param: str - name of parameter
    #
    #  return
    #    pd.DataFrame - data with timestamp for specific parameter
    # -------------------------------------------------------------------------
    def get_trend_data(self, param: str) -> pd.DataFrame:
        sql: str = 'SELECT \"{0}\", \"{1}\" FROM \"{2}\"'.format(self.key_time, param, self.name_tbl)
        df: pd.DataFrame = self.get_df_from_db(self.name_db, sql)

        return df

    # -------------------------------------------------------------------------
    #  get_df_from_db
    #  get all data from database
    #
    #  argument
    #    name_db: str - database name
    #    sql: str - SQL
    #
    #  return
    #    pd.DataFrame - all data from database
    # -------------------------------------------------------------------------
    def get_df_from_db(self, name_db: str, sql: str) -> pd.DataFrame:
        con: sqlite3.Connection = sqlite3.connect(name_db)
        df: pd.DataFrame = pd.read_sql_query(sql, con)
        con.close()

        return df

    # -------------------------------------------------------------------------
    #  get_df_from_db_all
    #  get all data from database
    #
    #  argument
    #    name_db: str - database name
    #    name_tbl: str - table name
    #
    #  return
    #    pd.DataFrame - all data from database
    # -------------------------------------------------------------------------
    def get_df_from_db_all(self, name_db: str, name_tbl: str) -> pd.DataFrame:
        sql: str = 'SELECT * FROM {0}'.format(name_tbl)
        df: pd.DataFrame = self.get_df_from_db(name_db, sql)

        return df
