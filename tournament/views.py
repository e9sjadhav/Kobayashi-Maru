from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from .models import Match, Team, TeamMatch
from .serializer import TeamSerializer,MatchSerializer
from drf_yasg.utils import swagger_auto_schema


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @swagger_auto_schema(request_body=TeamSerializer)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class TeamMatchDetailsApi(APIView):
    serializer_class = TeamSerializer

    def get(self, request, team_name):

        print("team_name",team_name)
        try:
            team_name = Team.objects.get(country=team_name)
            print("team_name",team_name)
            serializer = TeamSerializer(team_name)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
    

class TeamMatchListView(ListAPIView):
    serializer_class = TeamSerializer

    @swagger_auto_schema(request_body=TeamSerializer)
    def get_queryset(self):
        try:
            team_name = self.request.query_params.get('team_name')
            team = Team.objects.get(country=team_name)
            queryset = TeamMatch.objects.filter(team=team)
            serializer = TeamSerializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "matches not found"},status=status.HTTP_404_NOT_FOUND)
        
# match api views

class MatchListView(ListAPIView):
    queryset = TeamMatch.objects.all()
    serializer_class = MatchSerializer

    @swagger_auto_schema(request_body=MatchSerializer)
    def post(self,request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MatchDetailsView(APIView):

    def get(self,request,match_id):
        try:
            match_id = TeamMatch.objects.get(id=match_id)
            print(match_id)
            serializer = MatchSerializer(match_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)