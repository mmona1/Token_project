from collections import deque

class AuthTokenCache:
    def __init__(self, max_size=10):
        self.cache = deque(maxlen=max_size)

    def getToken(self):
        if self.cache:
            return self.cache[-1]  # Return the most recent token
        return None

    def setToken(self, token):
        self.cache.append(token)  # Append the token to the cache
