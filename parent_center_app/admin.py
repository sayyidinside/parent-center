from django.contrib import admin
from .models import Jadwal, mapel, Kelas, Extend_User, Admin, Guru, Siswa, OrangTua, Tugas, NilaiTugas, Absen, DaftarAbsen, PembayaranSPP

# Register your models here.
class MapelAdmin(admin.ModelAdmin):
    readonly_fields=['id_mapel',]

class ConAdmin(admin.ModelAdmin):
    readonly_fields=['id_admin',]

class KelasAdmin(admin.ModelAdmin):
    readonly_fields=['id_kelas',]

class GuruAdmin(admin.ModelAdmin):
    readonly_fields=['id_guru',]

class SiswaAdmin(admin.ModelAdmin):
    readonly_fields=['id_siswa',]

class UserAdmin(admin.ModelAdmin):
    readonly_fields=['id_user',]

class TugasAdmin(admin.ModelAdmin):
    readonly_fields=['id_tugas',]

class AbsenAdmin(admin.ModelAdmin):
    readonly_fields=['id_absen',]

class SppAdmin(admin.ModelAdmin):
    readonly_fields=['id_pembayaran',]

class JadwalAdmin(admin.ModelAdmin):
    readonly_fields=['id_jadwal',]

admin.site.register(mapel, MapelAdmin)
admin.site.register(Admin, ConAdmin)
admin.site.register(Kelas, KelasAdmin)
admin.site.register(Guru, GuruAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.register(OrangTua)
admin.site.register(Extend_User, UserAdmin)
admin.site.register(Tugas, TugasAdmin)
admin.site.register(Absen, AbsenAdmin)
admin.site.register(PembayaranSPP, SppAdmin)
admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(NilaiTugas)
admin.site.register(DaftarAbsen)