from django.urls import include, path
from . import views

urlpatterns = [
    path('',
        views.InterestList.as_view(),
        name='interest-list'),
]

