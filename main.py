from parkinsons.pipeline.data_ingestion_pipeline import DataIngestionPipeline;
from parkinsons.pipeline.data_preprocessing import DataPreprocessingPipeline;
from parkinsons.pipeline.model_build_pipeline import ModelBuildPipeline;
from parkinsons.pipeline.model_train_pipeline import ModelTrainingPipeline;
import logging;
import sys;
from exceptions.DataIngestionException import DataIngestionException
from exceptions.DataPreprocessingException import DataPreprocessingException;
from exceptions.ModelBuildException import ModelBuildException;


def Data_ingest():
    try:
        logging.info("Data ingestion begins");
        data_ingestion_pipe = DataIngestionPipeline();
        data_ingestion_pipe.run_ingestion_pipeline();
        logging.info("Data ingestion ends");
    except Exception as e:
        raise DataIngestionException(e, sys);

def Data_preprocess():
    try:
        data_preprocessing_pipe = DataPreprocessingPipeline();
        data_preprocessing_pipe.run_preprocessing_pipeline();
    except Exception as e:
        raise DataPreprocessingException(e, sys);

def Model_Build():
    try:
        model_build_pipe = ModelBuildPipeline();
        model_build_pipe.initiate_pipeline();
    except Exception as e:
        raise ModelBuildException(e, sys);

def Model_train():
    try:
        model_train_pipeline = ModelTrainingPipeline();
        model_train_pipeline.initialize_train();
    except Exception as e:
        raise ModelBuildException(e, sys);

if __name__ == "__main__":
    try:
        Data_ingest();
        Data_preprocess();
        Model_Build();
        Model_train();
    except Exception as e:
        logging.error(e);