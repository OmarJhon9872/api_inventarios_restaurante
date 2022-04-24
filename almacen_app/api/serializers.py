from pyexpat import model
from django.http import JsonResponse
from rest_framework import serializers

from almacen_app.models import Almacen, Producto

class ProductoSerializer(serializers.ModelSerializer):
    almacen = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Producto
        
    def validate_almacen(self, data):
        almacen = data['almacen']
        if 1:
            raise serializers.ValidationError("Almacen must be a number")

class AlmacenSerializer(serializers.ModelSerializer):
    productos = serializers.SerializerMethodField()
    
    class Meta:
        fields = '__all__'
        model = Almacen
    
    def get_productos(self, object):
        productos = Producto.objects.filter(almacen=object.pk)
        serializer = ProductoSerializer(productos, many=True)
        return serializer.data