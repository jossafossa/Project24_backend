from django.urls import include, path
from . import views

urlpatterns = [
    path('',
        views.PostList.as_view(),
        name='prikmuur-list'),
    path('<int:pk>',
        views.PostDetail.as_view(),
        name='post-detail'),
]
