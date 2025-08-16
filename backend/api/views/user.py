from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token  # module-level import
from rest_framework import status
from django.conf import settings
import requests
from rest_framework.authtoken.models import Token  

from api.serializers import (
    AccommodationSerializer,
    ActivitySerializer,
    ItinerarySerializer,
    JournalEntrySerializer,
    PlaceSerializer,
    RestaurantSerializer,
    TravelExpenseSerializer,
    OutfitSerializer,
    TripSerializer,
    UserSerializer,
    PackingListSerializer
)
from api.models import (
    Accommodation,
    Activity,
    Itinerary,
    JournalEntry,
    Place,
    Restaurant,
    TravelExpense,
    Outfit,
    Trip,
    User,
    PackingList
)
# đăng kí user mới và trả về token xác thực
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get(user_id=serializer.data.get('id'))
            return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# quản lí xác thực và lấy thông tin user đăng nhập đăng kí 
class GetAuthUserView(APIView):
    # cơ chế xác thực user
    authentication_classes = (TokenAuthentication,)
    # nếu thành công thì trả về thông tin user không trả về đối tượng AnonymousUser

    # nhận thông tin cá nhân đã xác thực 
    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response(data={'error':'No Token. Authorization Denied'}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=request.user.id)
        #request.user là đối tượng User đã được xác thực
        data = UserSerializer(user).data
        return Response(data)

    # đăng nhập   
    def post(self, request):
        #request.data giống dạng dict để truy cập phần thân của htpp request 
        email = request.data.get('email')
        password = request.data.get('password')

        if email == "" or password == "":
            return Response({'error': 'Please provide both email and password'},status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        #get_or_create trả về một tuple gồm đối tượng và một boolean cho biết đối tượng đã được tạo hay chưa
        #nếu không có token thì sẽ tạo mới một token cho user
        return Response({'token': token.key}, status=status.HTTP_200_OK)