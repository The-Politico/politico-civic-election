# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import ElectionType


class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        fields = "__all__"
