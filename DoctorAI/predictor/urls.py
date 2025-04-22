from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('result/', views.result, name='result'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
