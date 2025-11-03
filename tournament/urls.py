from django.urls import path, include
from .views import MatchCreate, MatchDetail,MatchSummary

urlpatterns = [
    path('', MatchSummary.as_view(), name='match-list'),
    path('<str:team_name>/', MatchDetail.as_view(), name='match-deatil'),
]