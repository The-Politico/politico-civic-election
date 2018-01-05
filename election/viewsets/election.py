from election.models import Election
from election.serializers import ElectionSerializer
from election.utils.api_auth import PermissionedViewSet


class ElectionViewSet(PermissionedViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
