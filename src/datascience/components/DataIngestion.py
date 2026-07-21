from urllib import request
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataIngestionConfig
import os
 
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        here we get
            root_dir, source_URL, local_data_file, store_dir
        """
        self.config = config 

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: {headers}")

        else:
            logger.info(f"File already exists")
