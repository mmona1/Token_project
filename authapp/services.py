import requests
from .cache import AuthTokenCache

class APIService:
    def __init__(self, auth_service_url):
        self.auth_service_url = auth_service_url
        self.auth_cache = AuthTokenCache(max_size=10)

    def authenticate_user(self, user_id):
        # Check the local cache first
        token = self.auth_cache.get_token(user_id)
        if token:
            print("Token fetched from cache.")
            return token

        response = requests.post(f"{self.auth_service_url}/auth", json={"user_id": user_id})
        if response.status_code == 200:
            token = response.json().get("token")
            self.auth_cache.set_token(user_id, token)
            return token
        else:
            raise Exception("Authentication failed!")
