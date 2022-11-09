from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig, TrainingPipelineConfig
from sensor.utils.main_utils import read_yaml_file
from sensor.logger import logging
from sensor.exception import SensorException
import os, sys
import pandas as pd


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e, sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame):
        try:
            number_of_columns = len(self._schema_config["columns"])
            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e, sys)

    def is_numerical_column_exist(self, dataframe:pd.DataFrame):
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns

            numerical_column_present = True
            missing_numerical_columns = []
            for numerical_column in numerical_columns:
                if numerical_column not in dataframe.columns:
                    missing_numerical_columns.append(numerical_column)
            logging.INFO(f"Missing numerical columns: [{missing_numerical_columns}]")
            return numerical_column_present
        except Exception as e:
            raise SensorException(e, sys)

    def detect_data_drift(self):
        pass

    def initiate_data_validation(self):
        try:
            error_message = ""
            train_file_path = self.data_ingestion_artifact.trained_filepath
            test_file_path = self.data_ingestion_artifact.test_filepath

            # Reading data from train and test csv files
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            #Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all columns \n"

            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test dataframe does not contain all columns\n"

            # Validate numerical columns
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all numerical columns\n"

            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test data does not  contain all numerical columns"

            if len(error_message) > 0:
                raise Exception(error_message)
            
            # Check data drift
            

            
        except Exception as e:
            raise SensorException(e, sys)
