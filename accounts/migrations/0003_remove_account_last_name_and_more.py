# Generated by Django 4.1.3 on 2022-12-19 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postal_code',
        ),
    ]
