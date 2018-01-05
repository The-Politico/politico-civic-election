from election.models import ElectionCycle
from election.serializers import ElectionCycleSerializer
from election.utils.api_auth import PermissionedViewSet


class ElectionCycleViewSet(PermissionedViewSet):
    queryset = ElectionCycle.objects.all()
    serializer_class = ElectionCycleSerializer
