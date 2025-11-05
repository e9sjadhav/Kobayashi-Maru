from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class AuditLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"created_at:{self.created_at}"
    

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)
    matches = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    teammatch = GenericRelation('TeamMatch')
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"country:{self.country} | matches:{self.matches} | won:{self.won} | lost:{self.lost} | points:{self.points}"


class Match(models.Model):
    date = models.DateField()
    # teammatch = GenericRelation('TeamMatch')
    log = GenericRelation(AuditLog)


    def __str__(self):
        return f"date:{self.date}"


class TeamMatch(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_matches"
    )
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="team_matches"
    )
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
    won = models.BooleanField(default=False)
    lost = models.BooleanField(default=False)
    log = GenericRelation(AuditLog)

    
    def __str__(self):
        return f"team:{self.team.country} | score:{self.batting_score} | wickets:{self.batting_wickets} | overs:{self.batting_overs} | won:{self.won} | lost:{self.lost}"

