from rest_framework import serializers, fields
from .models import QnaValidate, AnsValidate



class QnaImageValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = QnaValidate
        fields = '__all__'


class AnsImageValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnsValidate
        fields = '__all__'