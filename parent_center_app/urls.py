from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard_admin/', views.dashboardAdmin, name='dashboard admin'),
    path('data_siswa/', views.dataSiswa, name='data siswa'),
    path('data_guru/', views.dataGuru, name='data guru'),
    path('tambah_guru/', views.tambahGuru, name='tambah guru'),
    path('data_orangtua/', views.dataOrangtua, name='data orang tua'),
    path('logout/', views.logout_user, name='logout'),
]
