from .models import *
from .serializers import *
from rest_framework.response import Response  

class SkillController:
    serializer_class = SkillSerializer   

    def get_skill(self, request):
        kwargs = {}
        id = request.data.get("id")
        if id:
            kwargs["id"] = id
        mydata = self.serializer_class.Meta.model.objects.filter(**kwargs)
        serialized_data = self.serializer_class(mydata, many=True).data
        return Response(serialized_data)
    
    def create_skill(self, request):  
        serializer = self.serializer_class(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data)  
        else:  
            return Response(serializer.errors)
    
    def update_skill(self, request):
        
        emp = self.serializer_class.Meta.model.objects.filter(id=request.data.get("id")).first()
        serialized_data = self.serializer_class(instance = emp, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        
    def delete_skill(self, request):
        id = request.data.get("id")
        if not id:
            return Response("ID_NOT_PROVIDED")
        instance = self.serializer_class.Meta.model.objects.filter(id=request.data.get("id"))
        if not instance.first():
            return Response("NOT FOUND")
        instance.delete()
        return Response("DELETED SUCCESFULLY")