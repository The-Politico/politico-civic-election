from election.models import BallotMeasure
from election.serializers import BallotMeasureSerializer
from election.utils.api_auth import PermissionedViewSet


class BallotMeasureViewSet(PermissionedViewSet):
    queryset = BallotMeasure.objects.all()
    serializer_class = BallotMeasureSerializer
