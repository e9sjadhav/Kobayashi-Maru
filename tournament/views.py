from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TeamMatch, Team
from .forms import TeamMatchForm


# Create your views here.
class MatchSummary(ListView):
    model = TeamMatch
    template_name = "tournament/team_list.html"
    context_object_name = "summary"

class MatchDetail(DetailView):
    model = Team
    template_name = "tournament/MatchDetail.html"
    context_object_name = "matchdetails" 

class MatchCreate(CreateView):
    model = TeamMatch
    form_class = TeamMatchForm
    template_name = "tournament/team_view.html"