# Generated by Django 3.1.3 on 2020-12-16 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_datakaryawan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datakaryawan',
            name='status_lamaran',
        ),
    ]