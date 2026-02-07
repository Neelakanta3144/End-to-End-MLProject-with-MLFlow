from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME='Data Transformation Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    data_transform=DataTransformationTrainingPipeline()
    data_transform.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Training Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    model_train=ModelTrainerTrainingPipeline()
    model_train.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Evaluation Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.start_pipeline()
    logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e