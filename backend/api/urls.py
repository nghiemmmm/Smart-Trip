
# from api.views import main_view
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', main_view),  # Include the API URLs
    path('users/', UserView.as_view()),
    path('auth/', GetAuthUserView.as_view()),
]