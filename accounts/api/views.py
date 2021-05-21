from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.parsers import (
                                    JSONParser,
                                    MultiPartParser,
                                    FormParser,
                                    )

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    )


User = get_user_model()


from .serializers import (
    UserLoginSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    )
 
from django.db.models import Q
 
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
) 
 

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )


#User Login
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


#Register User
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserDetailAPIView(ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]