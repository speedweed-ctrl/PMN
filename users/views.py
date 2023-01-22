from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
#---------------------------------------------------------------------------

#----------------------------------------user views--------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    data = request.data
  
    user = User.objects.create(
            
            first_name=data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password'])
        )
    serializer = UserSerializerWithToken(user , many =False )
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializers = UserSerrializer(user, many=False)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_allUsers(request):
    user = User.objects.all()
    serializers = UserSerrializer(user, many=True)
    return Response(serializers.data)