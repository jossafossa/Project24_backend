from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),

    path('prikmuur/', views.PostList.as_view()),
    path('prikmuur/<int:pk>', views.PostDetail.as_view()),
]
