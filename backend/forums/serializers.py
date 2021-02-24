from rest_framework import serializers, fields
from .models import Post, Comment, tech
from profiles.models import Profile, ForumImagePost
from profiles.serializers import ProfileSerializer, ProfileListSerializer, ProfilePinnedQnaSerializer, ProfileImageSerializer, ProfilePinnedForumSerializer
from accounts.models import User


class ImagePostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(use_url=True, allow_empty_file=True)

    class Meta:
        model = ForumImagePost
        fields = ('thumbnail',)


class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'follower_num', 'followee_num')


class ProfilepostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', )


class ProfilepostSerializer(serializers.ModelSerializer):
    pinned_qnas = ProfilePinnedQnaSerializer(many=True, read_only=True)
    pinned_forums = ProfilePinnedForumSerializer(many=True, read_only=True)
    thumbnail = ImagePostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'post_num', 'follower_num',
                  'bio', 'thumbnail', 'pinned_qnas', 'pinned_forums', )


class PostListforamtSerializer(serializers.ModelSerializer):

    user = UserinfoSerializer(
        read_only=True,
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    profile = ProfilepostSerializer(
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'thumbnail', 'written_time', 'ref_tags',
                  'liked', 'comment_count', 'like_num', 'viewed_num', 'user', 'profile')


class PostListSerializer(serializers.ModelSerializer):

    user_info = ProfilepostListSerializer(
        read_only=True,
        many=True
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'thumbnail', 'written_time', 'ref_tags', 'liked',
                  'comment_count', 'viewed_num', 'like_num', 'user_info', 'profile')


# class PostListDetailSerializer(serializers.ModelSerializer):

#     thumbnail = serializers.ImageField(use_url=True)

#     profile = ProfilepostListSerializer(
#             read_only=True,
#         )

#     user_info = ProfilepostListSerializer(
#         many=True
#     )

#     comment_count = serializers.IntegerField(
#         source='comment_set.count',
#         read_only=True,
#     )
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'profile', 'written_time', 'ref_tags', 'liked', 'bookmarked', 'comment_count', 'thumbnail', 'viewed_num', 'like_num', 'bookmark_num', 'user_info','profile')


class CommentdetailSerializer(serializers.ModelSerializer):

    profile = ProfilepostSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'user', 'like_comment_num',
                  'post', 'written_time', 'liked_comment', 'profile')


class CommentlistSerializer(serializers.ModelSerializer):

    profile = ProfilepostSerializer(
        read_only=True
    )

    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'like_comment_num', 'user',
                  'post', 'written_time', 'liked_comment', 'profile')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user', 'id', 'comment_content', 'like_comment_num',
                  'post', 'written_time', 'liked_comment', 'profile')


class DetailCommentSerializer(serializers.ModelSerializer):

    profile = ProfilepostSerializer(
        read_only=True
    )

    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('user', 'id', 'written_time', 'comment_content',
                  'like_comment_num', 'profile')


class PostSerializer(serializers.ModelSerializer):

    ref_tags = fields.MultipleChoiceField(choices=tech)

    comment_set = CommentSerializer(
        many=True,
        read_only=True,
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'ref_tags', 'bookmark_num', 'bookmarked', 'like_num', 'liked', 'thumbnail',
                  'viewed_num', 'comment_count', 'written_time', 'comment_set', 'profile')


class ForumPostSerializer(serializers.ModelSerializer):

    ref_tags = fields.MultipleChoiceField(choices=tech)

    profile = ProfilepostSerializer(
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'thumbnail', 'ref_tags', 'bookmark_num', 'bookmarked',
                  'like_num', 'liked', 'comment_count', 'viewed_num', 'written_time', 'profile')


class PostdetailSerializer(serializers.ModelSerializer):

    ref_tags = fields.MultipleChoiceField(choices=tech)

    comment_set = DetailCommentSerializer(
        many=True,
        read_only=True,
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    profile = ProfilepostSerializer(
        read_only=True
    )

    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user', 'thumbnail', 'ref_tags', 'bookmark_num', 'bookmarked',
                  'like_num', 'liked', 'comment_count', 'viewed_num', 'is_following', 'written_time', 'profile', 'comment_set')


class likeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', "liked",  "like_num", "like_users")


class like_commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', "liked_comment")


class bookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', "bookmarked",  "bookmark_num", "bookmark_users")


class pinnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'pinned', 'pinned_num', 'pinned_users')


class pinnedDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title',)


class ForumpinnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'pinned', 'pinned_users', 'pinned_num')


class isfollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', "is_following")


class isfollowingcommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', "is_following")
