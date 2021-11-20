from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard_admin/', views.dashboardAdmin, name='dashboard admin'),
    path('data_siswa/', views.dataSiswa, name='data siswa'),
    path('tambah_siswa/', views.tambahSiswa, name='tambah siswa'),
    path('detail_siswa/', views.detailSiswa, name='detail siswa'),
    path('data_guru/', views.dataGuru, name='data guru'),
    path('tambah_guru/', views.tambahGuru, name='tambah guru'),
    path('detail_guru/', views.detailGuru, name='detail guru'),
    path('data_orangtua/', views.dataOrangtua, name='data orang tua'),
    path('tambah_orangtua/', views.tambahOrangtua, name='tambah orangtua'),
    path('detail_orangtua/', views.detailOrangtua, name='detail orangtua'),
    path('logout/', views.logout_user, name='logout'),
]
