import logging
import mlflow
from sklearn.compose import ColumnTransformer
import pandas  as pd 
import numpy as np
import mlflow
import sklearn
from zenml import step
from src.model_dev import DecisionTree , LightGBM, XGBoostModel, RandomForest, GradientBoosting, MLP_Classifier, logisticRegression
from .config import ModelNameConfig
from sklearn.pipeline import Pipeline

from zenml.client import Client

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def model_train(
    X_train: pd.DataFrame,
    Y_train: np.ndarray,
    X_test: pd.DataFrame,
    Y_test: np.ndarray,
    preprocessor: ColumnTransformer,
    config : ModelNameConfig,
    )->Pipeline:
    model = None
    if config.model_name == 'decisiontree':
        mlflow.sklearn.autolog()
        model = DecisionTree()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'xgboost':
        mlflow.sklearn.autolog()
        model = XGBoostModel()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'lightgbm':
        mlflow.sklearn.autolog()
        model = LightGBM()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'randomforest':
        mlflow.sklearn.autolog()
        model = RandomForest()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'logisticRegression':
        mlflow.sklearn.autolog()
        model = logisticRegression()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'GradientBoosting':
        mlflow.sklearn.autolog()
        model = GradientBoosting()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    elif config.model_name == 'MLPClassifier':
        mlflow.sklearn.autolog()
        model = MLP_Classifier()
        trained_model = model.train(X_train, Y_train, preprocessor)
        return trained_model
    
    else:
        raise ValueError("Model {} not supported".format(config.model_name))