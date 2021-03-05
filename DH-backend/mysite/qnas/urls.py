from django.urls import path
from .views import (
   QnaCreateAPI,
   QnaListAPI
)
urlpatterns = [
    path('', QnaCreateAPI.as_view()),
    path('list', QnaListAPI.as_view()),
]
