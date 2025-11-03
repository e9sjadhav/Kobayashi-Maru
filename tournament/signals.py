from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Team, TeamMatch

@receiver(post_save,sender=TeamMatch)
def update_team_data():
    team = isinstance.team
    played = team.team_matches.count()
    won = team.team_matches.filter(won=True).count()
    lost = team.team_matches.filter(lost=True).count()

    team.matches = played
    team.won = won
    team.lost = lost

    team.save(update_fields=["played","won","lost"])