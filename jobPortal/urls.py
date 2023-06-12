from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('Job', JobAPIView.as_view(
        {
            "get": "get",
            "post": "create",
            "patch": "update",
            "delete": "destroy"
        }
    )
         ),
         path('Skill', SkillAPIView.as_view(
        {
            "get": "get",
            "post": "create",
            "patch": "update",
            "delete": "destroy"
        }
    )
         ),
]