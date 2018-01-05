from election.models import Candidate
from election.serializers import CandidateSerializer
from election.utils.api_auth import PermissionedViewSet


class CandidateViewSet(PermissionedViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
