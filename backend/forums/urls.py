from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet


routerq = routers.DefaultRouter()
routerq.register('post', PostViewSet)
routerq.register('comment', CommentViewSet)

urlpatterns = [
    path('forumtest/', include(routerq.urls)),
    path('board/forum/', views.post_list),
    path('forum/', views.post_list_create),
    path('forum/<int:post_pk>/', views.post_detail_update_delete),
    path('forum_like/<int:post_pk>/', views.like),
    path('forum_bookmark/<int:post_pk>/', views.bookmark),
 
    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail_update_delete),
    path('comment_like/<int:comment_pk>/', views.like_comment),
]
