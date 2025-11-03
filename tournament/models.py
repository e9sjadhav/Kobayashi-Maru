from django.db import models

# Create your models here.
class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)
    matches = models.IntegerField(default=0)
    won = models.IntegerField()
    lost = models.IntegerField()

    # def matches_played(self)->int:
    #     return self.team_matches.count()
    
    
    # def matches_won(self)->int:
    #     return self.team_matches.filter(won=True).count()
    
    # def matches_lost(self)->int:
    #     return self.team_matches.filter(lost=True).count()
    
    def __str__(self):
        return f"country:{self.country} | won:{self.won} | lost{self.lost}"
    


class Match(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"date:{self.date}"

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
    matches = models.IntegerField(default=0)
    won = models.BooleanField(default=False)
    lost = models.BooleanField(default=False)


    def __str__(self):
        return f"team:{self.team.country} | score:{self.batting_score} | wickets:{self.batting_wickets} | overs:{self.batting_overs} | won:{self.won} | lost{self.lost}"