from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',
        views.PostList.as_view(),
        name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$',
       views.PostDetail.as_view(),
       name='post-detail'),
    path('getGroup/<int:pk>',
        views.PostList.as_view(),
        name='post-list'),
]
