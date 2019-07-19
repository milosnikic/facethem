# Generated by Django 2.1.5 on 2019-01-31 00:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_friends', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('winner', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_no', models.IntegerField()),
                ('player_id', models.CharField(max_length=200)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facethemapp.Match')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('player_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('date', models.DateField(null=True)),
                ('avatar', models.CharField(max_length=200, null=True)),
                ('cover_image', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facethemapp.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='person_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_1', to='facethemapp.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='person_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_2', to='facethemapp.User'),
        ),
    ]