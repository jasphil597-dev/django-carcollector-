from django.urls import path
from .views import Home, CarList, CarDetail, WashListCreate, WashDetail, AccessoryList, AccessoryDetail, AddAccessoryToCar, RemoveAccessoryFromCar, CreateUserView, LoginView, VerifyUserView # additional imports

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # new routes below
    path('cars/', CarList.as_view(), name='car-list'),
    path('cars/<int:id>/', CarDetail.as_view(), name='car-detail'),
    path('cars/<int:car_id>/washes/', WashListCreate.as_view(), name='wash-list-create'),
    path('cars/<int:car_id>/washes/<int:id>/', WashDetail.as_view(), name='wash-detail'),
    path('cars/<int:car_id>/accessory/', AccessoryList.as_view(), name='accessory-list'),  
    path('cars/<int:car_id>/accessory/<int:id>/', AccessoryDetail.as_view(), name='accessory-detail'),
    path('cars/<int:car_id>/add_accessory/<int:accessory_id>/', AddAccessoryToCar.as_view(), name='add-accessory-to-car'),
    path('cars/<int:car_id>/remove_accessory/<int:accessory_id>/', RemoveAccessoryFromCar.as_view(), name='remove-accessory-from-car'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
  


]
