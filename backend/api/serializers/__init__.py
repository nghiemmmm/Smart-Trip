#Chuyển đổi dữ liệu giữa Model <-> JSON
#Cần thiết khi làm Django REST API: model chỉ là dữ liệu, nhưng client cần JSO
from .approval import ApprovalSerializer
from .travel_plan import TravelPlanSerializer   
from .travel_plan import TravelPlanSerializer
from .email_log import EmailLogSerializer
