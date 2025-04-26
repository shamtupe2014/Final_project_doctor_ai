from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('result/', views.result, name='result'),
    #path('', views.homepage, name='home'),
    path('', views.login_view, name='login'),
    #path('register/', views.register_view, name='register'),
]