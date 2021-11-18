from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard/', views.dashboardAdmin, name='dashboardAdmin'), 
]
