from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Guru, Siswa

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
    context = {
        'title': 'Dashboard',
        'Jml_guru': jml_guru,
        'Jml_siswa_x':jml_siswa_x,
        'Jml_siswa_xi':jml_siswa_xi,
        'Jml_siswa_xii':jml_siswa_xii,
    }
    return render(request,
                  'parent_center_app/dashboard_admin.html',
                  context)


@login_required(login_url='login')
def dataSiswa(request):
    return render(request,
                  'parent_center_app/data_siswa.html',
                  {'title': 'Data Siswa'})

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
    return render(request,
                  'parent_center_app/data_guru.html',
                  {'title': 'Data Guru'})

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
    return render(request,
                  'parent_center_app/data_orangtua.html',
                  {'title': 'Data Orang Tua / Wali'})

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