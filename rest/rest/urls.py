from api.libro.libroAPI import LibroAPI
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/libro/select",LibroAPI.as_view(), name='LibroAPI'),#GET
    path("api/v1/libro/create",LibroAPI.as_view(), name='LibroAPI'),#POST
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
