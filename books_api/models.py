from django.db import models

# Create your models here.
class Auther(models.Model):
    author_id = models.IntegerField()
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    info = models.TextField()
    nic_name = models.CharField(max_length=56)
    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

class Genre(models.Model):
    pass

class Books(models.Model):
    order_id = models.IntegerField()
    title = models.CharField(max_length=64)
    page = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()

class Publisher(models.Model):
    pass