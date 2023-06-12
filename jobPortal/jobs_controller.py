from .models import *
from .serializers import *
from rest_framework.response import Response  
from rest_framework import status

class JobController:
    serializer_class = JobSerializer   


    def get_job(self, request):
        kwargs = {}
        id = request.data.get("id")
        if id:
            kwargs["id"] = id
        mydata = self.serializer_class.Meta.model.objects.filter(**kwargs)
        serialized_data = self.serializer_class(mydata, many=True).data
        return Response(serialized_data)
    
    def create_job(self, request):  
        skill_requirements = request.data.pop("skills_data")
        skills_lst = []
        for skills in skill_requirements:
            serialized_skills = SkillReuirmentSerializer(data=skills)
            #breakpoint()
            if serialized_skills.is_valid(): 
                saved_data = serialized_skills.save() 
                print(saved_data.id)
                skills_lst.append(saved_data.id)
        
        request.POST._mutable = True
        request.data['skill_requirements'] = skills_lst
        print(request.data)
        serializer = self.serializer_class(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_job(self, request):
        
        emp = self.serializer_class.Meta.model.objects.filter(id=request.data.get("id")).first()
        serialized_data = self.serializer_class(instance = emp, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        
    def delete_job(self, request):
        id = request.data.get("id")
        if not id:
            return Response("ID_NOT_PROVIDED")
        instance = self.serializer_class.Meta.model.objects.filter(id=request.data.get("id"))
        if not instance.first():
            return Response("NOT FOUND")
        instance.delete()
        return Response("DELETED SUCCESFULLY")