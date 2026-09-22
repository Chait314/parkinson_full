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

@dataclass
class ModelParams:
    input_nodes: int;
    hidden_layers: int;
    output_nodes: int;
    optimizer: str;
    loss: str;

@dataclass
class ModelConfig:
    data_source: Path;
    model_store: Path;