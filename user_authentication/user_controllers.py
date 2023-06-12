from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from user_authentication.models import User
from user_authentication.serializers import *
from rest_framework.response import Response
import random
from careerPortal.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils import timezone
import threading

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        #serializer = self.serializer_class(data=request.data,
                        #                   context={'request': request})
       # serializer.is_valid(raise_exception=True)
        #user = serializer.validated_data['user']
        user = authenticate(username=request.data.get("email"), password=request.data.get("password"))
        token, created = Token.objects.get_or_create(user=user)
        return Response ({
            'token': token.key,
            'user_id': user.pk,
            'name': user.first_name
        })
    
class ChangePasswordController:
    feature_name = "Change Password"

    serializer_class = ChangePasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request):
        print(request.user)
        
        request.POST._mutable = True
        
        request.data["old_password"] = request.data.get("old_password").strip()
        request.data["new_password"] = request.data.get("new_password").strip()
        request.data["confirm_password"] = request.data.get("confirm_password").strip()
        
        request.POST._mutable = True
        
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        
        if not serializer.is_valid():
            
            return Response(serializer.errors)
       
        if request.data.get('new_password') != request.data.get('confirm_password'):
            
            return Response("PASSWORD DOES NOT MATCH")
        print(request.data.get("old_password"))

        if not request.user.check_password(request.data.get("old_password")):
            
            return Response("INCORRECT_OLD_PASSWORD")

        request.user.set_password(request.data.get("new_password"))
        request.user.save()
        
        
        return Response("SUCCESSFULL")
    
class ForgetPasswordController:
    feature_name = "Forget Password"
    serializer_class = ForgetPasswordSerializer

    def forget_password(self, request):
       
        serialized_data = self.serializer_class(data=request.data)
       
        if not serialized_data.is_valid():
            return Response(serialized_data.errors)
        try:
            user = User.objects.filter(email=request.data.get("email")).first()
            if not user:
                return Response("USER_NOT_FOUND")
            otp = random.SystemRandom().randint(100000, 999999)
            user.otp = otp
            user.otp_generated_at = timezone.now()
            user.save()
            
            subject = "Password Recovery Request"
            message = f"""
                Hi {user.first_name} {user.last_name},
                Your request for password recovery has been received.
                Please use the following otp.
                OTP: {otp}
                """

            recipient_list = [request.data.get("email")]
            t = threading.Thread(target=send_mail, args=(subject, message, EMAIL_HOST_USER, recipient_list))
            t.start()
            return Response("EMAIL_SUCCESSFULLY_SENT")
        except Exception as e:
            print(e)
            return Response(e)
        
class VerifyOtpController:
    feature_name = "Reset Password"
    serializer_class = VerifyOtpSerializer

    def verify(self, request):
        
        request.POST._mutable = True
        
        request.data["new_password"] = request.data.get("new_password").strip()
        request.data["confirm_password"] = request.data.get("confirm_password").strip()
        
        request.POST._mutable = True
        try:
            
            time_delay = timezone.now() - timezone.timedelta(seconds=300)
            user = User.objects.filter(otp=request.data.get("otp"), otp_generated_at__gt=time_delay).first()
            
            if not user:
                return Response("INVALID_OTP")
            
            serialized_data = self.serializer_class(data=request.data, context={"user": user})
            
            if not serialized_data.is_valid():
                return Response(serialized_data.errors)
            
            if request.data.get('new_password') != request.data.get('confirm_password'):
                return Response("PASSWORD_DOES_NOT_MATCH")
            
            user.set_password(request.data.get("new_password"))
            user.otp = None
            user.save()
        
            return Response("SUCCESSFUL")
        except Exception as e:
            print(e)
            return Response(e)