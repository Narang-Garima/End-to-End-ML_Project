# utils.py
import os
import sys
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import pandas as pd
import pymysql
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading MySQL database started")

    try:
        # this is using pymysql-- commenting and using sqlalchemy
        '''
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info("Connection established ", {mydb})
        df = pd.read_sql_query ("SELECT * FROM students", mydb)
        logging.info("SQL query executed successfully")
        return df
        '''

        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
        with engine.connect() as conn:
            logging.info("Connection established using SQLAlchemy")
            
            query = text("SELECT * FROM students")
            df = pd.read_sql_query(query, conn)
            logging.info("SQL query executed successfully") 
            return df

    except Exception as e:
        logging.info("Error in reading data from MySQL")
        raise CustomException(e)
    
    finally: 
        logging.info("Reading MySQL database completed")
