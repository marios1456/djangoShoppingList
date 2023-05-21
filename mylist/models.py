from django.db import models
from datetime import date
#from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class ShoppingItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user", default=2)

    def __str__(self):
        return "id: " + f"{self.id}" + " name: " + self.name + " created at: " + f"{self.created_at}"



