from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [

    path('register/', views.createUser),
    path('login/', views.login),
    path('auth/', views.auth),
    path('profile/', views.profile),
    path('delete/', views.delete),

    # path('req/', views.req),

    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]



