from django.db import models

# Create your models here.
class Registrations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    message = models.TextField()
    
    def __str__(self):
        return self.name