from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, QnasmallViewSet, AnssmallViewSet


routerq = routers.DefaultRouter()
routerq.register('qna', PostViewSet)
routerq.register('ans', CommentViewSet)
routerq.register('qnasmall', QnasmallViewSet)
routerq.register('anssmall', AnssmallViewSet)


urlpatterns = [
    path('qnatest/', include(routerq.urls)),
    path('board/qna/', views.qna_list_create),
    path('qna/', views.qna_list_create),
    path('qna/<int:qna_pk>/', views.qna_detail_update_delete),
    path('qna/<int:qna_pk>/anss/', views.create_ans),
    path('qna_like/<int:qna_pk>/', views.like),
    path('qna_bookmark/<int:qna_pk>/', views.bookmark),
    path('qna_solved/<int:ans_pk>/', views.solve),
 
    path('ans/', views.ans_list),
    path('ans/<int:ans_pk>/', views.ans_detail_update_delete),
    path('ans_like/<int:ans_pk>/', views.like_ans),

    path('qna_small/', views.qna_list_small),
    path('qna_small/<int:qnasmall_pk>/', views.qna_detail_update_delete_small),

    path('ans_small/', views.ans_list_small),  
    path('ans_small/<int:anssmall_pk>/', views.ans_detail_update_delete_small),
]
