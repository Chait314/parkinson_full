from parkinsons.pipeline.data_ingestion_pipeline import DataIngestionPipeline;
from parkinsons.pipeline.data_preprocessing import DataPreprocessingPipeline;
import logging;
import sys;
from exceptions.DataIngestionException import DataIngestionException
from exceptions.DataPreprocessingException import DataPreprocessingException;

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


if __name__ == "__main__":
    try:
        Data_ingest();
        Data_preprocess();
    except Exception as e:
        logging.error(e);