from rest_framework import serializers

from .models import TeamMatch, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMatch
        fields = "__all__"
