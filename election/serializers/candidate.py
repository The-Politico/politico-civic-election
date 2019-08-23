# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
