import pandas as pd;
import tensorflow as tf;
from tensorflow.keras import layers, models;
import yaml;
import os;
import sys;
from parkinsons.entity.config_entity import (ModelConfig, ModelParams);
import pickle;

class Model:
    def __init__(self, model_params: ModelParams, model_config: ModelConfig):
        self.inner_nodes = model_params.input_nodes;
        self.hidden_layers = model_params.hidden_layers;
        self.outer_nodes = model_params.output_nodes;
        self.optimizer = model_params.optimizer;
        self.loss = model_params.loss;

        self.data_source = model_config.data_source
        self.model_store = model_config.model_store

        self.model = models.Sequential([
            layers.Input(shape=(self.inner_nodes,)),
            layers.Dense(32, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(32, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ]);

    def compile_model_and_store(self):
        self.model.compile(
            optimizer = self.optimizer,
            loss = self.loss,
            metrics=["accuracy", "precision", "recall"]
        );

        os.makedirs(self.model_store, exist_ok=True);
        model_path = os.path.join(str(self.model_store), "model.keras");

        self.model.save(model_path);

    