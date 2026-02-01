import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        print(f"Train Path: {train_data_path}")
        print(f"Test Path: {test_data_path}")

        data_transformation=DataTransformation()

        train_arr,test_arr,_=data_transformation.initiate_data_tranformation(train_data_path,test_data_path)


    except Exception as e:
        logging.error("Exception occurred in training pipeline")
        raise CustomException(e, sys)
    


    

