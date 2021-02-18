"""api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_url_v1_patterns = [
    url(r'^v1/', include('qnas.urls')),
]

schema_url_v2_patterns = [
    url(r'^v2/', include('events.urls')),
]

schema_url_v3_patterns = [
    url(r'^v3/', include('forums.urls')),
]

schema_url_v4_patterns = [
    url(r'^v4/', include('profiles.urls')),
]


schema_view_v1 = get_schema_view(
    openapi.Info(
        title="대전 102팀",
        default_version='v1',
        description="안녕하세요. 102팀 Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
)

schema_view_v2 = get_schema_view(
    openapi.Info(
        title="대전 102팀",
        default_version='v1',
        description="안녕하세요. 102팀 Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v2_patterns,
)

schema_view_v3 = get_schema_view(
    openapi.Info(
        title="대전 102팀",
        default_version='v1',
        description="안녕하세요. 102팀 Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v3_patterns,
)

schema_view_v4 = get_schema_view(
    openapi.Info(
        title="대전 102팀",
        default_version='v1',
        description="안녕하세요. 102팀 Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v4_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('profiles.urls')),
    path('', include('events.urls')),
    path('', include('qnas.urls')),
    path('', include('forums.urls')),
    path('', include('image_server.urls')),
    url(r'^swagger/qna/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger/event/$', schema_view_v2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger/forum/$', schema_view_v3.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger/profile/$', schema_view_v4.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
