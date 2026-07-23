from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
from pathlib import Path
from src.datascience.components.DataTransformation import DataTransformation


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt")) as f:
                status = f.read().split(" ")[-1]
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(data_transformation_config)
                    data_transformation.train_test_splitting()
                else:

                    raise Exception("Your data schema is not validated")

        except Exception as e:
            logger.exception(e)
            raise e
                        

            

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} ended <<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e