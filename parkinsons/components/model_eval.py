import keras;
import mlflow
import pandas as pd;
from parkinsons.entity.config_entity import ModelEvalConfig;
from pathlib import Path;


class ModelEvaluate:
    def __init__(self, model_evaluate: ModelEvalConfig):
        self.data_source = model_evaluate.data_source;
        self.model_source = model_evaluate.model_source;
        self.mlflow_uri = model_evaluate.mlflow_uri;
    
    #["accuracy", "precision", "recall"]
    def evaluate(self):
        model = keras.models.load_model(str(self.model_source));
        X_test = pd.read_csv(Path(self.data_source)/'X_test.csv').values;
        y_test = pd.read_csv(Path(self.data_source)/'y_test.csv').values;

        mlflow.set_experiment("Keras Evaluation");

        with mlflow.start_run():
            result = model.evaluate(X_test, y_test, return_dict = True);
            mlflow.log_metrics(result);