from .views import main_view
# from api.views import main_view
from django.urls import path,include

urlpatterns = [
    path('', main_view),  # Include the API URLs
]