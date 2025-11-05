from django.urls import include, path

from .views import TeamMatchDetailsApi, TeamMatchListView, TeamListView,MatchListView,MatchDetailsView,NewMatchView

# urlpatterns = [
#     path('', MatchSummary.as_view(), name='match-list'),
#     path('<str:team_name>/', MatchDetail.as_view(), name='match-deatil'),
# ]

urlpatterns = [
    path("teams/", TeamListView.as_view(), name="match-list"),
    path("teams/matches/", TeamMatchListView.as_view(), name="team-matches"),
    path("teams/<str:team_name>/", TeamMatchDetailsApi.as_view(), name="match-details"),
    path("matches/", MatchListView.as_view(), name="matches"),
    path("matches/create", NewMatchView.as_view(), name="create-matche"),
    path("matches/<int:match_id>/", MatchDetailsView.as_view(), name="matches"),
]
