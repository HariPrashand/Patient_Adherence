import logging
from abc import ABC , abstractmethod 

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score , confusion_matrix
class Evaluation(ABC):
    @abstractmethod
    def calculate_scores(self,y_true:np.ndarray, y_pred:np.ndarray):
        pass

class Accuracy(Evaluation):
    def calculate_scores(self,y_true:np.ndarray, y_pred:np.ndarray):
        try:
            logging.info("Calculating Accuracy")
            a = accuracy_score(y_true, y_pred)
            logging.info("The Accuracy value is: " + str(a))
            return a
        except Exception as e:
            logging.error(
                "Exception occurred in calculate_score method of the MSE class. Exception message:  "
                + str(e)
            )
            raise e


class Specificity(Evaluation):
    """
    Evaluation strategy that uses R2 Score
    """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            r2_score: float
        """
        try:

            logging.info("Entered the calculate_score  of Specificity")
            conf_matrix = confusion_matrix(y_true, y_pred)
            tn, fp, fn, tp = conf_matrix.ravel()

            # Calculate specificity
            r2 = tn / (tn + fp)

            
            logging.info("The specificity score value is: " + str(r2))
            return r2
        except Exception as e:
            logging.error(
                "Exception occurred in calculate_score method of the R2Score class. Exception message:  "
                + str(e)
            )
            raise e


# class RMSE(Evaluation):
#     """
#     Evaluation strategy that uses Root Mean Squared Error (RMSE)
#     """
#     def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
#         """
#         Args:
#             y_true: np.ndarray
#             y_pred: np.ndarray
#         Returns:
#             rmse: float
#         """
#         try:
#             logging.info("Entered the calculate_score method of the RMSE class")
#             rmse = np.sqrt(mean_squared_error(y_true, y_pred))
#             logging.info("The root mean squared error value is: " + str(rmse))
#             return rmse
#         except Exception as e:
#             logging.error(
#                 "Exception occurred in calculate_score method of the RMSE class. Exception message:  "
#                 + str(e)
#             )
#             raise e
