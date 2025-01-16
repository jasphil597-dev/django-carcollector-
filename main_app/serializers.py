from rest_framework import serializers
from .models import Car, Wash, Accessory
from django.contrib.auth.models import User # add this line to list of imports

# include User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user
  
class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'
        

class CarSerializer(serializers.ModelSerializer):
  wash_for_today = serializers.SerializerMethodField()
  accessories = AccessorySerializer(many=True, read_only=True)
  # add user field to Car serializer
  user = serializers.PrimaryKeyRelatedField(read_only=True)  # Make the user field read-only
  

# class CarSerializer(serializers.ModelSerializer):
#     washed_for_today = serializers.SerializerMethodField()
#     accessories = AccessorySerializer(many=True, read_only=True) #add this line

#     class Meta:
#         model = Car
#         fields = '__all__'  
        
#     # Add method to calculate if all wash types are completed for today
#     def get_washed_for_today(self, obj):
#         return obj.wash_for_today()
        
class WashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wash
        fields = '__all__'  
        read_only_fields = ('car',) 