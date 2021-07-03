from api.libro.libroSLR import libroSerial
from api.models import Libro
from rest_framework.response import Response
from rest_framework.views import APIView

class LibroAPI(APIView):
    def get(self,request):
        libros = Libro.objects.all()
        serializador = libroSerial(libros,many=True)
        return Response(serializador.data,status=200)

    def post(self, request):
        return Response(status=200)

    def put (self, request, ID):
        return Response (status=200)
    
    def delete (self, request, ID):
        return Response (status=200)