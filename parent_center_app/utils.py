from datetime import datetime


def custom_user():
    id = "usr-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_adm():
    id = "adm-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_guru():
    id = "gru-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_siswa():
    id = "sis-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_kelas():
    id = "kls-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_tugas():
    id = "tgs-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_absen():
    id = "abs-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_spp():
    id = "spp-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_mapel():
    id = "pel-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id


def custom_jadwal():
    id = "jad-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id
