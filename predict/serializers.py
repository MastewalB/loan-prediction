from rest_framework import fields, serializers


class LoanSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=15)
    married = serializers.CharField(max_length=15)
    dependents = serializers.IntegerField(max_value=None, min_value=None)
    education = serializers.CharField(max_length=200)
    self_employed = serializers.CharField(max_length=5)
    applicant_income = serializers.IntegerField(max_value=None, min_value=None)
    coapplicant_income = serializers.IntegerField(
        max_value=None, min_value=None)
    loan_amount = serializers.FloatField(max_value=None, min_value=None)
    loan_amount_term = serializers.IntegerField(
        max_value=None, min_value=None)
    credit_history = serializers.IntegerField(max_value=None, min_value=None)
    property_area = serializers.CharField(max_length=255)
