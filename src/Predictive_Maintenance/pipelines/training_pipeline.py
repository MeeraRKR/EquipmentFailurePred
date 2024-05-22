import os , sys

from src.Predictive_Maintenance.components.data_ingestion import DataIngestion
from src.Predictive_Maintenance.components.data_transformation import DataTransformation
from src.Predictive_Maintenance.components.model_trainer import ModelTrainer

from src.Predictive_Maintenance.logger import logging
from src.Predictive_Maintenance.exception import CustomException

def main():
    try:
        obj = DataIngestion()
        raw_data_path = obj.initiate_data_ingestion()

        data_transformation = DataTransformation()
        df_sampled = data_transformation.initiate_data_transformation(raw_data_path)
        
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(df_sampled)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()