from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views

from . import views

app_name = 'api'

urlpatterns = [
    path('auth', drf_views.obtain_auth_token, name='auth'),
    path('users', views.Users.as_view(), name='users'),
    path('users/<int:user_id>/livestreams', views.UserLivestreams.as_view(), name='user_livestreams'),
    path('livestreams/<int:pk>', views.Livestreamer.as_view(), name='update_livestream'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)