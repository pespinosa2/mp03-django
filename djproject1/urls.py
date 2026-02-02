from django.contrib import admin
from django.urls import path, include  # <- añade include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),  # <- añade esta línea
]
