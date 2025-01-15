from django.db import models
# add this import
from datetime import date

# A tuple of 2-tuples
WASH_TYPES = (
    ('B', 'Basic Wash'),
    ('D', 'Deluxe Wash'),
    ('P', 'Premiun Wash')
)
# new code above

# Add the Toy model
class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    # Add the M:M relationship
    accessories = models.ManyToManyField(Accessory, related_name="cars")
    
    # new code below
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def wash_for_today(self):
        return self.wash_set.filter(date=date.today()).count() >= len(WASH_TYPES)
    
# Wash model to track car washes
class Wash(models.Model):
    date = models.DateField(default=date.today)  
    wash_type = models.CharField(
        max_length=1,
        choices=WASH_TYPES
    )  
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Relationship with the Car model

    def __str__(self):
        return f"{self.car} - {self.get_wash_type_display()} on {self.date}"
    
    # Change the default sort order
    class Meta:
        ordering = ['-date']