import os;
import sys;
import pandas as pd;
import tensorflow as tf;
from parkinsons.entity.config_entity import (ModelTrainingParams, ModelTrainConfig)
from pathlib import Path;

class ModelTrain:
    def __init__(self, model_train_config: ModelTrainConfig):
        self.data_source = model_train_config.data_source;
        self.model_initial_source = model_train_config.model_initial_source;
        self.model_final_source = model_train_config.model_final_source;

    def train(self, model_train_params: ModelTrainingParams):
        model = tf.keras.models.load_model(str(self.model_initial_source));
        X = pd.read_csv(Path(self.data_source) / 'X_train.csv');
        y = pd.read_csv(Path(self.data_source) / 'y_train.csv');
        train_dataset = tf.data.Dataset.from_tensor_slices((X.values, y.values))
        train_dataset = train_dataset.shuffle(buffer_size = len(X)).batch(model_train_params.batch_size)

        print_callback = tf.keras.callbacks.LambdaCallback(
            on_epoch_end=lambda epoch, logs: print(
            f"Epoch {epoch+1}/{model_train_params.epochs} - loss: {logs['loss']:.4f}"
            ) if (epoch + 1) % 100 == 0 else None
        )
        history = model.fit(
            train_dataset, epochs = model_train_params.epochs,
            verbose = 0,
            callbacks = [print_callback]
        )
        os.makedirs(self.model_final_source, exist_ok=True);
        final_path = os.path.join(str(self.model_final_source), "model.keras");
        model.save(final_path);