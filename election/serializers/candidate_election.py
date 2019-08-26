# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import CandidateElection


class CandidateElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateElection
        fields = "__all__"
