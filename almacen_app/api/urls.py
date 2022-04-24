from django.urls import path
from almacen_app.api.views import (
    AlmacenesListAV, 
    AlmacenShowAV, 
    ProductosDetailAlmacenAV,
    ProductosListAV,
    ProductoShowAV,
    AlmacenDetailProductoAV)


urlpatterns = [
    path('almacenes', AlmacenesListAV.as_view(), name='almacenes-list'),
    path('almacenes/<int:id>', AlmacenShowAV.as_view(), name='almacenes-detail'),
    path('almacenes/<int:id>/productos', ProductosDetailAlmacenAV.as_view(), name='almacenes-products-detail'),
    
    path('productos', ProductosListAV.as_view(), name='das'),
    path('productos/<int:id>', ProductoShowAV.as_view(), name='fdsdfg'),
    path('productos/<int:id>/almacen', AlmacenDetailProductoAV.as_view(), name='fgfh'),
]