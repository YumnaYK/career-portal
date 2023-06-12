from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from user_authentication.user_controllers import *
from  user_authentication.user_controllers import *

login_controller = CustomAuthToken()
change_password_controller = ChangePasswordController()
forget_password_controller = ForgetPasswordController()
verify_otp = VerifyOtpController()

class LoginAPIView(viewsets.ModelViewSet):

    serializer_class = LoginSerializer

    def post(self, request):
        return login_controller.post(request)

class ChangePasswordAPI(viewsets.ModelViewSet):
   
    serializer_class = ChangePasswordSerializer

    def patch(self, request):
        return change_password_controller.update(request)    
    
class ForgetPasswordAPI(viewsets.ModelViewSet):

    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        return forget_password_controller.forget_password(request)
    
class VerifyOtpAPI(viewsets.ModelViewSet):
    
    serializer_class = VerifyOtpSerializer

    def post(self, request):
        return verify_otp.verify(request)