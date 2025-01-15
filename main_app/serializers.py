from rest_framework import serializers
from .models import Car, Wash, Accessory


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'
        
class CarSerializer(serializers.ModelSerializer):
    washed_for_today = serializers.SerializerMethodField()
    accessories = AccessorySerializer(many=True, read_only=True) #add this line

    class Meta:
        model = Car
        fields = '__all__'  
        
    # Add method to calculate if all wash types are completed for today
    def get_washed_for_today(self, obj):
        return obj.wash_for_today()
        
class WashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wash
        fields = '__all__'  
        read_only_fields = ('car',) 