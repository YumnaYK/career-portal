from .models import *
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class SkillReuirmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill_Requirement
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    # skill_requirements = SkillReuirmentSerializer(many = True)

    class Meta:
        model = Job
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pay'] = f"PKR {representation['pay']}"
        return representation



