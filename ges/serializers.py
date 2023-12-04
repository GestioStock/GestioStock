# serializers.py
from rest_framework import serializers
from .models import Producto, ProductosdeFecha, ProductosdePila, EntradaProducto, Categoria, SubCategoria

class ProductosdeFechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosdeFecha
        fields = '__all__'

class ProductosdePilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosdePila
        fields = '__all__'

class EntradaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaProducto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'








