from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from requests import request
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

#from firebase_auth.authentication import FirebaseAuthentication
from .models import UserProfile
from .serializers import UpdateUserProfile, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from firebase_auth.authentication import custom_firebase_authentication
from itertools import chain
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# Class based view to Get User Details using Token Authentication


def user_details(request):
    auth_user=custom_firebase_authentication(request)
    if auth_user:
        try:
            #print(auth_user.username)
            #data = UserProfile.objects.select_related("user").filter(user__username=auth_user.username)
            data = User.objects.filter(username=auth_user.username).values()
            data_profile = UserProfile.objects.filter(user__username=auth_user.username).values()
            result_list = list(chain(data, data_profile))
            #data = User.objects.filter(username=auth_user.username).values()
            return JsonResponse({"success":True, "data":list(result_list) })
        except Exception as e:
            return JsonResponse({"success":False, "message":f"{e}"})
    else:
        return JsonResponse({"success":False, "message":f"{e}"})
    
        


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    lookup_field = 'user'

    # def get(self, request):
    #     user = self.get_object()
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    def get(self):
        user = User.objects.filter(username=self.request.user)
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#def get_user_details(request):


class UserListAPI(generics.ListAPIView):
    #authentication_classes = (FirebaseAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class ProfileUpdateAPIView(generics.UpdateAPIView):
    #authentication_classes = (TokenAuthentication,)
    
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UpdateUserProfile
    lookup_field = 'user__username'

    def update(self, request, *args, **kwargs):
        auth_user=custom_firebase_authentication(request)
        if auth_user:
            try:
                instance = self.get_object()
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Profile updated successfully"})
                else:
                    return Response({"message": "failed", "details": serializer.errors})
            except Exception as e:
                return JsonResponse({"success":False, "message":f"{e}"})
        else:
            return JsonResponse({"success":False, "message":f"{e}"})



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TestCallBackURL(APIView):
    def get(self, request):
        print(1)

#CALLBACK_URL_YOU_SET_ON_GOOGLE="http://localhost:8000//"
class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/"
    client_class = OAuth2Client
