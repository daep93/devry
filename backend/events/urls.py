from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet


router = routers.DefaultRouter()
router.register('eventwrite', PostViewSet)

urlpatterns = [
    path('event/', include(router.urls)),
    path('events/', views.event_list_create),
    path('events/<int:event_pk>/', views.event_detail_update_delete),
]
