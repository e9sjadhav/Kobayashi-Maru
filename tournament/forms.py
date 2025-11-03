from django import forms
from .models import TeamMatch

class TeamMatch(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ['team','match','batting_score','batting_wickets','batting_overs']