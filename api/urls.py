from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns([
    path('',
        views.api_root),
    path('rest-auth/',
        include('rest_auth.urls')),
    path('rest-auth/registration/',
        include('rest_auth.registration.urls')),
    path('users/',
        include('users.urls')),
    path('friendcircle',
        include('friendcircle.urls')),
    path('prikmuur/',
        include('prikmuur.urls')),
    path('interests/',
        include('interests.urls')),
])
