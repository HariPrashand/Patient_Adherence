import logging
import mlflow
from typing import Tuple
from typing_extensions import Annotated
import pandas  as pd 
import numpy as np
from zenml import step
from sklearn.base import RegressorMixin
from sklearn.pipeline import Pipeline
from src.evaluation import Accuracy, Specificity 
from zenml.client import Client
import src

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(
    model: Pipeline,
    X_test: pd.DataFrame,
    y_test: np.ndarray,
) -> Tuple[Annotated[ src.evaluation.Accuracy, "acc"], Annotated[float, "spec"]]:
    try:
        prediction = model.predict(X_test)
        acc = Accuracy()
        a = acc.calculate_scores(y_test,prediction)
        mlflow.log_metric("accuracy", a)
        
        r2_class = Specificity()
        r2 = r2_class.calculate_scores(y_test,prediction)
        mlflow.log_metric("specificity", r2)
        
        # rmse_class = RMSE()
        # rmse = rmse_class.calculate_scores(y_test,prediction)
        # mlflow.log_metric("rmse", rmse)
        
        return acc ,r2
    except Exception as e:
        logging.error("Error in evaluating Model: {}".format(e))
        raise e
