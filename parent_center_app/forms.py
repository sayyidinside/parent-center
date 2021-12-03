from django import forms
from .models import Siswa, Kelas
# , Guru, OrangTua, mapel, PembayaranSPP
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# dynamic choices
classes = Kelas.objects.all().values_list('kelas', 'kelas').order_by('kelas')
class_list = [clas for clas in classes]


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ('nis', 'nisn', 'nama', 'id_kelas', 'jns_kelamin', 'tpt_lahir',
                  'tgl_lahir', 'agama', 'no_tlp', 'alamat')
        widgets = {'nis': forms.TextInput(attrs={'class': 'form-control',
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
                                                   'rows': '4'})}
