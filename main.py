from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Data Validation Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    data_validation=DataValidationTrainingPipeline()
    data_validation.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e