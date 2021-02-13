from rest_framework import serializers, fields
from .models import Qna, Ans, tech, Qnasmall, Anssmall
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileListSerializer
from accounts.models import User

class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'id', 'username')


class AnssmalllistSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Anssmall
        fields = ('id', "ans", "content", "user", "written_time")


class ProfileqnaListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img')


class ProfileqnaSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'bio')
# 'post_num' is_following,is_following추가해야함


class QnasmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qnasmall
        fields = ('id', "qna", "content", "user", "written_time")


class QnasmalllistSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Qnasmall
        fields = ('id', "qna", "content", "user", "written_time")


class AnssmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Anssmall
        fields = ('id', "ans", "content", "user", "written_time")


class QnaListforamtSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfileqnaListSerializer(
        read_only=True,
    )
    
    comment_num = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id', 'title','user', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class QnaListSerializer(serializers.ModelSerializer):
    
    profile = ProfileqnaListSerializer(
        read_only=True,
    )

    comment_num = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class AnsdetailSerializer(serializers.ModelSerializer):

    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfileqnaListSerializer(
        read_only=True,
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'id', 'assisted', 'user','like_ans_num', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')

 
class AnslistformatSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfileListSerializer(
        read_only=True
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ('id', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')


class AnslistSerializer(serializers.ModelSerializer):
    
    profile = ProfileListSerializer(
        read_only=True
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ('id', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')


class AnsSerializer(serializers.ModelSerializer):


    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ('id', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set', 'profile')


class AnsinfoSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfileListSerializer(
        read_only=True
    )

    anssmall_set = AnssmalllistSerializer(
        many=True,
        read_only=True,
    )

    comment_anssmall_num = serializers.IntegerField(
        source='anssmall_set.count',
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ('id', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set', 'comment_anssmall_num','profile')


class QnadetailSerializer(serializers.ModelSerializer):

    ref_tags= fields.MultipleChoiceField(choices=tech)
    
    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfileqnaSerializer(
        read_only=True,
    )

    qnasmall_set = QnasmalllistSerializer(
        many=True,
        read_only=True,
    )

    ans_set = AnsinfoSerializer(
        many=True,
        read_only=True,
    )

    comment_num = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id','profile', 'title','written_time', 'ref_tags', 'solved', 'like_num', 'comment_num',
        'viewed_num', 'bookmark_num','content', 'qnasmall_set', 'ans_set', 'liked', 'bookmarked','user' )


class QnaSerializer(serializers.ModelSerializer):


    ref_tags= fields.MultipleChoiceField(choices=tech)
        
    qnasmall_set = QnasmallSerializer(
        many=True,
        read_only=True,
    )

    ans_set = AnsSerializer(
        many=True,
        read_only=True,   
    )

    comment_num = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id','title','user','profile','content','ref_tags', 'liked', 'like_num', 'bookmarked',
        'solved','bookmark_num', 'viewed_num', 'written_time','ans_set', 'comment_num','qnasmall_set')


class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', "liked")


class like_ansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "liked_ans")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', "bookmarked")


class solveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "assisted")
