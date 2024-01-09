# Generated by Django 4.0.5 on 2022-07-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groupbreaks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakname', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=20)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
            options={
                'verbose_name': 'Group break',
                'verbose_name_plural': 'Group breaks',
            },
        ),
        migrations.CreateModel(
            name='Groupclasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Group class',
                'verbose_name_plural': 'Group classes',
            },
        ),
        migrations.CreateModel(
            name='Grouproutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=20)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
            options={
                'verbose_name': 'Group routine',
                'verbose_name_plural': 'Group routines',
            },
        ),
        migrations.CreateModel(
            name='GroupSpecifiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=20)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
            options={
                'verbose_name': 'Group specificationr',
                'verbose_name_plural': 'Group specificationrs',
            },
        ),
        migrations.CreateModel(
            name='Groupsubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Group subject',
                'verbose_name_plural': 'Group subjects',
            },
        ),
        migrations.CreateModel(
            name='Groupsubjectteachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nooflessonsperweek', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Group subject teacher',
                'verbose_name_plural': 'Group subject teachers',
            },
        ),
        migrations.CreateModel(
            name='SchoolGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('lessonduration', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
    ]