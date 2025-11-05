from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Team, TeamMatch


@receiver(post_save, sender=TeamMatch)
def update_team_data(sender, instance, created, **kwargs):
    print("*******signal****")
    team = instance.team
    matches = team.team_matches.count()
    won = team.team_matches.filter(won=True).count()
    lost = team.team_matches.filter(lost=True).count()
    points = won *2

    team.matches = matches
    team.won = won
    team.lost = lost
    team.points = points
    team.save(update_fields=["matches", "won", "lost","points"])
