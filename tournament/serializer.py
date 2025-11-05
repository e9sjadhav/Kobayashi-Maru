from rest_framework import serializers

from .models import TeamMatch, Team, Match


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMatch
        fields = "__all__"

class MatchDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"