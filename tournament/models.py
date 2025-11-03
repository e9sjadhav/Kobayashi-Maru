from django.db import models

# Create your models here.
class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    def matches_played(self)->int:
        return self.team_matches.count()
    
    
    def matches_won(self)->int:
        return self.team_matches.filter(won=True).count()
    
    def matches_lost(self)->int:
        return self.team_matches.filter(lost=True).count()
    
    def __str__(self):
        return f"country:{self.country}"
    


class Match(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"country:{self.date}"

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()