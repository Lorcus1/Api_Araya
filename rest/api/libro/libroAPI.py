from rest_framework import serializers
from api.libro.libroSLR import libroSerial
from api.models import Libro
from rest_framework.response import Response
from rest_framework.views import APIView

class LibroAPI(APIView):
    def get(self,request):
        try:
            libros = Libro.objects.all()
            serializador = libroSerial(libros,many=True)
            return Response(serializador.data,status=200)
        except:
            return Response(status=400)
    def post(self, request):
        serializador = libroSerial(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=200)
        else:
            return Response(serializador.errors , status=400)

    def put (self, request, ID):
        libros = Libro.objects.get(ID=ID)
        serializador = libroSerial(libros, data=request.data)

        if serializador.is_valid():
            serializador.save()
            return Response (status=200)
        else:
            return Response (serializador.errors, status=400)
        
    
    def delete (self, request, ID):
        libros = Libro.objects.get(ID=ID)
        libros.delete()
        return Response(status=200)