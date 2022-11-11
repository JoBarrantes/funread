# Generated by Django 4.0.2 on 2022-11-08 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('GradesID', models.AutoField(primary_key=True, serialize=False)),
                ('BooksID', models.CharField(max_length=200)),
                ('Progress', models.IntegerField(blank=True, null=True)),
                ('Grade', models.FloatField(blank=True, null=True)),
                ('iduser', models.ForeignKey(db_column='iduser', on_delete=django.db.models.deletion.CASCADE, related_name='iduser', to='Users.user')),
            ],
        ),
    ]