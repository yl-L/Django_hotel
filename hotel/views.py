from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from hotel.models import Hotel
def index(request):
      hotels=Hotel.objects.all().order_by('-score')
      return render(request,'index.html',{'hotels':hotels,})

def hotel_id(request,id):
      detail = Hotel.objects.get(id=id)
      return render(request,'hotel.html',{'detail':detail,})