from django.conf import settings

from rest_framework.permissions import AllowAny
from mysite.app_settings import import_callable
from .serializers import UserRegistrationSerializer as DefaultRegisterSerializer


serializers = getattr(settings, 'REST_AUTH_REGISTER_SERIALIZERS', {})

RegisterSerializer = import_callable(
    serializers.get('REGISTER_SERIALIZER', DefaultRegisterSerializer))


def register_permission_classes():
    permission_classes = [AllowAny, ]
    for klass in getattr(settings, 'REST_AUTH_REGISTER_PERMISSION_CLASSES', tuple()):
        permission_classes.append(import_callable(klass))
    return tuple(permission_classes)
