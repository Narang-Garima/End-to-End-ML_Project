# app.py
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys
from src.MLProject.components.data_integestion import  DataIngestion 

if __name__ == "__main__":
    logging.info("App stared")

    try:
        #a = 1 / 0
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")

    except Exception as e:
        #logging.info("Divided by zero")
        raise CustomException(e, sys)   