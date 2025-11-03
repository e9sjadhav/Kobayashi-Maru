from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TeamMatch, Team
from .forms import TeamMatchForm
from django.shortcuts import get_object_or_404

# Create your views here.
class MatchSummary(ListView):
    model = TeamMatch
    template_name = "tournament/team_list.html"
    context_object_name = "summary"

class MatchDetail(DetailView):
    model = Team
    template_name = "tournament/team_view.html"
    context_object_name = "matchdetails"

    def get_object(self):
        team_name = self.kwargs.get('team_name')
        return get_object_or_404(Team,country=team_name)

class MatchCreate(CreateView):
    model = TeamMatch
    form_class = TeamMatchForm
    template_name = "tournament/team_view.html"