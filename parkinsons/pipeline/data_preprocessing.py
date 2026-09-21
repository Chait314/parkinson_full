import pandas as pd;
from exceptions.DataPreprocessingException import DataPreprocessingException
import sys;
import logging
import os;
from parkinsons.entity.config_entity import DataPreprocessingConfig;
from parkinsons.components.data_preprocessing import DataPreprocessing;
import yaml;

class DataPreprocessingPipeline:
    def __init__(self):
        pass;
    def run_preprocessing_pipeline(self):
        try:
            with open('config.yaml', 'r') as file:
                    data = yaml.safe_load(file);
            logging.info("Data Preprocessing Begins");
            data_prepro = data['data_preprocessing'];
            
            data_preprocess_config:DataPreprocessingConfig = DataPreprocessingConfig(
                data_prepro['root_dir'], data_prepro['data_source'], data_prepro['csv_file_store']
            )
            data_preprocessing = DataPreprocessing(data_preprocess_config);
            logging.info("Preprocess step begins");
            data_preprocessing.preprocess();
            logging.info("Preprocess step ends")
        except Exception as e:
            raise DataPreprocessingException(e, sys);