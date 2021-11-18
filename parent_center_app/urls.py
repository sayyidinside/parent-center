from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard_admin/', views.dashboardAdmin, name='dashboard admin'), 
    path('data_siswa/', views.dataSiswa, name='data siswa'), 
]
