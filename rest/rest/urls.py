from api.libro.libroAPI import LibroAPI
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/libro/select",LibroAPI.as_view(), name='LibroAPI'),#GET
    path("api/v1/libro/create",LibroAPI.as_view(), name='LibroAPI'),#POST
    path("api/v1/libro/update/<int:ID>",LibroAPI.as_view(), name='LibroAPI'),#PUT
    path("api/v1/libro/delete/<int:ID>",LibroAPI.as_view(), name='LibroAPI'),#DEL
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
