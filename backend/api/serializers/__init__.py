#Chuyển đổi dữ liệu giữa Model <-> JSON
#Cần thiết khi làm Django REST API: model chỉ là dữ liệu, nhưng client cần JSO
from .accommodation import AccommodationSerializer
from .activity import ActivitySerializer
from .itinerary import ItinerarySerializer
from .journal_entry import JournalEntrySerializer
from .place import PlaceSerializer
from .restaurant import RestaurantSerializer    
from .travle_expense import TravelExpenseSerializer
from .outfit import OutfitSerializer
from .trip import TripSerializer
from .user import UserSerializer
from .packing_list import PackingListSerializer
