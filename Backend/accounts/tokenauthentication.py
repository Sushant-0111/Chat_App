import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

from accounts.models import User

class JWTAuthentication(BaseAuthentication):


    
    def authenticate(self, request):
        token = self.extract_token(request=request)
        if token is None:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            self.verify_token(payload=payload)
            
            user_id = payload['id']
            user = User.objects.get(id=user_id)
            return user
        
        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed("Invalid token")    
    
    
    
    def verify_token(self, payload):
        if "exp" not in payload:
            raise InvalidTokenError("Token is missing expiration time")
        
        exp_timestamp = payload['exp']
        current_timestamp = datetime.now().timestamp()
        
        if current_timestamp > exp_timestamp:
            raise ExpiredSignatureError("Token has expired")
        
    
    
    def extract_token(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            return token
        return None    

    
    
# # payload is all the data that we want to encrypt with the token
# # expiration is the time when the token will expire
    @staticmethod # this is a static method because we are not using self or cls in the method 
    def generate_token(payload):
        expiration = datetime.now() + timedelta(hours=24)
        payload['exp'] = expiration
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
        return token
    
