import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'
    MODEL_FILE = os.path.join(settings.MODELS, "LoanPredictionAdaBoost.joblib")
    model = joblib.load(MODEL_FILE)
