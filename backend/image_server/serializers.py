from rest_framework import serializers, fields
from .models import QnaValidate
from qnas.models import Qna, Ans



class QnaImageValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = QnaValidate
        fields = '__all__'