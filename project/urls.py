from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import StaticViewSitemap
from .views import HomeView, ApplyView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your Api",
        default_version="v1",
        description="Test Description",
        contact=openapi.Contact(email="abc@abc.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("tournament.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

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
    # path('', HomeView.as_view(), name='home'),
    path('apply/', ApplyView.as_view(), name='apply'),
]
