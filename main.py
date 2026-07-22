from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("=" * 60)
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    logger.info("=" * 60)

except Exception as e:
    logger.exception(e)
    raise


STAGE_NAME = "Data Validation Stage"

try:
    logger.info("=" * 60)
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    logger.info("=" * 60)

except Exception as e:
    logger.exception(e)
    raise