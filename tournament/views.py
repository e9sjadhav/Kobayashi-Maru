from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.views.generic import ListView,DetailView,CreateView,View
from .models import Match, Team, TeamMatch
from .serializer import TeamSerializer,TeamMatchSerializer, MatchDateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers
from .forms import TeamMatchForm, MatchForm


class TeamListView(ListView):
    model = Team
    template_name = "tournament/team_list.html"
    context_object_name = "summary"

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class TeamMatchDetailsApi(DetailView):

    model = Team
    template_name = "tournament/team_view.html"
    # serializer_class = TeamSerializer


class TeamMatchListView(ListView):
    model = TeamMatch
    template_name = "tournament/team_match.html"
    context_object_name = "matches"

    print("starting")
    def get_queryset(self):
        print("inside get")
        queryset = super().get_queryset()
        print("request.GET.get('team_name'):",self.request.GET.get("team_name"))
        team_name = self.request.GET.get("team_name")
        print("team name:",team_name)
        
        if team_name:
            team = Team.objects.get(country=team_name)
            print("done team",team)
            queryset = queryset.filter(team=team)
            print("matches matches",queryset)
            return queryset
        return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
         
# match api views
class NewMatchView(CreateView):
    model = TeamMatch
    form_class = MatchForm
    template_name = "tournament/create_match_date.html"
    success_url = "create/"
    
    # def post(self,request):
    #     serializer = MatchDateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MatchListView(View):
    # model = Match
    # template_name = "tournament/team_view.html"

    model = TeamMatch
    form_class = TeamMatchForm
    template_name = "tournament/create_match.html"
    success_url = "matches/"

    # def get_queryset(self):
    #     matches =  super().get_queryset()
    #     return matches
    
    # queryset = TeamMatch.objects.all()
    # serializer_class = TeamMatchSerializer
    
    def post(self,request):
        serializer = TeamMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MatchDetailsView(APIView):
    # model = TeamMatch
    # template_name = "tournament/team_view.html"

    # using get method
    def get(self,request,*args, **kwargs):
        match_id = self.kwargs["match_id"]
        print("match_id",match_id)
        try:
            match_id = TeamMatch.objects.get(id=match_id)
            print(match_id)
            serializer = TeamMatchSerializer(match_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)