from django.urls import path, include
from . import views
from .views import home_view
from .views import register, login_view, dashboard_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]