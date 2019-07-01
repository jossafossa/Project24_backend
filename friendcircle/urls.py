from django.urls import include, path

from . import views

urlpatterns = [
    path('',
        views.FriendCircleListView.as_view(),
        name='friendcircle-list'),
    path('<int:pk>',
        views.FriendCircleDetailView.as_view(),
        name='friendcircle-detail'),
    path('getCandidateFriendCircle',
        views.GetMatchCandidateFriendCircle.as_view(),
        name='get-CandidateFriendcircle'),
    path('getCandidateUser/<int:pk>',
        views.GetMatchCandidateUser.as_view(),
        name='get-CandidateUser'),
    path('GetMyMemberships',
        views.GetMyMemberships.as_view(),
        name='get-mymemberships'),
    path('SwipeCandidateFriendCircle',
        views.SwipeCandidateFriendCircle.as_view(),
        name='swipecandidatefriendcircle'),
    path('SwipeCandidateUser/<int:pk>',
        views.SwipeCandidateUser.as_view(),
        name='swipecandidateuser'),
]
