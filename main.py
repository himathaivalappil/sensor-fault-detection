from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainingPipeline
import sys


# def test_exception():
#     try:
#         logging.info("Dividing 1 by zero")
#         val = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)

if __name__ == '__main__':
    train_pipeline = TrainingPipeline()
    train_pipeline.run_pipeline()



    # training_pipline_cfg = TrainingPipelineConfig()
    # data_ingestion_cfg = DataIngestionConfig(training_pipeline_config=training_pipline_cfg)
    # print(data_ingestion_cfg.__dict__)

    # mongodbclient = MongoDBClient()
    # print("Collection name: ", mongodbclient.database.list_collection_names())