from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    date=datetime.datetime.now()
    name='Rahim'
    city='Aligarh'
    college='AMU Aligarh'
    message='Good'
    h=int(date.strftime('%H'))
    if h<12:
        message +='Morning'
    elif h<16:
        message +='Afternoon'
    elif h<21:
        message +='Evening'
    else:
        message +='Night'
    my_dict={'date':date, 'name':name, 'city':city, 'college':college , 'message':message}
    return render(request, 'firstApp/home.html', context=my_dict)


