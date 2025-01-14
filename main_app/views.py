from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Car, Wash, Accessories
from .serializers import CarSerializer, WashSerializer, AccessoriesSerializer

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

class WashListCreate(generics.ListCreateAPIView):
    serializer_class = WashSerializer

    def get_queryset(self):
        car_id = self.kwargs.get('car_id')
        return Wash.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car_id = self.kwargs.get('car_id')
        try:
            car = Car.objects.get(id=car_id)
            serializer.save(car=car)
        except Car.DoesNotExist:
            raise ValueError("Car with the given ID does not exist.")

class WashDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WashSerializer
    lookup_field = 'id'

    def get_queryset(self):
        car_id = self.kwargs.get('car_id')
        return Wash.objects.filter(car_id=car_id)


class AccessoriesList(generics.ListCreateAPIView):
    queryset = Accessories.objects.all()  
    serializer_class = AccessoriesSerializer

class AccessoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessories.objects.all()  
    serializer_class = AccessoriesSerializer  
    lookup_field = 'id'
