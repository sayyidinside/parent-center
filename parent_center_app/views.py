from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Guru, Kelas, OrangTua, Siswa
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard admin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                messages.error(request, 'Username or Password is incorrect')
        return render(request, 'parent_center_app/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboardAdmin(request):
    jml_siswa_x = Siswa.objects.filter(id_kelas__kelas='X').count()
    jml_siswa_xi = Siswa.objects.filter(id_kelas__kelas='XI').count()
    jml_siswa_xii = Siswa.objects.filter(id_kelas__kelas='XII').count()
    jml_guru = Guru.objects.count()
    kelass = Kelas.objects.all().order_by('kelas', 'jurusan', 'no_kelas')

    time_limit = timezone.now() - timezone.timedelta(hours=3)
    admin_active = User.objects.filter(last_login__gte=time_limit,
                                       extend_user__user_level='Admin'
                                       ).order_by('last_login').reverse()[:5]
    guru_active = User.objects.filter(last_login__gte=time_limit,
                                      extend_user__user_level='Guru'
                                      ).order_by('last_login').reverse()[:5]
    ortu_active = User.objects.filter(last_login__gte=time_limit,
                                      extend_user__user_level='Orang Tua'
                                      ).order_by('last_login').reverse()[:5]
    context = {
        'title': 'Dashboard',
        'Jml_guru': jml_guru,
        'Jml_siswa_x': jml_siswa_x,
        'Jml_siswa_xi': jml_siswa_xi,
        'Jml_siswa_xii': jml_siswa_xii,
        'Kelass': kelass,
        'admin_active': admin_active,
        'guru_active': guru_active,
        'ortu_active': ortu_active}
    return render(request,
                  'parent_center_app/dashboard_admin.html',
                  context)


@login_required(login_url='login')
def dataSiswa(request):
    siswas = Siswa.objects.all()
    kelass = Kelas.objects.all().order_by('kelas', 'jurusan', 'no_kelas')
    context = {
        'title': 'Data Siswa',
        'Siswas': siswas,
        'Kelass': kelass,
    }
    return render(request,
                  'parent_center_app/data_siswa.html',
                  context)


@login_required(login_url='login')
def tambahSiswa(request):
    return render(request,
                  'parent_center_app/tambah_siswa.html',
                  {'title': 'Tambah Siswa'})


@login_required(login_url='login')
def detailSiswa(request):
    return render(request,
                  'parent_center_app/detail_siswa.html',
                  {'title': 'Detail Siswa'})


@login_required(login_url='login')
def dataGuru(request):
    gurus = Guru.objects.all()
    context = {
        'title': 'Data Guru',
        'Gurus': gurus,
    }
    return render(request,
                  'parent_center_app/data_guru.html',
                  context)


@login_required(login_url='login')
def tambahGuru(request):
    return render(request,
                  'parent_center_app/tambah_guru.html',
                  {'title': 'Tambah Guru'})


@login_required(login_url='login')
def detailGuru(request):
    return render(request,
                  'parent_center_app/detail_guru.html',
                  {'title': 'Detail Guru'})


@login_required(login_url='login')
def dataOrangtua(request):
    orangTuas = OrangTua.objects.all()
    context = {
        'title': 'Data Orang Tua / Wali',
        'OrangTuas': orangTuas,
    }
    return render(request,
                  'parent_center_app/data_orangtua.html',
                  context)


@login_required(login_url='login')
def tambahOrangtua(request):
    return render(request,
                  'parent_center_app/tambah_orangtua.html',
                  {'title': 'Tambah Orang Tua / Wali'})


@login_required(login_url='login')
def detailOrangtua(request):
    return render(request,
                  'parent_center_app/detail_orangtua.html',
                  {'title': 'Detail Orang Tua / Wali'})


@login_required(login_url='login')
def dataMapel(request):
    return render(request,
                  'parent_center_app/data_mapel.html',
                  {'title': 'Mata Pelajaran'})


@login_required(login_url='login')
def dataKelas(request):
    return render(request,
                  'parent_center_app/data_kelas.html',
                  {'title': 'Kelas'})


@login_required(login_url='login')
def profileAdmin(request):
    return render(request,
                  'parent_center_app/profile_admin.html',
                  {'title': 'Profile'})


@login_required(login_url='login')
def cariSpp(request):
    return render(request,
                  'parent_center_app/cari_spp.html',
                  {'title': 'Data SPP'})


@login_required(login_url='login')
def bayarSpp(request):
    return render(request,
                  'parent_center_app/tambah_spp.html',
                  {'title': 'Bayar SPP'})


@login_required(login_url='login')
def dataSpp(request):
    return render(request,
                  'parent_center_app/data_spp.html',
                  {'title': 'Data SPP X RPL 1'})
@login_required(login_url='login')
def jadwalKbm(request):
    siswas = Siswa.objects.all()
    kelass = Kelas.objects.all().order_by('kelas','jurusan','no_kelas')
    context ={
        'title': 'Jadwal KBM',
        'Siswas' : siswas,
        'Kelass' : kelass,
    }
    return render(request,
                  'parent_center_app/jadwal_kbm.html', context)

@login_required(login_url='login')
def tambahKbm(request):
    return render(request,
                  'parent_center_app/tambah_kbm.html',
                  {'title': 'Tambah Jadwal KBM'})

@login_required(login_url='login')
def biodataSiswa(request):
    return render(request,
                  'parent_center_app/biodata_siswa.html',
                  {'title': 'Biodata Siswa'})

@login_required(login_url='login')
def kbmSiswa(request):
    return render(request,
                  'parent_center_app/jadwal_kbm_siswa.html',
                  {'title': 'Jadwal KBM Siswa'})

@login_required(login_url='login')
def riwayatSpp(request):
    return render(request,
                  'parent_center_app/riwayat_spp.html',
                  {'title': 'Riwayat Pembayaran SPP Siswa'})

@login_required(login_url='login')
def absensiSiswa(request):
    return render(request,
                  'parent_center_app/absensi_siswa.html',
                  {'title': 'Absensi Siswa'})

@login_required(login_url='login')
def nilaiSiswa(request):
    return render(request,
                  'parent_center_app/nilai_siswa.html',
                  {'title': 'Nilai Siswa'})