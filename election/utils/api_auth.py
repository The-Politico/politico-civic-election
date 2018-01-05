from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

from .api_pagination import ResultsPagination


class PermissionedViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    pagination_class = ResultsPagination
