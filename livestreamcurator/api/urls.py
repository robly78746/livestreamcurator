from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views

from . import views

app_name = 'api'

urlpatterns = [
    path('auth', drf_views.obtain_auth_token, name='auth'),
    path('users/<int:user_id>/follows/livestreams/<int:livestream_id>', views.UserFollowStream.as_view(), name='user_follow_stream'),
    path('users/<int:user_id>/livestreams', views.UserLivestreams.as_view(), name='user_livestreams'),
    path('users', views.Users.as_view(), name='users'),
    path('livestreams/<int:livestream_id>', views.modify_livestream, name='modify_livestream'),
    path('livestreams', views.Livestreams.as_view(), name='livestreams'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)