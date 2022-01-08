from django.urls import path
from predict.views import LoanPredictionView

urlpatterns = [
    path('predict/', LoanPredictionView.as_view(), name="loan_prediction")
]
