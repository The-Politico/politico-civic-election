from election.models import ElectionDay
from election.serializers import ElectionDaySerializer
from election.utils.api_auth import PermissionedViewSet


class ElectionDayViewSet(PermissionedViewSet):
    queryset = ElectionDay.objects.all()
    serializer_class = ElectionDaySerializer
