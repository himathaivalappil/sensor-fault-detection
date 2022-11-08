from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData

import os, sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """Export mongodb collection record as dataframe into feature store

        Raises:
            SensorException: _description_

        Returns:
            DataFrame: _description_
        """
        try:
            logging.info("Exporting data from mongodb into feature store")
            self.sensor_data = SensorData()
            self.dataframe = self.sensor_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )
            self.feature_store_filepath = (
                self.data_ingestion_config.feature_store_filepath
            )

            # Creating folder
            dir_path = os.path.dirname(self.feature_store_filepath)
            os.makedirs(dir_path, exist_ok=True)
            logging.info("Created folder for feature store ")

            # Saving dataframe as csv
            self.dataframe.to_csv(self.feature_store_filepath, index=False, header=True)
            return self.dataframe

        except Exception as e:
            raise SensorException(e, sys)

    def split_data_into_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ration
            )
            logging.info("Performed train test split on the dataframe")
            dir_path = os.path.dirname(self.data_ingestion_config.training_filepath)
            os.makedirs(dir_path, exist_ok=True)

            train_set.to_csv(
                self.data_ingestion_config.training_filepath, index=False, header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_filepath, index=False, header=True
            )
            logging.info(
                "Exported train and test files after splitting to {self.data_ingestion_config.training_filepath}"
            )

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_into_train_test(dataframe=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(
                trained_filepath=self.data_ingestion_config.training_filepath,
                test_filepath=self.data_ingestion_config.testing_filepath,
            )
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)
