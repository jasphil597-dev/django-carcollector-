from rest_framework import serializers
from .models import Car, Wash, Accessories

class CarSerializer(serializers.ModelSerializer):
    washed_for_today = serializers.SerializerMethodField()
    
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
        
class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'