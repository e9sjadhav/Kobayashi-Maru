from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from .models import Match, Team, TeamMatch
from .serializer import TeamSerializer,TeamMatchSerializer, MatchDateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers



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

        # print("team_name",team_name)
        try:
            team_name = Team.objects.get(country=team_name)
            # print("team_name",team_name)
            serializer = TeamSerializer(team_name)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)


class MyQueryParamSerializer(serializers.Serializer):
    team_name = serializers.CharField()

# curl -X GET http://127.0.0.1:8000/teams/matches/?team_name=c003

class TeamMatchListView(APIView):
    serializer_class = TeamMatchSerializer
    print("started api")
    # @swagger_auto_schema(query_serializer=MyQueryParamSerializer)
    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter(
                'team_name',
                openapi.IN_QUERY,
                description="The new query param",
                type=openapi.TYPE_STRING,
            )])
    def get(self, request):
        print("inside get")
        print("request.GET.get('team_name'):",request.GET.get("team_name"))
        team_name = request.GET.get("team_name")
        print("team name:",team_name)
        
        if team_name:
            team = Team.objects.get(country=team_name)
            print("done team",team)
            matches = TeamMatch.objects.filter(team=team)
            print("matches matches",matches)
            serializer = TeamMatchSerializer(matches,many=True)
            print("serializer",serializer)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
        
        
# match api views
class NewMatchView(APIView):

    @swagger_auto_schema(request_body=MatchDateSerializer)
    def post(self,request):
        serializer = MatchDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MatchListView(ListAPIView):
    queryset = TeamMatch.objects.all()
    serializer_class = TeamMatchSerializer

    @swagger_auto_schema(request_body=TeamMatchSerializer)
    def post(self,request):
        serializer = TeamMatchSerializer(data=request.data)
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
            serializer = TeamMatchSerializer(match_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)