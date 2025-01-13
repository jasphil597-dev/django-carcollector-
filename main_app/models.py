from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
