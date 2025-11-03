from django import forms
from .models import TeamMatch, Match

class TeamMatchForm(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ['team','match','batting_score','batting_wickets','batting_overs']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["date"]