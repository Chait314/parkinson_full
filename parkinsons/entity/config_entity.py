from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir:Path;
    data_source:Path;
    csv_file_store:Path;

@dataclass
class DataPreprocessingConfig:
    root_dir:Path;
    data_source:Path;
    csv_file_store:Path;