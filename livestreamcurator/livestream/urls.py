from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'livestream'

urlpatterns = [
    path('', TemplateView.as_view(template_name="livestream/home.html"), name='home'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/add/', views.modifyStream, name='add'),
    path('<str:username>/delete/', views.deleteStream, name='delete'),
    path('<str:username>/edit/<str:streamer>/', views.modifyStream, name='edit'),
    path('<str:username>/group/add/', views.modifyGroup, name='group_add'),
    path('<str:username>/group/edit/<str:groupName>/', views.modifyGroup, name='group_edit'),
    path('<str:username>/group/delete/', views.deleteGroup, name='group_delete'),
    path('<str:username>/group/show/<str:groupName>/', views.showGroup, name='group_show'),
    path('<str:username>/group/delete/<str:groupName>/', views.deleteFromGroup, name='group_delete_member'),
]