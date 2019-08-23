# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import ElectionCycle


class ElectionCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionCycle
        fields = "__all__"
