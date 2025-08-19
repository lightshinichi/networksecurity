from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__== "__main__" :
    try:
        tpipe =TrainingPipelineConfig()
        data_cofig= DataIngestionConfig(tpipe)
        ingest= DataIngestion(data_cofig)
        logging.info("Intitate the data ingestion")
        artifact= ingest.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        data_valid_config= DataValidationConfig(tpipe)
        data_validation = DataValidation(artifact,data_valid_config)
        logging.info("Initiate data validation")
        data_valid_artifact= data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_valid_artifact)
        logging.info("Data Transformation Initiated")
        data_transformation_config = DataTransformationConfig(tpipe)
        data_transformation = DataTransformation(data_valid_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")
        logging.info("Model training started")
        model_trainer_config = ModelTrainerConfig(tpipe)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created ")



    except Exception as e :
        raise NetworkSecurityException(e,sys)
        

