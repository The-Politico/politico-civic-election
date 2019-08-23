# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import BallotAnswer


class BallotAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallotAnswer
        fields = "__all__"
