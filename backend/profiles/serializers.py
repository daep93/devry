from rest_framework import serializers, fields
from .models import Profile
from .models import tech, tags
from django.shortcuts import get_object_or_404

from articles.serializers import ArticleProfileSerializer, ArticleListSerializer, ArticleSerializer, CommentProfileSerializer
from accounts.serializers import UserSerializer

class ProfileListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'profile_img', 'tech_stack', 'tag')


class ProfileSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=tags)        

    posts = ArticleProfileSerializer(many=True, read_only=True)
    # posts = ArticleProfileSerializer(read_only=True)
    comments = CommentProfileSerializer(many=True, read_only=True)
    # comments = CommentProfileSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'profile_img', 'region', 'group', 'bio', 'sns_name',
        'sns_url', 'tech_stack', 'project_name','project_url','tag', 'posts', 'comments')

 
class ProfileUpdateSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=tags)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'profile_img', 'region', 'group', 'bio', 'sns_name',
        'sns_url', 'tech_stack', 'project_name','project_url','tag')



# 불러오기   ex> profile/3   get

# {
#     email,               // 이메일
#     username,            // 사용자 이름
#     joined,              // 가입한 날짜
#     follower_num,        // 팔로워 수
#     followee_num,        // 팔로이 수
#     prifile_img,         // 이미지 baseUrl인 https://placeimg.com(예시) 뒤에 올 주소. 
#     region,              //  사는 지역
#     group,               // 소속 
#     bio,                 // 자기소개
#     links: {             // 깃헙, 링크드인과 같은 링크
# 		  name: url
# 		}
# 	  tech_stack: [tech],  // 기술 스택 목록
#     projects: {          // 프로젝트 목록
# 			name: url,
#     }  
#     tags: {              // 선호하는 tag 목록
#       tag: referred_num // 태그이름 : 글에 태그된 횟수 
#     },
#     pinned_posts: [                    // 고정한 글 목록 (자신이 쓴 글 중에서)
#      {
#        id,               // 글 번호
#        title,            // 글 제목
# 			 username,         // 사용자 이름
#        written_time,     // 글이 쓰인 시점
#        thumbnail_img,    // 글의 썸네일
#        like_num,         // 얼마나 좋아요를 받았는지   
#        comment_num,      // 글의 댓글 갯수
#        tags : [ tag ]                 // 글에 참조된 태그 목록
#      }
#     ],
#      posts: [                    // 글 목록 전체
#      {
#        id,               // 글 번호
#        title,            // 글 제목
# 			 username,         // 사용자 이름
#        written_time,     // 글이 쓰인 시점
#        thumbnail_img,    // 글의 썸네일
#        like_num,         // 얼마나 좋아요를 받았는지   
#        comment_num,      // 글의 댓글 갯수
#        tags : [ tag ]                 // 글에 참조된 태그 목록
#      }
#     ],
#     comments: [                    // 댓글 목록  전체
#      {
#        comment_id,                  // 댓글 번호
# 			 post_id,                  // 댓글이 쓰여진 글 번호
# 			 username,           // 사용자 이름
#        title,               // 글 제목
#        written_time,        // 글이 쓰인 시점
#        comment,             // 내가 해당 글에 쓴 댓글 내용 
#      }
#     ] 
#   }


# 
# 불러오기    ex> profile/setting     get    이전의 프로필 설정을 확인할 수 있게 요청 토큰 인증하고 사용자 프로필 정보 가져옴
#         {
# 	 email                             // 이메일
#    profile_img,                      // 이미지서버의 baseUrl인 https://placeimg.com(예시) 뒤에 올 주소.
#    region,                           // 사는 지역
#    group,                            // 소속 
#    bio,                              // 자기소개    
#    links: {                          // 링크 목록(깃헙, 페이스북, 링크드인)
#        name: url,           
#    } 
#    tech_stacks                       // 기술 스택 목록
#    projects : {                      // 프로젝트 목록(이름 : URL) - 프로젝트는 최대 3개까지만 입력 가능
#        name: url,   
# 	 }
#    tags,                             // 선호하는 tag 목록
# } 

# 수정   ex>profile/setting       put  프로필 정보 갱신 토큰 인증하고 프로필 수정
# {
# 	 username,                         // 닉네임
#    profile_img,                      // 이미지서버의 baseUrl인 https://placeimg.com(예시) 뒤에 올 주소.
#    region,                           // 사는 지역
#    group,                            // 소속 
#    bio,                              // 자기소개    
#    links: {                          // 링크 목록(깃헙, 페이스북, 링크드인)
#        name: url,           
#    } 
#    tech_stacks                       // 기술 스택 목록
#    projects : {                      // 프로젝트 목록(이름 : URL) - 프로젝트는 최대 3개까지만 입력 가능
#        name: url,   
# 	 }
#    tags                              // 선호하는 tag 목록
# } 