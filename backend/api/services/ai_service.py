'''import os
import requests
from django.conf import settings

def get_chat_response(message):
    api_key = os.getenv('API_KEY')
    response = requests.post(
        'https://api.x.ai/grok',
        json={'query': message},
        headers={'Authorization': f'Bearer {api_key}'}
    )
    '''