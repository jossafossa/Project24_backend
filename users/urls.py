from django.urls import include, path

from . import views

urlpatterns = [
    path('',
        views.UserListView.as_view(),
        name='user-list'),
    path('<int:pk>',
        views.UserDetailView.as_view(),
        name='customuser-detail'),
    path('GetMyUser',
        views.GetMyUser.as_view(),
        name='getmyuser'),
#    path('getUser',
#        views.GetMatchCandidateUser.as_view(),
#        name='get-user'),
]
