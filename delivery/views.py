from django.shortcuts import render

# Create your views here.
def Pickup(request):
 return render(request,"Pickup.html")


def Delivery(request):
 return render(request,"Delivery.html")