from django.contrib import admin

from .models import Match, Team, TeamMatch

# Register your models here.

admin.site.register(Team)
admin.site.register(TeamMatch)
admin.site.register(Match)
