from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.DataIngestion import DataIngestion
from src.datascience import logger

STAGE_NAME = "Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):      
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
        except Exception as e:
            raise e


     
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
