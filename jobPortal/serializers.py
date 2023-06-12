from .models import *
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Skill
        fields= '__all__'

class SkillReuirmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Skill_Requirement
        fields= '__all__'

class JobSerializer(serializers.ModelSerializer):

    skill_requirements = SkillReuirmentSerializer(many = True)

    class Meta:
        model= Job
        fields = ['id', 'job_title', 'skill_requirements']

    def create(self, validated_data):

        skill_requirements_data = validated_data.pop('skill_requirements')
        job = Job.objects.create(**validated_data)

        for skill_requirement_data in skill_requirements_data:
            skill = Skill.objects.get(id=skill_requirement_data['skill'])
            Skill_Requirement.objects.create(skill=skill, scale=skill_requirement_data['scale'])

        return job




