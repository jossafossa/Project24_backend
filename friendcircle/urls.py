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
    path('SwipeCandidateFriendCircle',
        views.SwipeCandidateFriendCircle.as_view(),
        name='swipecandidatefriendcircle'),
    path('<int:pk>/SwipeCandidateUser',
        views.SwipeCandidateUser.as_view(),
        name='swipecandidateuser'),

]
