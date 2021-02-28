from django.urls import path
from .views import UserCreateAPI,UserLoginAPI
urlpatterns = [
    path('login', UserLoginAPI.as_view()),
    path('register', UserCreateAPI.as_view())
]
