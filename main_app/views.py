from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Car, Wash, Accessory
from .serializers import CarSerializer, WashSerializer, AccessorySerializer

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

  # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    accessories_not_associated = Accessory.objects.exclude(id__in=instance.accessories.all())
    accessories_serializer = AccessorySerializer(accessories_not_associated, many=True)

    return Response({
        'car': serializer.data,
        'accessories_not_associated': accessories_serializer.data
    })
  

class WashListCreate(generics.ListCreateAPIView):
    serializer_class = WashSerializer

    def get_queryset(self):
        car_id = self.kwargs.get('car_id')
        return Wash.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car_id = self.kwargs.get('car_id')
        car = Car.objects.get(id=car_id)
        serializer.save(car=car)
            

class WashDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WashSerializer
    lookup_field = 'id'

    def get_queryset(self):
        car_id = self.kwargs.get('car_id')
        return Wash.objects.filter(car_id=car_id)


class AccessoryList(generics.ListCreateAPIView):
    queryset = Accessory.objects.all()  
    serializer_class = AccessorySerializer

class AccessoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()  
    serializer_class = AccessorySerializer  
    lookup_field = 'id'

class AddAccessoryToCar(APIView):
    def post(self, request, car_id, accessory_id):
        car = Car.objects.get(id=car_id)
        accessory = Accessory.objects.get(id=accessory_id)
        car.accessories.add(accessory)
        return Response({'message': f'Accessory "{accessory.name}" added to Car "{car.make} {car.model}".'})


class RemoveAccessoryFromCar(APIView):
    def post(self, request, car_id, accessory_id):
        car = Car.objects.get(id=car_id)
        accessory = Accessory.objects.get(id=accessory_id)
        car.accessories.remove(accessory)
        return Response({'message': f'Accessory "{accessory.name}" removed from Car "{car.make} {car.model}".'})