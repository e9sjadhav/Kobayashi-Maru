from django.urls import include, path

from .views import TeamMatchDetailsApi, TeamMatchListView, TeamListView,MatchListView,MatchDetailsView

# urlpatterns = [
#     path('', MatchSummary.as_view(), name='match-list'),
#     path('<str:team_name>/', MatchDetail.as_view(), name='match-deatil'),
# ]

urlpatterns = [
    path("teams/", TeamListView.as_view(), name="match-list"),
    path("teams/<str:team_name>/", TeamMatchDetailsApi.as_view(), name="match-details"),
    path("teams/matches/", TeamMatchListView.as_view(), name="team-matches"),
    path("matches/", MatchListView.as_view(), name="matches"),
    path("matches/<int:match_id>/", MatchDetailsView.as_view(), name="matches"),
]
