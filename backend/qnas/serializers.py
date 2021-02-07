from rest_framework import serializers, fields
from .models import Qna, Ans, tech, Qnasmall, Anssmall
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileListSerializer
from accounts.models import User

class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'id', 'username')


class ProfileqnaListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img')


class ProfileqnaSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'bio')
# 'post_num' is_following,is_following추가해야함

class ProfileQnaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'username', 'written_time', 'thumbnail', 'like_num', 'comment_num', 'ref_tags',)


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


class AnssmalllistSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

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
    
    class Meta:
        model = Qna
        fields = ('id', 'title','user', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class QnaListSerializer(serializers.ModelSerializer):
    
    profile = ProfileqnaListSerializer(
        read_only=True,
    )
    
    class Meta:
        model = Qna
        fields = ('id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


class AnsdetailSerializer(serializers.ModelSerializer):

    profile = ProfileqnaListSerializer(
        read_only=True,
    )

    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'title', 'assisted', 'user','like_ans_num', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')

 
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
        fields = ( 'title', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set' ,'profile')


class AnsSerializer(serializers.ModelSerializer):


    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ( 'title', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set', 'profile')


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
        fields = ('id','profile', 'title','written_time', 'ref_tags', 'solved', 'like_num', 'ans_count',
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

    ans_count = serializers.IntegerField(
        source='ans_set.count',
        read_only=True,
    )

    class Meta:
        model = Qna
        fields = ('id','title', 'user','profile','content','ref_tags', 'liked', 'like_num', 'bookmarked',
        'solved','bookmark_num', 'viewed_num', 'written_time','ans_set', 'ans_count','qnasmall_set')


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


class TagSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('author', 'ref_tags_count', )  