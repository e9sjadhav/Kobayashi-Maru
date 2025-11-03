from django.urls import path, include
from .views import TeamListView, MatchDetailsApi,MatchListView

# urlpatterns = [
#     path('', MatchSummary.as_view(), name='match-list'),
#     path('<str:team_name>/', MatchDetail.as_view(), name='match-deatil'),
# ]

urlpatterns = [
    path('', TeamListView.as_view(), name='match-list'),
    path('<str:team_name>/', MatchDetailsApi.as_view(), name='match-details'),
    path('matches/', MatchListView.as_view(), name='matches'),
]