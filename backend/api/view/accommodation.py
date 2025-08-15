from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
import requests

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

