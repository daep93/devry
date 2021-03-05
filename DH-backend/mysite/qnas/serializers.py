from rest_framework import serializers
from .models import Qna

class QnaRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Qna
        fields=['title','content','ref_tags','writer']
    

class QnaListSerializer(serializers.ModelSerializer):
    ref_tags=serializers.SerializerMethodField()
    class Meta:
        model=Qna
        fields='__all__'
    def get_ref_tags(self, qna):
        return qna.ref_tags.split('|')