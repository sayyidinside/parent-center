from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('dashboard_admin/<str:condition>', views.dashboardAdmin, name='dashboard admin'),
    path('data_siswa/', views.dataSiswa, name='data siswa'),
    path('tambah_siswa/', views.tambahSiswa, name='tambah siswa'),
    path('detail_siswa/<str:pk>', views.detailSiswa, name='detail siswa'),
    path('data_siswa/delete/<str:pk>', views.delete_siswa, name='delete siswa'),
    path('data_guru/', views.dataGuru, name='data guru'),
    path('tambah_guru/', views.tambahGuru, name='tambah guru'),
    path('detail_guru/<str:pk>', views.detailGuru, name='detail guru'),
    path('data_guru/delete/<str:pk>', views.delete_guru, name='delete guru'),
    path('data_orangtua/', views.dataOrangtua, name='data orang tua'),
    path('tambah_orangtua/', views.tambahOrangtua, name='tambah orangtua'),
    path('detail_orangtua/<int:pk>', views.detailOrangtua, name='detail orangtua'),
    path('data_orangtua/delete/<str:pk>', views.delete_ortu, name='delete orangtua'),
    path('data_mapel/', views.dataMapel, name='data mapel'),
    path('data_mapel/edits/<str:pk>', views.edit_mapel, name='edit mapel'),
    path('data_mapel/delete/<str:pk>', views.delete_mapel, name='delete mapel'),
    path('data_kelas/', views.dataKelas, name='data kelas'),
    path('data_kelas/delete/<str:pk>', views.delete_kelas, name='delete kelas'),
    path('profile_admin/', views.profileAdmin, name='profile admin'),
    path('logout/', views.logout_user, name='logout'),
    path('cari_spp/', views.cariSpp, name='cari spp'),
    path('tambah_spp/', views.bayarSpp, name='bayar spp'),
    path('data_spp/', views.dataSpp, name='data spp'),
    path('data_spp/delete/<str:pk>', views.delete_spp, name='delete spp'),
    path('jadwal_kbm/<str:kelas>', views.jadwalKbm, name='jadwal kbm'),
    path('tambah_kbm/', views.tambahKbm, name='tambah jadwal kbm'),
    path('jadwal_kbm/delete/<str:pk>', views.delete_jadwal, name='delete jadwal'),
    # orangtua
    path('biodata_siswa/', views.biodataSiswa, name='profil siswa'),
    path('jadwal_kbm_siswa/', views.kbmSiswa, name='jadwal kbm siswa'),
    path('riwayat_spp/', views.riwayatSpp, name='riwayat spp siswa'),
    path('absensi_siswa/<str:mapel>', views.absensiSiswa, name='absensi siswa'),
    path('nilai_siswa/<str:mapel>', views.nilaiSiswa, name='nilai siswa'),
    # guru
    path('dashboard_guru/', views.dashboardGuru, name='dashboard guru'),
]
