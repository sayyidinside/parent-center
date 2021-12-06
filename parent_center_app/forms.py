from django import forms
from .models import Siswa, Guru, OrangTua, Jadwal
# , mapel, PembayaranSPP
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ['nis', 'nisn', 'nama', 'id_kelas', 'jns_kelamin', 'tpt_lahir',
                  'tgl_lahir', 'agama', 'no_tlp', 'alamat']
        widgets = {
            'nis': forms.TextInput(attrs={'class': 'form-control',
                                          'id': 'inputNis',
                                          'name': 'nis',
                                          'required': True}),
            'nisn': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'inputNisn',
                                           'name': 'nisn',
                                           'required': True}),
            'nama': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'inputNama',
                                           'name': 'nama',
                                           'required': True}),
            'id_kelas': forms.Select(attrs={'class': 'select2select form-control',
                                            'id': 'id_kelas',
                                            'name': 'id_kelas'}),
            'jns_kelamin': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'tpt_lahir': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'tpt_lahir',
                                                'name': 'tpt_lahir',
                                                'required': True}),
            'tgl_lahir': forms.DateInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'id': 'tgl_lahir',
                                                'name': 'tgl_lahir',
                                                'required': True}),
            'agama': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'inputAgama',
                                            'name': 'agama',
                                            'required': True}),
            'no_tlp': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'inputTlp',
                                             'name': 'no_tlp',
                                             'required': True}),
            'alamat': forms.Textarea(attrs={'class': 'form-control',
                                            'id': 'inputAlamat',
                                            'name': 'alamat',
                                            'required': True,
                                            'rows': '4'})
        }


class GuruForm(forms.ModelForm):

    class Meta:
        model = Guru
        fields = ('nama', 'email', 'no_tlp', 'no_induk', 'alamat', 'jns_kelamin')
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'inputNama',
                                           'name': 'nama',
                                           'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'example@gmail.com',
                                             'id': 'inputEmail',
                                             'name': 'email',
                                             'required': True}),
            'no_tlp': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'inputNoTlp',
                                             'name': 'no_tlp',
                                             'required': True}),
            'no_induk': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'inputNip',
                                               'name': 'no_induk',
                                               'required': True,
                                               'autofocus': True}),
            'alamat': forms.Textarea(attrs={'class': 'form-control',
                                            'id': 'inputAlamat',
                                            'name': 'alamat',
                                            'required': True,
                                            'rows': '4'}),
            'jns_kelamin': forms.RadioSelect(attrs={'class': 'form-check-input'})
        }


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=16,
        label='Password',
        widget=forms.PasswordInput(attrs={'type': 'password',
                                          'class': 'form-control',
                                          'placeholder': 'Password',
                                          'id': 'inputPassword',
                                          'name': 'password',
                                          'required': True})
    )
    password2 = forms.CharField(
        max_length=16,
        label='Ulangi Password',
        widget=forms.PasswordInput(attrs={'type': 'password',
                                          'class': 'form-control',
                                          'placeholder': 'Ulangi Password',
                                          'id': 'inputPassword2',
                                          'name': 'password',
                                          'required': True})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'id': 'inputUsername',
                                               'name': 'username',
                                               'required': True}),
        }


class OrangTuaForm(forms.ModelForm):

    class Meta:
        model = OrangTua
        fields = ['nama', 'id_ortu', 'keterangan', 'no_tlp', 'alamat', 'jns_kelamin']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'inputNama',
                                           'name': 'nama',
                                           'required': True,
                                           'autofocus': True
                                           }),
            'id_ortu': forms.Select(attrs={'class': 'select2select form-control',
                                           'id': 'id_siswa',
                                           'name': 'siswa'}),
            'keterangan': forms.Textarea(attrs={'class': 'form-control',
                                                'id': 'inputKeterangan',
                                                'rows': '2',
                                                'name': 'keterangan'
                                                }),
            'no_tlp': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'inputNoTlp',
                                             'name': 'no_tlp',
                                             'required': True
                                             }),
            'alamat': forms.Textarea(attrs={'class': 'form-control',
                                            'name': 'alamat',
                                            'id': 'inputAlamat',
                                            'rows': '4',
                                            'required': True
                                            }),
            'jns_kelamin': forms.RadioSelect(attrs={'class': 'form-check-input'})
        }


class JadwalForm(forms.ModelForm):

    class Meta:
        model = Jadwal
        fields = ['id_kelas', 'id_mapel', 'id_guru', 'hari', 'jumlah_jam', 'mulai', 'selesai']
        widgets = {
            'id_kelas': forms.Select(attrs={'class': 'select2select form-control',
                                            'id': 'id_kelas',
                                            'name': 'id_kelas'}),
            'id_mapel': forms.Select(attrs={'class': 'select2select',
                                            'name': 'id_mapel',
                                            'id': 'id_mapel'}),
            'id_guru': forms.Select(attrs={'class': 'select2select',
                                           'name': 'id_guru',
                                           'id': 'id_guru'
                                           }),
            'hari': forms.Select(attrs={'class': 'form-control pl-8',
                                        'name': 'hari',
                                        'id': 'hari'
                                        }),
            'jumlah_jam': forms.NumberInput(attrs={'class': 'form-control',
                                                   'id': 'jp',
                                                   'name': 'jp',
                                                   'min': '1',
                                                   'value': '1',
                                                   'required': True
                                                   }),
            'mulai': forms.TimeInput(attrs={'class': 'form-control',
                                            'type': 'time',
                                            'id': 'jam_mulai',
                                            'nama': 'jam_mulai',
                                            'required': True
                                            }),
            'selesai': forms.TimeInput(attrs={'class': 'form-control',
                                              'type': 'time',
                                              'id': 'jam_selesai',
                                              'nama': 'jam_selesai',
                                              'required': True
                                              })
        }
