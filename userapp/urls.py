from django.urls import path
from userapp import views
urlpatterns = [
    path('add_user',views.register_api,name='add_user'),
    path('users/<int:pk>/', views.user_detail,name='user_detail'),
    path('login',views.login_api,name='login'),
    path('user',views.user,name='user'),
]