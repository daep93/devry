from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileList, UpdateUser, UserSignupView, UserLoginView, UserLogoutView, UserInfoView




urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('info/',  UserInfoView.as_view(), name='info'),
    path('profiles/<int:user_id>/', ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:user_id>/update/', UpdateUser.as_view(), name='update_user'),
    path('delete/', views.delete),

    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]



