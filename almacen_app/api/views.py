from rest_framework.views import APIView
from almacen_app.models import Almacen, Producto
from almacen_app.api.serializers import AlmacenSerializer, ProductoSerializer
from rest_framework.response import Response
from rest_framework import status, generics


# class AlmacenesListAV(generics.ListCreateAPIView):
#     serializer_class = AlmacenSerializer
    
#     def get_queryset(self):
#         return Almacen.objects.all()

class AlmacenesListAV(APIView):
    def get(self, request):
        almacenes = Almacen.objects.all()
        serializer = AlmacenSerializer(almacenes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error' : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
class AlmacenShowAV(APIView):
    def get(self, request, id):
        try:
            almacen = Almacen.objects.get(pk=id)
            
            serializer = AlmacenSerializer(almacen)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        try:
            almacen = Almacen.objects.get(pk = id)
            serializer = AlmacenSerializer(almacen, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error' : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
                
        except Almacen.DoesNotExist:
            return Response({'error':'Objeto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        try:
            almacen = Almacen.objects.get(pk = id)    
        
            almacen.delete()
            return Response({'status': 'Objeto eliminado'}, status=status.HTTP_204_NO_CONTENT)
                
        except Almacen.DoesNotExist:
            return Response({'error':'Objeto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
            
class ProductosDetailAlmacenAV(APIView):
    def get(self, request, id):
        try:
            almacen = Almacen.objects.get(pk=id)
            productos = Producto.objects.filter(almacen=almacen.pk)
            serializer = ProductoSerializer(productos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Almacen.DoesNotExist:
            return Response({'error': 'Almacen no encontrado'}, status=status.HTTP_404_NOT_FOUND)
   
class ProductosListAV(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error' : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
###################################
    
class ProductoShowAV(APIView):
    def get(self, request, id):
        try:
            producto = Producto.objects.get(pk=id)
            
            serializer = ProductoSerializer(producto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        try:
            producto = Producto.objects.get(pk = id)
            serializer = ProductoSerializer(producto, data=request.data)
            if serializer.is_valid():
                #producto.almacen = int(request.data['almacen'])
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error' : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
                
        except Producto.DoesNotExist:
            return Response({'error':'Producto no encontrado put'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        try:
            producto = Producto.objects.get(pk = id)    
        
            Producto.delete()
            return Response({'status': 'Producto eliminado'}, status=status.HTTP_204_NO_CONTENT)
                
        except Producto.DoesNotExist:
            return Response({'error':'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    
class AlmacenDetailProductoAV(APIView):
    def get(self, request):
        almacenes = Almacen.objects.all()
        serializer = AlmacenSerializer(almacenes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)