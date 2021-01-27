from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet


routerq = routers.DefaultRouter()
routerq.register('qna', PostViewSet)
routerq.register('ans', CommentViewSet)

urlpatterns = [
    path('qna/', include(routerq.urls)),
    path('qnas/', views.qna_list_create),
    path('qnas/<int:qna_pk>/', views.qna_detail_update_delete),
    path('qnas/<int:qna_pk>/anss/', views.create_comment),

    path('anss/', views.comment_list),
    path('anss/<int:comment_pk>/', views.comment_detail_update_delete),
]
