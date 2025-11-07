from django.urls import include, path

from .views import TeamMatchDetailsApi, TeamMatchListView, TeamListView,MatchListView,MatchDetailsView,NewMatchView,MatchUpdateView

# urlpatterns = [
#     path('', MatchSummary.as_view(), name='match-list'),
#     path('<str:team_name>/', MatchDetail.as_view(), name='match-deatil'),
# ]

urlpatterns = [
    path("teams/", TeamListView.as_view(), name="match-list"),
    path("teams/matches/", TeamMatchListView.as_view(), name="team-matches"),
    path("teams/<int:pk>/", TeamMatchDetailsApi.as_view(), name="match-details"),
    path("matches/", MatchListView.as_view(), name="matches"),
    path("matches/create/", NewMatchView.as_view(), name="create-match"),
    path("matches/update/<int:pk>/", MatchUpdateView.as_view(), name="update-match"),
    path("matches/<int:match_id>/", MatchDetailsView.as_view(), name="matches"),
]

#Generic detail view TeamMatchDetailsApi must be called with either an object pk or a slug in the URLconf.
