from rest_framework import serializers, fields, renderers
from .models import Qna, Ans, tech, Qnasmall, Anssmall, ImagePost
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileListSerializer
from accounts.models import User

class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'id', 'username', 'follower_num', 'followee_num')

#  추가했음
class QnaImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qna
        fields = ('title', 'user', 'content', 'ref_tags',)
class AnsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ans
        fields = ('user', 'content',)


# 이미지 업로드
class ImagePostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = ImagePost
        fields = ('image',)


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
        fields = ('user', 'username', 'profile_img', 'bio', 'pinned_posts')


class QnasmallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qnasmall
        fields = ('id', "qna", "content", "user", "written_time")


class AnsQnaTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = ('title',)

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
        fields = ('qna_id', 'title','user', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


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
        fields = ('qna_id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')


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
    title = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    anssmall_set = AnssmallSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ans
        fields = ('id', 'assisted', 'like_ans_num','user', 'content', 'qna', 'written_time', 'liked_ans', 'anssmall_set', 'profile', 'title', 'username')


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
        fields = ('qna_id','profile', 'title','written_time', 'ref_tags', 'solved', 'like_num', 'comment_num',
        'viewed_num', 'bookmark_num','content', 'qnasmall_set', 'ans_set', 'liked', 'bookmarked', 'is_following', 'user' )


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
        fields = ('qna_id','title','user','profile','content','ref_tags', 'liked', 'like_num', 'bookmarked', 'pinned', 'pinned_num',
        'solved','bookmark_num', 'viewed_num', 'written_time','ans_set', 'comment_num','qnasmall_set')


class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('qna_id', "liked", "like_num", "like_users")


class like_ansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "liked_ans")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('qna_id', "bookmarked", "bookmark_num", "bookmark_users")

class QnapinnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qna
        fields = ('qna_id', 'pinned', 'pinned_users', 'pinned_num')


class QnaDetailPinnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qna
        fields = ('qna_id', 'title',)

class solveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "assisted")


class isfollowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qna
        fields = ('qna_id', "is_following")


class isfollowingansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ans
        fields = ('id', "is_following")


class mybookmarkSerializer(serializers.ModelSerializer):
    
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
        fields = ('qna_id', 'title','user', 'written_time', 'ref_tags', 'like_num', 'comment_num', 'viewed_num', 'solved', 'liked', 'profile')
