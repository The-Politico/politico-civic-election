# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import ElectionEvent


class ElectionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionEvent
        fields = "__all__"
