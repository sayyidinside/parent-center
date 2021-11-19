import secrets
from datetime import datetime

def custom_id(user):
    if user == "admin":
        id = "adm-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "siswa":
        id = "sis-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "guru":
        id = "gru-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "user":
        id = "usr-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "kelas":
        id = "kls-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "tugas":
        id = "tgs-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    elif user == "absen":
        id = "abs-"+datetime.now().strftime('%d%m%Y%H%M%S%f') 
    elif user == "spp":
        id = "spp-"+datetime.now().strftime('%d%m%Y%H%M%S%f')   
    else:
        id = "mpl-"+datetime.now().strftime('%d%m%Y%H%M%S%f')
    return id