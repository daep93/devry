from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('awrite', PostViewSet)
router.register('cwrite', CommentViewSet)
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('forum/', include(router.urls)),
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('articles_like/<int:article_pk>/', views.like),
    path('articles_bookmark/<int:article_pk>/', views.bookmark),
    path('articles_pinned/<int:article_pk>/', views.pinned),
    path('articles/<int:article_pk>/comments/', views.create_comment),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),
]
