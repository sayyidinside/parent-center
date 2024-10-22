from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import DaftarAbsen, Guru, Jadwal, Kelas, Mapel, NilaiTugas
from .models import OrangTua, Siswa, ExtendUser, PembayaranSPP
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import SiswaForm, RegisterForm, GuruForm, OrangTuaForm, SppForm
from .forms import JadwalForm, MapelForm, KelasForm


# Create your views here.
def level_login(current_user) -> str:
    """funtion to render correct dashboard according to user level

    Args:
        current_user (obj): current login user

    Returns:
        sritng: dashboard url to redirect
    """
    match current_user.user.extenduser.user_level:
        case 'Admin':
            return '/dashboard_admin/hari%20ini'
        case 'Guru':
            return 'dashboard guru'
        case _:
            return 'jadwal kbm siswa'


def level_permission(current_user, level: list) -> bool:
    """function to resricted user to access the page if level not met

    Args:
        current_user (obj): current login user
        level (list): correct user levels to access page

    Returns:
        boolean: True or False to if statment
    """
    if current_user.user.extenduser.user_level in level:
        return True
    else:
        return False


def get_day(plus: int = 0) -> str:
    """funtion to get current day in bahasa

    Returns:
        str: name of the day
    """
    match timezone.localtime().isoweekday() + plus:
        case 1:
            return 'Senin'
        case 2:
            return 'Selasa'
        case 3:
            return 'Rabu'
        case 4:
            return 'Kamis'
        case _:
            return 'Jumat'


def login_user(request):
    if request.user.is_authenticated:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(level_login(request))
            else:
                messages.error(request, 'Username or Password is incorrect')
        return render(request, 'parent_center_app/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboardAdmin(request, condition='hari ini'):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        jml_siswa_x = Siswa.objects.filter(id_kelas__kelas='X').count()
        jml_siswa_xi = Siswa.objects.filter(id_kelas__kelas='XI').count()
        jml_siswa_xii = Siswa.objects.filter(id_kelas__kelas='XII').count()
        jml_guru = Guru.objects.count()

        match condition:
            case 'kemarin':
                num = -1
            case 'hari ini':
                num = 0
            case 'besok':
                num = 1
            case _:
                num = 2

        hari_ini = get_day(num)
        jadwal = Jadwal.objects.all().order_by('id_kelas', 'mulai').filter(hari=hari_ini)

        time_limit = timezone.localtime() - timezone.timedelta(hours=3)
        admin_active = User.objects.filter(last_login__gte=time_limit,
                                           extenduser__user_level='Admin'
                                           ).order_by('last_login').reverse()[:5]
        guru_active = User.objects.filter(last_login__gte=time_limit,
                                          extenduser__user_level='Guru'
                                          ).order_by('last_login').reverse()[:5]
        ortu_active = User.objects.filter(last_login__gte=time_limit,
                                          extenduser__user_level='Orang Tua'
                                          ).order_by('last_login').reverse()[:5]

        context = {
            'tanggal': timezone.localtime(),
            'hari': hari_ini,
            'title': 'Dashboard',
            'Jml_guru': jml_guru,
            'Jml_siswa_x': jml_siswa_x,
            'Jml_siswa_xi': jml_siswa_xi,
            'Jml_siswa_xii': jml_siswa_xii,
            'jadwal': jadwal,
            'admin_active': admin_active,
            'guru_active': guru_active,
            'ortu_active': ortu_active
        }
        return render(request,
                      'parent_center_app/dashboard_admin.html',
                      context)


@login_required(login_url='login')
def dataSiswa(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
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
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            form = SiswaForm(request.POST)
            if form.is_valid():
                siswa = form.save(commit=False)
                siswa.save()
                return redirect('data siswa')
        else:
            form = SiswaForm()

        context = {
            'form': form,
            'title': 'Tambah Siswa'
        }
        return render(request,
                      'parent_center_app/detail_siswa.html',
                      context)


@login_required(login_url='login')
def detailSiswa(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        siswa = get_object_or_404(Siswa, pk=pk)
        if request.method == 'POST':
            form = SiswaForm(request.POST, instance=siswa)
            if form.is_valid():
                siswa = form.save(commit=False)
                siswa.save()
                return redirect('data siswa')
        else:
            form = SiswaForm(instance=siswa)

        context = {
            'form': form,
            'siswa': siswa,
            'title': 'Detail Siswa'
        }
        return render(request,
                      'parent_center_app/detail_siswa.html',
                      context)


@login_required(login_url='login')
def dataGuru(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
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
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            user_form = RegisterForm(request.POST)
            guru_form = GuruForm(request.POST)
            if user_form.is_valid() and guru_form.is_valid():
                user_form = user_form.save(commit=False)
                user_form.email = guru_form.cleaned_data.get('email')
                user_form.save()
                guru_form = guru_form.save(commit=False)
                ExtendUser.objects.update_or_create(user=user_form,
                                                    user_level='Guru')
                guru_form.id_user = ExtendUser.objects.get(user=user_form)
                guru_form.save()
                return redirect('data guru')
            else:
                messages.error(request, user_form.errors)
        else:
            user_form = RegisterForm()
            guru_form = GuruForm()

        context = {
            'user_form': user_form,
            'guru_form': guru_form,
            'title': 'Tambah Guru'
        }
        return render(request,
                      'parent_center_app/tambah_guru.html',
                      context)


@login_required(login_url='login')
def detailGuru(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        guru = get_object_or_404(Guru, pk=pk)
        if request.method == 'POST':
            form = GuruForm(request.POST, instance=guru)
            if form.is_valid():
                guru = form.save(commit=False)
                guru.save()
                return redirect('data guru')
        else:
            form = GuruForm(instance=guru)

        context = {
            'title': 'Detail Guru',
            'form': form
        }
        return render(request,
                      'parent_center_app/detail_guru.html',
                      context)


@login_required(login_url='login')
def dataOrangtua(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
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
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            user_form = RegisterForm(request.POST)
            ortu_form = OrangTuaForm(request.POST)
            if user_form.is_valid() and ortu_form.is_valid():
                user_form = user_form.save(commit=False)
                user_form.save()
                ortu_form = ortu_form.save(commit=False)
                ExtendUser.objects.update_or_create(user=user_form,
                                                    user_level='Orang Tua')
                ortu_form.id_user = ExtendUser.objects.get(user=user_form)
                ortu_form.save()
                return redirect('data orang tua')
            else:
                messages.error(request, user_form.errors)
        else:
            user_form = RegisterForm()
            ortu_form = OrangTuaForm()

        context = {
            'title': 'Tambah Orang Tua / Wali',
            'user_form': user_form,
            'ortu_form': ortu_form
        }
        return render(request,
                      'parent_center_app/tambah_orangtua.html',
                      context)


@login_required(login_url='login')
def detailOrangtua(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        ortu = get_object_or_404(OrangTua, pk=pk)
        if request.method == 'POST':
            form = OrangTuaForm(request.POST, instance=ortu)
            if form.is_valid():
                ortu = form.save(commit=False)
                ortu.save()
                return redirect('data orang tua')
        else:
            form = OrangTuaForm(instance=ortu)

        context = {
            'title': 'Detail Orang Tua / Wali',
            'form': form
        }
        return render(request,
                      'parent_center_app/detail_orangtua.html',
                      context)


@login_required(login_url='login')
def dataMapel(request, pk=None):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        mapel_detail = Mapel.objects.filter(pk=pk).first()
        mapel = Mapel.objects.filter().order_by('nama')
        if mapel_detail is None:
            if request.method == 'POST':
                form = MapelForm(request.POST)
                if form.is_valid():
                    form.save()
            else:
                form = MapelForm()
        else:
            form = MapelForm(request.POST, instance=mapel_detail)

        context = {
            'title': 'Mata Pelajaran',
            'mapel': mapel,
            'form': form
        }
        return render(request,
                      'parent_center_app/data_mapel.html',
                      context)


def edit_mapel(request, pk=None):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        form = get_object_or_404(Mapel, pk=pk)
        # if request.method == 'POST':
        #     form = MapelForm(request.POST, instance=pelajaran)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('data orang tua')
        # else:
        #     form = MapelForm(instance=pelajaran)
        context = {'form': form}
    return render(request,
                  'parent_center_app/data_mapel.html',
                  context)


@login_required(login_url='login')
def dataKelas(request, pk=None):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        kelas_detail = Kelas.objects.filter(pk=pk).first()
        kelas = Kelas.objects.all().order_by('kelas')
        if kelas_detail is None:
            if request.method == 'POST':
                form = KelasForm(request.POST)
                if form.is_valid():
                    form.save()
            else:
                form = KelasForm()
        else:
            form = KelasForm(request.POST, instance=kelas_detail)

        context = {'title': 'Kelas',
                   'daftar_kelas': kelas,
                   'form': form
                   }
        return render(request,
                      'parent_center_app/data_kelas.html',
                      context)


@login_required(login_url='login')
def profileAdmin(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        context = {'title': 'Profile'}
        return render(request,
                      'parent_center_app/profile_admin.html',
                      context)


@login_required(login_url='login')
def cariSpp(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        context = {'title': 'Data SPP'}
        return render(request,
                      'parent_center_app/cari_spp.html',
                      context)


@login_required(login_url='login')
def bayarSpp(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            form = SppForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('data spp')
        else:
            form = SppForm()

        context = {
            'title': 'Bayar SPP',
            'form': form
        }
        return render(request,
                      'parent_center_app/tambah_spp.html',
                      context)


@login_required(login_url='login')
def dataSpp(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        form = PembayaranSPP.objects.all().order_by('tgl_bayar').reverse()

        context = {
            'title': 'Data SPP',
            'form': form
        }
        return render(request,
                      'parent_center_app/data_spp.html',
                      context)


@login_required(login_url='login')
def jadwalKbm(request, kelas='kls-22112021001556824333'):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        daftar_jadwal = Jadwal.objects.all().filter(id_kelas=kelas).order_by('hari').reverse()
        kelass = Kelas.objects.all().order_by('kelas', 'jurusan', 'no_kelas')
        selected = kelas
        context = {
            'title': 'Jadwal KBM',
            'daftar_jadwal': daftar_jadwal,
            'Kelass': kelass,
            'selected': selected
        }
        return render(request,
                      'parent_center_app/jadwal_kbm.html',
                      context)


@login_required(login_url='login')
def tambahKbm(request):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        if request.method == 'POST':
            form = JadwalForm(request.POST)
            if form.is_valid():
                jadwal = form.save(commit=False)
                jadwal.save()
                kls = request.POST.get('id_kelas')
                return redirect('jadwal kbm', kelas=kls)
        else:
            form = JadwalForm()

        context = {
            'title': 'Tambah Jadwal KBM',
            'form': form
        }
        return render(request,
                      'parent_center_app/tambah_kbm.html',
                      context)


@login_required(login_url='login')
def biodataSiswa(request):
    if level_permission(request, ['Admin', 'Orang Tua']) is False:
        return redirect(level_login(request))
    else:
        ortu = request.user.extenduser.orangtua.id_ortu.pk
        siswa = get_object_or_404(Siswa, pk=ortu)
        form = SiswaForm(instance=siswa)
        context = {
            'form': form,
            'siswa': siswa,
            'title': 'Biodata'
        }
        return render(request,
                      'parent_center_app/biodata_siswa.html',
                      context)


@login_required(login_url='login')
def kbmSiswa(request):
    if level_permission(request, ['Admin', 'Orang Tua']) is False:
        return redirect(level_login(request))
    else:
        ortu = request.user.extenduser.orangtua.id_ortu.pk
        siswa = get_object_or_404(Siswa, pk=ortu)
        kelas = siswa.id_kelas
        jadwal = Jadwal.objects.all().order_by('hari').filter(id_kelas=kelas).reverse()
        context = {
            'title': 'Jadwal KBM Siswa',
            'jadwal': jadwal,
            'siswa': siswa
        }
        return render(request,
                      'parent_center_app/jadwal_kbm_siswa.html',
                      context)


@login_required(login_url='login')
def riwayatSpp(request):
    if level_permission(request, ['Admin', 'Orang Tua']) is False:
        return redirect(level_login(request))
    else:
        siswa = request.user.extenduser.orangtua.id_ortu.pk
        spp = PembayaranSPP.objects.all().order_by('thn_ajar').filter(id_siswa=siswa).reverse()

        context = {
            'title': 'Riwayat Pembayaran SPP Siswa',
            'spp': spp
        }
        return render(request,
                      'parent_center_app/riwayat_spp.html',
                      context)


@login_required(login_url='login')
def absensiSiswa(request, mapel='pel-23112021085749532504'):
    if level_permission(request, ['Admin', 'Orang Tua']) is False:
        return redirect(level_login(request))
    else:
        pelajaran = Mapel.objects.all().order_by('nama')
        siswa = request.user.extenduser.orangtua.id_ortu.pk
        absen = DaftarAbsen.objects.all().filter(id_siswa=siswa,
                                                 id_absen__id_mapel=mapel).reverse()
        selected = mapel
        context = {
            'title': 'Absensi Siswa',
            'pelajaran': pelajaran,
            'absen': absen,
            'selected': selected
        }
        return render(request,
                      'parent_center_app/absensi_siswa.html',
                      context)


@login_required(login_url='login')
def nilaiSiswa(request, mapel='pel-23112021085749532504'):
    if level_permission(request, ['Admin', 'Orang Tua']) is False:
        return redirect(level_login(request))
    else:
        pelajaran = Mapel.objects.all().order_by('nama')
        siswa = request.user.extenduser.orangtua.id_ortu.pk
        nilai = NilaiTugas.objects.all().filter(id_siswa=siswa,
                                                id_tugas__id_mapel=mapel).reverse()
        selected = mapel
        context = {
            'title': 'Nilai Siswa',
            'pelajaran': pelajaran,
            'nilai': nilai,
            'selected': selected
        }
        return render(request,
                      'parent_center_app/nilai_siswa.html',
                      context)


@login_required(login_url='login')
def dashboardGuru(request):
    if level_permission(request, ['Admin', 'Guru']) is False:
        return redirect(level_login(request))
    else:
        context = {'title': 'Dashboard'}
        return render(request,
                      'parent_center_app/dashboard_guru.html',
                      context)


@login_required(login_url='login')
def delete_siswa(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = Siswa.objects.filter(pk=pk)
        data.delete()
    return redirect('data siswa')


@login_required(login_url='login')
def delete_guru(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = Guru.objects.filter(pk=pk)
        data.delete()
    return redirect('data guru')


@login_required(login_url='login')
def delete_ortu(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = OrangTua.objects.filter(pk=pk)
        data.delete()
    return redirect('data orang tua')


@login_required(login_url='login')
def delete_mapel(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = Mapel.objects.filter(pk=pk)
        data.delete()
    return redirect('data mapel')


@login_required(login_url='login')
def delete_kelas(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = Kelas.objects.filter(pk=pk)
        data.delete()
    return redirect('data kelas')


@login_required(login_url='login')
def delete_spp(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = PembayaranSPP.objects.filter(pk=pk)
        data.delete()
    return redirect('data spp')


@login_required(login_url='login')
def delete_jadwal(request, pk):
    if level_permission(request, ['Admin']) is False:
        return redirect(level_login(request))
    else:
        data = Jadwal.objects.filter(pk=pk)
        data.delete()
    return redirect('jadwal kbm', kelas='kls-22112021001556824333')
