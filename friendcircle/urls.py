from django.urls import include, path

from . import views

urlpatterns = [
    path('',
        views.FriendCircleListView.as_view(),
        name='friendcircle-list'),
    path('<int:pk>',
        views.FriendCircleDetailView.as_view(),
        name='friendcircle-detail'),
    path('getCandidate',
        views.GetMatchCandidateFriendCircle.as_view(),
        name='get-Candidate'),
    path('GetMyMemberships',
        views.GetMyMemberships.as_view(),
        name='get-mymemberships'),
]
