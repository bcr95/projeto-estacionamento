from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rotativo/', include('rotativo.urls')),
    path('cliente/', include('cliente.urls')),
    path('', home, name='home')
]
