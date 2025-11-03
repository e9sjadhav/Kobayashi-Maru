from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import StaticViewSitemap
from .views import HomeView, ApplyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', include("tournament.urls")),
]

# Sitemap
sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns += [
    path('sitemap/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap_xml'),
]

urlpatterns += [
    path('', HomeView.as_view(), name='home'),
    path('apply/', ApplyView.as_view(), name='apply'),
]
