# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import Race


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"
