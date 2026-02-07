from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger
from pathlib import Path

STAGE_NAME='Model Evaluation Stage'

class ModelEvaluationTrainingPipeline():
    def __init__(self) -> None:
        pass
    def start_pipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__=='__main__':
    try:
        logger.info(f'>>>>>>>> {STAGE_NAME} started <<<<<<<<')
        obj=ModelEvaluationTrainingPipeline()
        obj.start_pipeline()
        logger.info(f'>>>>>>>> {STAGE_NAME} completed <<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e