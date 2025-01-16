from rest_framework import serializers
from django.contrib.auth.models import get_user_model

class UserSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)

   def create(selfm,validated_data):
       user = get_user_model().objects.create_user(
           email = validated_data['email'],
           password = validated_data['password'],
            first_name = validated_data.get('first_name'," "),   
            last_name = validated_data.get("last_name"," "), 
       )
       return super().create(validated_data)




class Meta:
           model = get_user_model()
           fields = ['id','email','password','first_name','last_name']
           extra_kwargs = {
               'password' : {'write_only':True}
           }