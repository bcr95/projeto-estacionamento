from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rotativo/', include('rotativo.urls')),
    path('auth/', include('usuario.urls')),
    path('', home, name='home'),
]
