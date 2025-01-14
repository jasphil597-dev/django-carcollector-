from django.urls import path
from .views import Home, CarList, CarDetail, WashListCreate, WashDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cars/', CarList.as_view(), name='car-list'),
    path('cars/<int:id>/', CarDetail.as_view(), name='car-detail'),
    path('cars/<int:car_id>/washes/', WashListCreate.as_view(), name='wash-list-create'),
    path('cars/<int:car_id>/washes/<int:id>/', WashDetail.as_view(), name='wash-detail'),
]
