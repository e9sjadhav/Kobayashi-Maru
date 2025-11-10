from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.views.generic import ListView,DetailView,CreateView,View, UpdateView,FormView
from .models import Match, Team, TeamMatch
from .serializer import TeamSerializer,TeamMatchSerializer, MatchDateSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework import serializers
from .forms import TeamMatchForm, MatchForm,TeamForm
from django.urls import reverse_lazy

class TeamListView(FormView):
    model = Team
    template_name = "tournament/team_list.html"
    form_class = TeamForm
    success_url = reverse_lazy("teams")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = Team.objects.all()
        return context

    def form_valid(self, form):
        match = form.save(commit=False)
        match.owner = self.request.user
        match.save()
        return super().form_valid(form)

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
    success_url = reverse_lazy("create-match")
    

class MatchListView(FormView):

    model = TeamMatch
    form_class = TeamMatchForm
    template_name = "tournament/create_match.html"
    success_url = reverse_lazy("matches")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = TeamMatch.objects.all()
        return context

    def form_valid(self, form):
        match = form.save(commit=False)
        match.owner = self.request.user
        match.save()
        return super().form_valid(form)


class MatchUpdateView(UpdateView):

    model = TeamMatch
    form_class = TeamMatchForm
    template_name = "tournament/create_match.html"
    success_url = reverse_lazy("matches")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

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