# Generated by Django 4.0.2 on 2022-11-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('StudentsGroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsgroups',
            name='userId',
            field=models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, related_name='idUser', to='Users.user'),
        ),
    ]