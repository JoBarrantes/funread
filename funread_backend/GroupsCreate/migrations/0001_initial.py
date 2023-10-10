# Generated by Django 4.0.2 on 2023-10-06 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('Media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsCreate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('createdat', models.DateTimeField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
                ('idimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Media.media')),
            ],
            options={
                'db_table': 'groupscreate',
            },
        ),
    ]