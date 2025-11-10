from django import forms

from .models import Match, TeamMatch, Team


class TeamMatchForm(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ["team", "match", "batting_score", "batting_wickets", "batting_overs"]
       
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["date"]
