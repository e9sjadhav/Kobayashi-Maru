from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TeamMatch, Team


# Create your views here.
class MatchSummary(ListView):
    model = TeamMatch
    template_name = "tournament/summary.html"
    context_object_name = "summary"

class MatchDetail(DetailView):
    model = Team
    template_name = "tournament/MatchDetail.html"
    context_object_name = "matchdetails" 