from django.db import models
from datetime import date

# Create your models here.


class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return "id: " + f"{self.id}" + " name: " + self.name + " created at: " + f"{self.created_at}"



