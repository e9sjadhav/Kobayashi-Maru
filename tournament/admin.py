from django.contrib import admin
from .models import Team, TeamMatch, Match
# Register your models here.

admin.site.register(Team)
admin.site.register(TeamMatch)
admin.site.register(Match)