from django.shortcuts import render

# Create your views here.
from distutils.sysconfig import customize_compiler
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.views.generic import ListView, DetailView
import calendar
from calendar import HTMLCalendar
from datetime import datetime




# Create your views here.

def home(request):
    return render(request, 'eco/first_page.html')
    

def search_order(request):
    if request.method == "POST":
        searched = request.POST['searched']   
        alls = [i.customer.name for i in Order.objects.all()]
        if searched in alls:
            searched4 = True
        else:

            searched4 = False
        orders = Order.objects.filter(customer__name__contains=searched)   
        return render(request, 'eco/first_page2.html', {'searched4':searched4, 'orders':orders})


def list_order(request, order_id):
    ordering = Order.objects.get(pk=order_id)
    return render(request, 'eco/second_page.html', {'ordering':ordering})





def a_calendar(request, user, year, month):
    name = user
    month = month.title()
    #convert month from string to integer
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_num)

    now_year = datetime.now().year
    now_time = datetime.now().time

    return render(request, 'eco/calendar.html', 
            {'name':name, 'year':year, 'month':month, 'cal':cal, 'now_y':now_year, 'now_t':now_time,})