from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from snippets import views as snippets_views

# Provide schema
schema_view = get_schema_view(title='YOUR RESTFUL API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', snippets_views.SnippetViewSet)
router.register(r'users', snippets_views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

urlpatterns = [
    # API basic
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/schema/$', schema_view),
    url(r'^api/auth/', include('rest_framework.urls')),
    # admin
    url(r'^admin/', admin.site.urls)
]
