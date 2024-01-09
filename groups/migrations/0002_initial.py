# Generated by Django 4.0.5 on 2022-07-03 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolgroups',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school'),
        ),
        migrations.AddField(
            model_name='groupsubjectteachers',
            name='groupsubjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.groupsubjects'),
        ),
        migrations.AddField(
            model_name='groupsubjectteachers',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teachers'),
        ),
        migrations.AddField(
            model_name='groupsubjectteachers',
            name='theclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.groupclasses'),
        ),
        migrations.AddField(
            model_name='groupsubjects',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.schoolgroups'),
        ),
        migrations.AddField(
            model_name='groupsubjects',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subjects'),
        ),
        migrations.AddField(
            model_name='groupspecifiction',
            name='groupsubjectteachers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.groupsubjectteachers'),
        ),
        migrations.AddField(
            model_name='grouproutine',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.schoolgroups'),
        ),
        migrations.AddField(
            model_name='groupclasses',
            name='classteacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teachers'),
        ),
        migrations.AddField(
            model_name='groupclasses',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.schoolgroups'),
        ),
        migrations.AddField(
            model_name='groupclasses',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.streams'),
        ),
        migrations.AddField(
            model_name='groupbreaks',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.schoolgroups'),
        ),
    ]
