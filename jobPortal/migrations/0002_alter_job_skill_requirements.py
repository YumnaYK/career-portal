# Generated by Django 4.2.2 on 2023-06-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skill_requirements',
            field=models.ManyToManyField(blank=True, null=True, to='jobPortal.skill_requirement'),
        ),
    ]