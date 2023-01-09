from django.db import models


# Create your models here.
class Staff(models.Model):
    staff_number = models.PositiveIntegerField()
    day_of_employment = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    position = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return f'Student:{self.first_name}{self.last_name}'
