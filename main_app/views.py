from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Car, Wash
from .serializers import CarSerializer, WashSerializer

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the car-collector API home route!'}
        return Response(content)

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()  
    serializer_class = CarSerializer  

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()  
    serializer_class = CarSerializer  
    lookup_field = 'id'  

# main_app/views.py
class WashListCreate(generics.ListCreateAPIView):
    serializer_class = WashSerializer
    
    def get_queryset(self):
        car_id = self.kwargs['car_id']
        return Wash.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car_id = self.kwargs['car_id']
        car = Car.objects.get(id=car_id)
        serializer.save(car=car)
        
class WashDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WashSerializer
    lookup_field = 'id'

    def get_queryset(self):
        car_id = self.kwargs['car_id']
        return Wash.objects.filter(car_id=car_id)