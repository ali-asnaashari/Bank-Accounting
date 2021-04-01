from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('signup',include('signup.urls')),
    path('',include('login.urls')),
    path('system/',include('system.urls')),
    path('admin/', admin.site.urls),
    
]
