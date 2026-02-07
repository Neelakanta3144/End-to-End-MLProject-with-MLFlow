from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    obj=DataIngestionTrainingPipeline()
    obj.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e