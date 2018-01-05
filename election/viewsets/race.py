from election.models import Race
from election.serializers import RaceSerializer
from election.utils.api_auth import PermissionedViewSet


class RaceViewSet(PermissionedViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
