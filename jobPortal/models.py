from django.db import models
from django.utils import timezone


# Create your models here

class Job(models.Model):
    job_id = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    due_date = models.DateField(auto_now=True)
    job_requirements = models.TextField()
    pay = models.CharField()
    job_location = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    skill_requirements = models.ManyToManyField("Skill_Requirement", null=True, blank=True)
    job_mode = models.CharField(max_length=20)


class Skill(models.Model):
    name = models.CharField(max_length=50)


class Skill_Requirement(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    scale = models.IntegerField()
