import os;
import pandas as pd;
import sys;
from pathlib import Path;
from dataclasses import dataclass;

from parkinsons.entity.config_entity import DataIngestionConfig;
import logging

class DataIngestion:
    def __init__(self, data_ingestion_yml: DataIngestionConfig):
        self.root_dir = data_ingestion_yml.root_dir;
        self.data_source = data_ingestion_yml.data_source;
        self.csv_file_store = data_ingestion_yml.csv_file_store;

        os.makedirs(self.root_dir, exist_ok=True);
        print(self.csv_file_store);

    def ingest_data(self):
        datafile = pd.read_csv(str(self.data_source), sep = ",");
        base_path, _ = os.path.splitext(str(self.data_source))
        os.makedirs(self.csv_file_store, exist_ok=True);
        logging.info("csv file made")
        csv_output_path = os.path.join(self.csv_file_store, "parkinsons.csv");
        datafile.to_csv(csv_output_path, index=False)
        logging.info("csv file inserted");
        self.csv_file_store = csv_output_path