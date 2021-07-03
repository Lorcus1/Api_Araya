from api.models import Libro
from rest_framework import fields, serializers


from rest_framework import serializers

class libroSerial (serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    nombre = serializers.CharField(required=False)
    autor = serializers.CharField(required=False)
    Sinopsis = serializers.CharField(required=False)
    Precio   = serializers.IntegerField(required=False)
    Stock    = serializers.IntegerField(required=False)
    Publicación = serializers.DateField(required=False)
    class Meta:
        model = Libro
        fields = '__all__'