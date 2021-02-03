from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('profilewrite', PostViewSet)

urlpatterns = [
    path('profile/', include(router.urls)),
    path('profiles/', views.profile_list_create),
    path('profiles/<int:profile_pk>/', views.profile_detail_update_delete),

]
