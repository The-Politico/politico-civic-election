# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import ElectionDay


class ElectionDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionDay
        fields = "__all__"
