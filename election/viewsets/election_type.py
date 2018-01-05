from election.models import ElectionType
from election.serializers import ElectionTypeSerializer
from election.utils.api_auth import PermissionedViewSet


class ElectionTypeViewSet(PermissionedViewSet):
    queryset = ElectionType.objects.all()
    serializer_class = ElectionTypeSerializer
