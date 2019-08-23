# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import BallotMeasure


class BallotMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallotMeasure
        fields = "__all__"
