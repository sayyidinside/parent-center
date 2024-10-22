from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
from .utils import custom_jadwal, custom_user, custom_absen, custom_adm, custom_guru
from .utils import custom_kelas, custom_mapel, custom_siswa, custom_spp, custom_tugas
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Mapel(models.Model):
    id_mapel = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=custom_mapel,
        editable=False
    )
    nama = models.CharField(max_length=50)

    class jenis_mapel(models.TextChoices):
        A = 'A', 'A. Muatan Nasional'
        B = 'B', 'B. Muatan Kewilayahan'
        C1 = 'C1', 'C1. Muatan Peminatan Kejuruan'
        C2 = 'C2', 'C2. Dasar Program Keahlian'
        C3 = 'C3', 'C3. Kompetensi Keahlian'

    jenis = models.CharField(
        max_length=30,
        choices=jenis_mapel.choices,
        default=jenis_mapel.A
    )

    def __str__(self):
        return self.nama


class Kelas(models.Model):
    id_kelas = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=custom_kelas,
        editable=False
    )

    class rentang_kelas(models.TextChoices):
        X = 'X'
        XI = 'XI'
        XII = 'XII'

    kelas = models.CharField(
        max_length=3,
        choices=rentang_kelas.choices,
        default=rentang_kelas.X
    )

    class jurusan(models.TextChoices):
        TITL = 'TITL', 'Teknik Intalasi Tenaga Listrik'
        TP = 'TP', 'Teknik Pemesinan'
        TKR = 'TKR', 'Teknik Kendaraan Ringan'
        TKJ = 'TKJ', 'Teknik Komputer Jaringan'
        RPL = 'RPL', 'Rekayasa Perangkat Lunak'
        TBSM = 'TBSM', 'Teknik dan Bisnis Sepeda Motor'

    jurusan = models.CharField(
        max_length=30,
        choices=jurusan.choices,
        default=jurusan.TITL
    )
    no_kelas = models.SmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f'{self.kelas} { self.get_jurusan_display() } {self.no_kelas}'


class ExtendUser(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    id_user = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_user,
        editable=False
    )

    class user_level(models.TextChoices):
        ADMIN = 'Admin'
        GURU = 'Guru'
        ORTU = 'Orang Tua'

    user_level = models.CharField(
        max_length=10,
        choices=user_level.choices,
        default=user_level.GURU
    )

    def __str__(self):
        return f'{self.user_level} | {self.user.username}'


class Admin(models.Model):
    id_admin = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_adm,
        editable=False
    )
    nama = models.CharField(max_length=50)
    email = models.EmailField(default="example@gmail.com")
    no_tlp = models.CharField(max_length=12)
    alamat = models.TextField(null=True)
    id_user = models.OneToOneField(
        ExtendUser,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.id_user.user.username} | {self.nama}'


class Guru(models.Model):
    id_guru = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_guru,
        editable=False
    )
    nama = models.CharField(max_length=50)
    email = models.EmailField(default="example@gmail.com")
    no_tlp = models.CharField(max_length=12)
    no_induk = models.CharField(max_length=20)
    alamat = models.TextField(null=True)

    class jns_kelamin(models.TextChoices):
        P = 'Perempuan'
        L = 'Laki-Laki'

    jns_kelamin = models.CharField(
        max_length=10,
        choices=jns_kelamin.choices,
        default=jns_kelamin.L)
    id_user = models.OneToOneField(
        ExtendUser,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.no_induk} - {self.nama}'


class Siswa(models.Model):
    nis = models.CharField(max_length=15, null=True)
    nisn = models.CharField(max_length=15, null=True)
    id_siswa = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_siswa,
        editable=False
    )
    nama = models.CharField(max_length=50)
    tpt_lahir = models.CharField(max_length=50)
    tgl_lahir = models.DateField(default=date.today)
    agama = models.CharField(max_length=15)

    class jns_kelamin(models.TextChoices):
        P = 'Perempuan'
        L = 'Laki-Laki'

    jns_kelamin = models.CharField(
        max_length=10,
        choices=jns_kelamin.choices,
        default=jns_kelamin.L
    )
    no_tlp = models.CharField(max_length=13, null=True)
    alamat = models.TextField(null=True)
    id_kelas = models.ForeignKey(
        Kelas,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.nis} - {self.nama}'


class OrangTua(models.Model):
    id_ortu = models.ForeignKey(Siswa, on_delete=CASCADE)
    nama = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    no_tlp = models.CharField(max_length=13)
    alamat = models.TextField(null=True)
    id_user = models.OneToOneField(
        ExtendUser,
        null=True,
        on_delete=models.SET_NULL
    )

    class jns_kelamin(models.TextChoices):
        P = 'Perempuan'
        L = 'Laki-Laki'

    jns_kelamin = models.CharField(
        max_length=10,
        choices=jns_kelamin.choices,
        default=jns_kelamin.L
    )

    def __str__(self):
        return f'{self.nama} | Orangtua dari {self.id_ortu.nama} - {self.id_ortu.nis}'


class Tugas(models.Model):
    id_tugas = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_tugas,
        editable=False
    )
    id_mapel = models.ForeignKey(Mapel, on_delete=CASCADE)
    id_kelas = models.ForeignKey(Kelas, on_delete=CASCADE)
    id_guru = models.ForeignKey(
        Guru,
        null=True,
        on_delete=models.SET_NULL
    )
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return f'''{self.id_mapel.nama} |
                   {self.id_kelas.kelas} {self.id_kelas.jurusan} {self.id_kelas.no_kelas} |
                   {self.nama} |
                   {self.keterangan}'''


class NilaiTugas(models.Model):
    id_tugas = models.ForeignKey(Tugas, on_delete=CASCADE)
    id_siswa = models.ForeignKey(Siswa, on_delete=CASCADE)
    nilai = models.IntegerField()

    def __str__(self):
        return f'''{self.id_tugas.id_mapel.nama} |
                   {self.id_tugas.id_kelas.kelas} {self.id_tugas.id_kelas.jurusan}
                   {self.id_tugas.id_kelas.no_kelas} |
                   {self.id_tugas.nama} |
                   {self.id_siswa.nama} |
                   {self.nilai}'''


class Absen(models.Model):
    id_absen = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_absen,
        editable=False
    )
    id_mapel = models.ForeignKey(Mapel, on_delete=CASCADE)
    id_kelas = models.ForeignKey(Kelas, on_delete=CASCADE)
    id_guru = models.ForeignKey(
        Guru,
        null=True,
        on_delete=models.SET_NULL
    )
    tgl = models.DateField(default=date.today)
    pertemuan = models.IntegerField()

    def __str__(self):
        return f'''{self.id_kelas.kelas} {self.id_kelas.jurusan} {self.id_kelas.no_kelas} |
                   {self.id_mapel.nama} |
                   Pertemuan ke {self.pertemuan} |
                   {self.tgl}'''


class DaftarAbsen(models.Model):
    id_absen = models.ForeignKey(Absen, on_delete=CASCADE)
    id_siswa = models.ForeignKey(Siswa, on_delete=CASCADE)

    class keterangan(models.TextChoices):
        H = 'H', 'Hadir'
        A = 'A', 'Alfa'
        I = 'I', 'Izin'
        S = 'S', 'Sakit'

    keterangan = models.CharField(
        max_length=10,
        choices=keterangan.choices,
        default=keterangan.H
    )

    def __str__(self):
        return f'''{self.id_absen.id_kelas.kelas} {self.id_absen.id_kelas.no_kelas}
                   {self.id_absen.id_kelas.jurusan} |
                   {self.id_absen.id_mapel.nama} |
                   Pertemuan ke {self.id_absen.pertemuan} |
                   {self.id_absen.tgl} |
                   {self.id_siswa.nama} |
                   {self.keterangan}'''


class PembayaranSPP(models.Model):
    id_pembayaran = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_spp,
        editable=False
    )
    id_siswa = models.ForeignKey(Siswa, on_delete=CASCADE)
    tgl_bayar = models.DateField(default=date.today)
    bulan_ke = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12),
                                                            MinValueValidator(1)])
    jumlah = models.PositiveBigIntegerField()
    thn_ajar = models.CharField(max_length=10, default='2012/2022')

    class Semesteran(models.TextChoices):
        ganjil = '1', 'Ganjil',
        genap = '2', 'Genap'

    semester = models.CharField(
        max_length=10,
        choices=Semesteran.choices,
        default=Semesteran.ganjil)

    def __str__(self):
        return f'''{self.id_siswa.nama} |
                   Lunas Rp. {self.jumlah} |
                   Tahun ajar {self.thn_ajar} |
                   Semester {self.semester}'''


class Jadwal(models.Model):
    id_jadwal = models.CharField(
        max_length=30,
        primary_key=True,
        unique=True,
        default=custom_jadwal,
        editable=False
    )
    id_kelas = models.ForeignKey(Kelas, on_delete=CASCADE)
    id_mapel = models.ForeignKey(Mapel, on_delete=CASCADE)
    id_guru = models.ForeignKey(Guru, null=True, on_delete=models.SET_NULL)

    class hari(models.TextChoices):
        SENIN = 'Senin'
        SELASA = 'Selasa'
        RABU = 'Rabu'
        Kamis = 'Kamis'
        JUMAT = 'Jumat'

    hari = models.CharField(
        max_length=10,
        choices=hari.choices,
        default=hari.SENIN
    )
    jumlah_jam = models.IntegerField()
    mulai = models.TimeField(null=True)
    selesai = models.TimeField(null=True)

    def __str__(self):
        return f'''{self.id_kelas.kelas} {self.id_kelas.jurusan} {self.id_kelas.no_kelas} |
                   Hari {self.hari} |
                   Jam {self.mulai} - {self.selesai} WIB |
                   Guru {self.id_guru.nama}'''
