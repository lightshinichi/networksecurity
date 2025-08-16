from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__== "__main__" :
    try:
        tpipe =TrainingPipelineConfig()
        data_cofig= DataIngestionConfig(tpipe)
        ingest= DataIngestion(data_cofig)
        logging.info("Intitate the data ingestion")
        artifact= ingest.initiate_data_ingestion()
        print(artifact)


    except Exception as e :
        raise NetworkSecurityException(e,sys)
        

