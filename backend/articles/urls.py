from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('awrite', PostViewSet)
router.register('cwrite', CommentViewSet)


urlpatterns = [
    path('forum/', include(router.urls)),
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('articles/<int:article_pk>/comments/', views.create_comment),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),
]
