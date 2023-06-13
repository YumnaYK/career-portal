from django.db import models
from django.utils import timezone
from django.core.validators import MaxFileSizeValidator
from django.core.validators import RegexValidator

# Create your models here

class Job(models.Model):
    job_id = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    due_date = models.DateField() #auto_now=True
    job_requirements = models.TextField()
    pay = models.CharField()
    job_location = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    skill_requirements = models.ManyToManyField("Skill_Requirement", null=True, blank=True)
    job_mode = models.CharField(max_length=25)
    experience = models.CharField(max_length=100, null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Skill_Requirement(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    scale = models.IntegerField()

class Candidate(models.Model):

    TITLE_CHOICES = (
        ('Mr', 'Male'),
        ('Ms', 'Female'),
        ('Mrs', 'Married Women'),
    )
    WORK_CHOICES = (
        ('ON', 'Onsite'),
        ('WFH', 'Home'),
        ('HYB', 'Hybrid'),
    )
    title = models.CharField(max_length=3, choices= TITLE_CHOICES, blank=True) # Mrs,Ms,Mr 
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\+d{3}-\d{3}-\d{7}$', 'Enter a valid contact number in the format "+92-3XZ-YYYYYYY".')]
    )
    resume = models.FileField(validators=[MaxFileSizeValidator(40* 1024 * 1024)])
    work_experience =  models.IntegerField() #in years
    prefered_workmode = models.CharField(max_length=3, choices= WORK_CHOICES) #hybrid,online,WFH
    

class CandidateEducation(models.Model):
