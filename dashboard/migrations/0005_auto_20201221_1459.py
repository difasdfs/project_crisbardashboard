# Generated by Django 3.1.3 on 2020-12-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_datakaryawan_lama_bekerja'),
    ]

    operations = [
        migrations.AddField(
            model_name='datakaryawan',
            name='alasan_keluar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='datakaryawan',
            name='tanggal_keluar',
            field=models.DateField(null=True, verbose_name='Tanggal Keluar'),
        ),
    ]
