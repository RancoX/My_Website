from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings


class IUsernameOrEmailModelBackend(ModelBackend):
    UserModel = get_user_model()
    def authenticate(self, request, username=None, password=None):
        try:
            user = self.UserModel.objects.get(username__iexact=username) or self.UserModel.objects.get(email__iexact=username)
        except self.UserModel.DoesNotExist:
            messages.error(request,'The provided login credentials is invalid,please try again') 
            return redirect(settings.LOGIN_URL)

        if user.check_password(password):
            return user

        return None
    
    def get_user(self, user_id):
        return self.UserModel.get(pk=user_id)