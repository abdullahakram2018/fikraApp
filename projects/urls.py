from django.urls import path
from projects import views
urlpatterns = [
    path('project',views.project,name='project'),
    path('branch', views.branch,name='branch'),
]