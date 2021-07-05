from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password

class LoginApi(APIView):
    def post(self, request):
        data = request.data

        usuario = data['usuario']
        clave = data['clave']
        try:
            user = User.objects.get(username = usuario)
        except:
            return Response({"Error": "usuario no válido"}, status=400)

        clave_valida = check_password(clave, user.password)
        if(clave_valida):
            token, created = Token.objects.get_or_create(user=user)

            return Response({"Token": token.key},status=200)
        else:
            return Response({"Error": "clave inválida"}, status=400)

class LogoutApi(APIView): 
    def post(self, request):
        try:
            data = request.data
            token = data['token']
            token = Token.objects.filter(key = token )

            token.delete()

            return Response(status=200)
            
        except:
            return Response (status=400)