from rest_framework import serializers
from .models import Qna, Ans


class QnaListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'author')


class AnsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', 'content', 'user', 'qna')
        # read_only_fields = ('qna',)
        

class QnaSerializer(serializers.ModelSerializer):
    
    ans_set = AnsSerializer(
        many=True,
        read_only=True,
    )

    ans_count = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id', 'title', 'content', 'author', 'like', 'view', 'image', 'created_at', 'updated_at', 'ans_set', 'ans_count',)