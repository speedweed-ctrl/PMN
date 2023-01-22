from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import *

# in this file i used a deprecated library but if iremove the code from here the endponits wont be grouped under the user tag
schema_view = get_swagger_view(title='user actions endpoints')

urlpatterns = [
    path('',schema_view),
    path('login',MyTokenObtainPairView.as_view() , name='login'),
    path('register' , registerUser , name='register'),
    path('profile' , getUserProfile , name='user profile'),
    path('users',get_allUsers , name='all users'),
]