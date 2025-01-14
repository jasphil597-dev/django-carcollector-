from django.contrib import admin
# import your models here
from .models import Car, Wash, Accessories

# Register your models here
admin.site.register(Car)
admin.site.register(Wash)
admin.site.register(Accessories)
