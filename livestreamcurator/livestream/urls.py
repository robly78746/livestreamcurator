from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'livestream'

urlpatterns = [
    path('', TemplateView.as_view(template_name="livestream/home.html"), name='home'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/add/', views.addStream, name='add'),
    path('<str:username>/delete/', views.deleteStream, name='delete'),
    path('<str:username>/edit/<str:streamer>/', views.editStream, name='edit'),
    path('<str:username>/group/create/', views.groupCreate, name='group_create'),
]