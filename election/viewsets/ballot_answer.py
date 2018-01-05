from election.models import BallotAnswer
from election.serializers import BallotAnswerSerializer
from election.utils.api_auth import PermissionedViewSet


class BallotAnswerViewSet(PermissionedViewSet):
    queryset = BallotAnswer.objects.all()
    serializer_class = BallotAnswerSerializer
