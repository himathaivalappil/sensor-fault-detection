import os, sys
import numpy as np
import pandas as pd
from typing import Optional
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME


class SensorData:
    """
    This class helps to export entire mongodb record as pandas dataframe
    """

    def __init__(self):
        """_summary_

        Raises:
            SensorException: _description_
        """
        try:
            self.mongo_client = MongoDBClient(DATABASE_NAME)
        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None
    ) -> pd.DataFrame:
        """_summary_

        Args:
            collection_name (str): _description_
            database_name (Optional[str], optional): _description_. Defaults to None.

        Raises:
            SensorException: _description_

        Returns:
            pd.DataFrame: _description_
        """
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"], axis=1)
                logging.info("Removed column _id from table")
            df.replace({"na": np.nan}, inplace=True)
            logging.info("Replaced all na values with np.nan values")
            return df

        except Exception as e:
            raise SensorException(e, sys)
