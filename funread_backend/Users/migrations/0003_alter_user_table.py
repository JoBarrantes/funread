# Generated by Django 4.0.2 on 2023-09-18 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_roles'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]