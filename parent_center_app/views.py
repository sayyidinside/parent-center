from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    return render(request,
                  'parent_center_app/dashboard_admin.html',
                  {'title': 'Dashboard'})


@login_required(login_url='login')
def dataSiswa(request):
    return render(request,
                  'parent_center_app/data_siswa.html',
                  {'title': 'Data Siswa'})


@login_required(login_url='login')
def dataGuru(request):
    return render(request,
                  'parent_center_app/data_guru.html',
                  {'title': 'Data Guru'})


@login_required(login_url='login')
def dataOrangtua(request):
    return render(request,
                  'parent_center_app/data_orangtua.html',
                  {'title': 'Data Orang Tua / Wali'})
