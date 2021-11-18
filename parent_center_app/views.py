from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_user')
            else:
                messages.error(request, 'Username or Password is incorrect')
        return render(request, 'parent_center_app/login.html', {})


def dashboardAdmin(request):
    return render(request, 'parent_center_app/dashboardAdmin.html', {'title':'Dashboard'})
