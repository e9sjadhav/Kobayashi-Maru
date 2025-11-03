from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TeamMatch, Team
from .forms import TeamMatchForm
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializer import TeamSerializer

# Create your views here.
# class MatchSummary(ListView):
#     model = TeamMatch
#     template_name = "tournament/team_list.html"
#     context_object_name = "summary"

# class MatchDetail(DetailView):
#     model = Team
#     template_name = "tournament/team_view.html"
#     context_object_name = "matchdetails"

#     def get(self,request,*args, **kwargs):
#         team_name = self.request.GET.get('team_name')
#         return get_object_or_404(Team,country=team_name)


# class MatchCreate(CreateView):
#     model = TeamMatch
#     form_class = TeamMatchForm
#     template_name = "tournament/team_view.html"


class TeamListView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()
    
    def post(self,request):
        serializer = TeamSerializer(data=request.data)
        return serializer.data

class MatchDetailsApi(APIView):
    serializer_class = TeamSerializer

    def get(self, request, team_name):
        team_name = self.request.GET.get('team_name')
        serializer = TeamSerializer(team_name)
        return serializer.data

class MatchListView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.values('matches')
    
