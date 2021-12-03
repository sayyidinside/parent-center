from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard_admin/', views.dashboardAdmin, name='dashboard admin'),
    path('data_siswa/', views.dataSiswa, name='data siswa'),
    path('tambah_siswa/', views.tambahSiswa, name='tambah siswa'),
    path('detail_siswa/<str:pk>', views.detailSiswa, name='detail siswa'),
    path('data_guru/', views.dataGuru, name='data guru'),
    path('tambah_guru/', views.tambahGuru, name='tambah guru'),
    path('detail_guru/', views.detailGuru, name='detail guru'),
    path('data_orangtua/', views.dataOrangtua, name='data orang tua'),
    path('tambah_orangtua/', views.tambahOrangtua, name='tambah orangtua'),
    path('detail_orangtua/', views.detailOrangtua, name='detail orangtua'),
    path('data_mapel/', views.dataMapel, name='data mapel'),
    path('data_kelas/', views.dataKelas, name='data kelas'),
    path('profile_admin/', views.profileAdmin, name='profile admin'),
    path('logout/', views.logout_user, name='logout'),
    path('cari_spp/', views.cariSpp, name='data spp'),
    path('tambah_spp/', views.bayarSpp, name='bayar spp'),
    path('data_spp/', views.dataSpp, name='data spp'),
    path('jadwal_kbm/', views.jadwalKbm, name='jadwal kbm'),
    path('tambah_kbm/', views.tambahKbm, name='tambah jadwal kbm'),
    # orangtua
    path('biodata_siswa/', views.biodataSiswa, name='profil siswa'),
    path('jadwal_kbm_siswa/', views.kbmSiswa, name='jadwal kbm siswa'),
    path('riwayat_spp/', views.riwayatSpp, name='riwayat spp siswa'),
    path('absensi_siswa/', views.absensiSiswa, name='absensi siswa'),
    path('nilai_siswa/', views.nilaiSiswa, name='nilai siswa'),
    # guru
    path('dashboard_guru/', views.dashboardGuru, name='dashboard guru'),
]
