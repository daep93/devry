from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PostViewSet


router = routers.DefaultRouter()
router.register('eventwrite', PostViewSet)

urlpatterns = [
    path('eventtest/', include(router.urls)),
    path('board/event/main/', views.event_main_list),
    path('board/event/', views.event_list),
    path('event/', views.event_list_create),
    path('event/<int:event_pk>/', views.event_detail_update_delete),
    path('event_bookmark/<int:event_pk>/', views.bookmark),
]
