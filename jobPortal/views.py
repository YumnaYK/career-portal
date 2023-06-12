from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *
from .jobs_controller import *
from .skill_controller import *

jobs_controller = JobController()
skill_controller = SkillController()

class JobAPIView(viewsets.ModelViewSet):

    serializer_class = JobSerializer

    def get(self, request):
        return jobs_controller.get_job(request)

    def create(self, request):
        return jobs_controller.create_job(request)

    def update(self, request):
        return jobs_controller.update_job(request)

    def destroy(self, request):
        return jobs_controller.delete_job(request)
    
class SkillAPIView(viewsets.ModelViewSet):

    serializer_class = SkillSerializer

    def get(self, request):
        return skill_controller.get_skill(request)

    def create(self, request):
        return skill_controller.create_skill(request)

    def update(self, request):
        return skill_controller.update_skill(request)

    def destroy(self, request):
        return skill_controller.delete_skill(request)