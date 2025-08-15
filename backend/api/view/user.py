# from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import authenticate
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token  # module-level import
# from rest_framework import status
# from django.conf import settings
# import requests

# from api.serializers import (
#     AccommodationSerializer,
#     ActivitySerializer,
#     ItinerarySerializer,
#     JournalEntrySerializer,
#     PlaceSerializer,
#     RestaurantSerializer,
#     TravelExpenseSerializer,
#     OutfitSerializer,
#     TripSerializer,
#     UserSerializer,
#     PackingListSerializer
# )
# from api.models import (
#     Accommodation,
#     Activity,
#     Itinerary,
#     JournalEntry,
#     Place,
#     Restaurant,
#     TravelExpense,
#     Outfit,
#     Trip,
#     User,
#     PackingList
# )

# class UserView(APIView):
#     def post(self, request):
#         from rest_framework.authtoken.models import Token  # import bên trong function
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             token = Token.objects.get(user_id=serializer.data.get('id'))
#             return Response(data={'token': token.key}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)