from django.shortcuts import render
import numpy as np
from .apps import PredictConfig
from predict.utils import LoanMapper
from rest_framework.views import APIView
from rest_framework.response import Response
from predict.serializers import LoanSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.


class LoanPredictionView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        data = request.data

        serializer = LoanSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        mapped_data = LoanMapper.loan_mapper(serializer.data)

        loan_predictor = PredictConfig.model
        predicted_result = loan_predictor.predict([mapped_data])
        response = {"Predicted Result": predicted_result}

        return Response(response, status=200)
