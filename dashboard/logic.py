from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone


def apamanager(user):
    return user.groups.filter(name='Manager').exists()


def bagianapa(user):
    return user.last_name


def anggotabagian(nama_manager, bagian):
    User = get_user_model()
    users = User.objects.filter(
        last_name=bagian).exclude(first_name=nama_manager)
    return users


def delete_user(user_id):
    User = get_user_model()
    users = User.objects.filter(pk=user_id)
    users.delete()


def inputtugasstaff(nama_staff, judul, isi, status, jenis):
    sekarang = timezone.now()
    t = Tugas(
        nama_staff,
        judul,
        isi,
        status,
        jenis,
        dibuat_pada=sekarang
    )
    t.save()


def dapatkantugas(user_id):
    pengguna = User.objects.get(pk=user_id)
    tugasnya = pengguna.tugas_set.all()

    tugas_rutin = []
    tugas_proyek = []

    for tugas in tugasnya:
        if tugas.status != "On Progress":
            continue
        elif tugas.jenis == "Rutin":
            dibuat_pada = tugas.formatwaktu(tugas.dibuat_pada)
            tugas_rutin.append(
                [tugas, tugas.deadline_tugas(), tugas.progressnya(), dibuat_pada, tugas.status])
        elif tugas.jenis == "Proyek":
            dibuat_pada = tugas.formatwaktu(tugas.dibuat_pada)
            tugas_proyek.append(
                [tugas, tugas.deadline_tugas(), tugas.progressnya(), dibuat_pada, tugas.status])
    return (tugas_rutin, tugas_proyek)


def tugasselesai(user_id):
    pengguna = User.objects.get(pk=user_id)
    tugasnya = pengguna.tugas_set.all()
    tugas_selesai = []

    for tugas in tugasnya:
        if tugas.status == "Selesai":
            selesai_pada = tugas.formatwaktu(tugas.selesai_pada)
            tugas_selesai.append([tugas, selesai_pada])

    return tugas_selesai


def tugasdeadline(user_id):
    pengguna = User.objects.get(pk=user_id)
    tugasnya = pengguna.tugas_set.all()
    tugas_deadline = []

    for tugas in tugasnya:
        if tugas.status == "Deadline":
            tugas_deadline.append(
                [tugas.judul, tugas.formatwaktu(tugas.deadline), tugas.id])

    return tugas_deadline


def detailtugas(tugas_id):
    tugasnya = Tugas.objects.get(pk=tugas_id)
    judulnya = tugasnya.judul
    isinya = tugasnya.isi
    dibuat_pada = tugasnya.formatwaktu(tugasnya.dibuat_pada)
    statusnya = tugasnya.status
    deadlinenya = tugasnya.formatwaktu(tugasnya.deadline)
    selesainya = tugasnya.progressnya()

    return {
        "judul": judulnya,
        "isi": isinya,
        "dibuat_pada": dibuat_pada,
        "status": statusnya,
        "deadline": deadlinenya,
        "selesai": selesainya
    }


def ngecekdeadline():
    tugas = Tugas.objects.all()
    for a in tugas:
        deadline = a.deadline
        saat_ini = timezone.now()
        apakah_deadline = (deadline - saat_ini)
        if (apakah_deadline.days < 0):
            a.status = "Deadline"
            a.save()
