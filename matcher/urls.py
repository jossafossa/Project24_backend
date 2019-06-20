from django.urls import include, path
from . import views

urlpatterns = [
    path('getUser/',
        views.GetMatchCandidateGroup.as_view(),
        name='get-user'),
]

