# Imports from other dependencies.
from rest_framework import serializers


# Imports from election.
from election.models import Election


class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = "__all__"
