from django.urls import include, path
from .views import GoogleLogin, ProfileUpdateAPIView, TestCallBackURL, UserDetailAPI, RegisterUserAPIView, FacebookLogin, UserListAPI, user_details

urlpatterns = [
  #path("get-details/",UserDetailAPI.as_view()),
  path("get-list-users/",UserListAPI.as_view()),
  path("get-details/",user_details),
  path('register/',RegisterUserAPIView.as_view()),
  path('profile-update/<str:user__username>', ProfileUpdateAPIView.as_view()),
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),
  path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
  path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
  path('google-callback-url/', TestCallBackURL.as_view(), name='google_login_back'),
]