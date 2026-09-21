import pandas as pd;
from exceptions.DataPreprocessingException import DataPreprocessingException
import sys;
import logging
import os;
from parkinsons.entity.config_entity import DataPreprocessingConfig;
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

class DataPreprocessing:
    def __init__(self, data_preprocessing_config:DataPreprocessingConfig):
        self.root_dir = data_preprocessing_config.root_dir;
        self.data_source = data_preprocessing_config.data_source;
        self.csv_file_store = data_preprocessing_config.csv_file_store;

    def preprocess(self):
        try:
            df = pd.read_csv("artifacts/data/parkinsons.csv");
            df = df.dropna();
            df = df.drop(["name"], axis = 1);

            smote = SMOTE(random_state=42);
            X = df.drop(["status"], axis=1);
            y = df["status"];
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42);
            X_re_train, y_re_train = smote.fit_resample(X_train, y_train)

            os.makedirs(self.csv_file_store, exist_ok = True);
            X_re_train.to_csv(os.path.join(self.csv_file_store, 'X_train.csv'), index = False);
            y_re_train.to_csv(os.path.join(self.csv_file_store, 'y_train.csv'), index = False);
            X_test.to_csv(os.path.join(self.csv_file_store, 'X_test.csv'), index = False);
            y_test.to_csv(os.path.join(self.csv_file_store, 'y_test.csv'), index = False);

        except Exception as e:
            raise DataPreprocessingException(e, sys);
