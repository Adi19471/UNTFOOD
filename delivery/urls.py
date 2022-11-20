
from django.urls import path
from django.views import View
from delivery import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pickup/', views.Pickup,name="Pickup"),
    path('Delivery/', views.Delivery,name="Delivery"),
 
] 




