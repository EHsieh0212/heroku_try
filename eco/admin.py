from django.contrib import admin
from .models import Order
from .models import Customer



# Register your models here.


admin.site.register(Customer)
admin.site.register(Order)