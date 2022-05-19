from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Order(models.Model):
    order = models.TextField(max_length=100)    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.customer.name

