from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate

# serializer for User management and Handling 
class UserSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only = True)
    
    #  method to create user
    def create(self , validate_data):
        user = get_user_model().objects.create_superuser(
            email= validate_data['email'],
            password=validate_data['password'],
            first_name= validate_data.get('first_name',""),
            last_name = validate_data.get('last_name',"")
        )
        return user
    class Meta:
         model = get_user_model()
         fields = ['email','password','first_name','last_name']
         extra_kwargs = {'password':{'write_only': True}}
        
        
        
# Serializer for Login user and Validate the user 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length = 15,ready_only = True)
    password = serializers.CharField(max_length=255, write_only = True)
    
    
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password",None)
        
        if email is None:
            raise serializers.ValidationError("Email address is required for login") 
        if password is None:
            raise serializers.ValidationError("Password is required for login")
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password")
        
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        
        
        return {
            "email": user.email,
            "id": user.id
            
        }
