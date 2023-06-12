# Generated by Django 4.2.2 on 2023-06-12 06:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.IntegerField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobPortal.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=50, unique=True)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateField()),
                ('job_requirements', models.TextField()),
                ('pay', models.FloatField()),
                ('job_location', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('job_mode', models.CharField(max_length=20)),
                ('skill_requirements', models.ManyToManyField(to='jobPortal.skill_requirement')),
            ],
        ),
    ]