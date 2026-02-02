from django.contrib import admin
from django.urls import path, include  # <- include es obligatorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),  # <- esta línea debe estar
]
