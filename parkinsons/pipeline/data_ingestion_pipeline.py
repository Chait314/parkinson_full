import os;
import pandas as pd;
import sys;
from pathlib import Path;
from dataclasses import dataclass;

from parkinsons.entity.config_entity import DataIngestionConfig;
import yaml
from parkinsons.components.data_ingestion import DataIngestion;
from exceptions.DataIngestionException import DataIngestionException


class DataIngestionPipeline():
    def __init__(self):
        pass;

    def run_ingestion_pipeline(self):
        try:
            with open('config.yaml', 'r') as file:
                data = yaml.safe_load(file);
            data_ing_yml:DataIngestionConfig = DataIngestionConfig(root_dir=data["data_ingestion"]["root_dir"], 
                                                data_source=data["data_ingestion"]["data_source"],
                                                csv_file_store=data["data_ingestion"]["csv_file_store"]);
            os.makedirs(data["artifacts_root"]["artifact_root_dir"], exist_ok=True);
            data_ingestion = DataIngestion(data_ing_yml)
            data_ingestion.ingest_data();
        except Exception as e:
            raise DataIngestionException(e, sys);