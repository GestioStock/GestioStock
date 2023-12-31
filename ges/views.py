from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import JsonResponse
from django.db.models import *
from django.utils import timezone
from django.http import HttpResponse
from .models import *
from django.http import HttpResponse, JsonResponse


from rest_framework import generics,status
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# funciones de agregacion----------------------------------
from .serializers import ProductoSerializer, ProductosdeFechaSerializer, EntradaProductoSerializer, ProductosdePilaSerializer,CategoriaSerializer, SubCategoriaSerializer
from django.http import JsonResponse
from django.views import View

# -----------------
from .formUser import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# funciones para el gráfico
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class ProductoListCreateView(APIView):
    def post(self, request, format=None):

        serializer = ProductoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductosdeFechaCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProductosdeFechaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntradaProductoCreateView(APIView):
    def post(self, request, format=None):
        serializer = EntradaProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductosdePilaCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProductosdePilaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def addProduct(request):
    if request.method == 'POST':

        response = redirect('addProduct')  # Puedes cambiar la redirección según tus necesidades
        return response
    else:
        return render(request, 'templatesGes/addProduct.html')



class AddCate(APIView):
    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class AddSubCate(APIView):
    def post(self, request, format=None):
        serializer = SubCategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#  funciones de eliminacion----------------------------------


def eliminar_producto(request):
    return render(request, 'templatesGes/delProduct.html')


class CategoriaDeleteView(APIView):
    def delete(self, request, idCate, format=None): 
        try:
            categoria = Categoria.objects.get(idCate=idCate)  
            categoria.delete()
            return Response({'message': 'Categoría eliminada exitosamente'}, status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response({'error': 'La categoría no existe'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubcategoriaDeleteView(APIView):
    def delete(self, request, idSubCate, format=None):  
        try:
            subcategoria = SubCategoria.objects.get(idSubCate=idSubCate) 
            subcategoria.delete()
            return Response({'message': 'Sub-Categoría eliminada exitosamente'}, status=status.HTTP_204_NO_CONTENT)
        except SubCategoria.DoesNotExist:
            return Response({'error': 'La sub-categoría no existe'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def gestor(request):
    return render(request,'templatesGes/gestor.html' )





def cate(request):

    data = {' '}
    return render(request, 'templatesGes/categorias.html')

class CategoriaListAPI(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        data = [{'id': categoria.idCate, 'nombre': categoria.nombreCate} for categoria in categorias]
        
        return JsonResponse(data, safe=False)


class SubCategoriaListAPI(View):
    def get(self, request):
        subcategorias = SubCategoria.objects.all()
        data = [{'id': subcategoria.idSubCate, 'nombre': subcategoria.nombreSubCate} for subcategoria in subcategorias]
        
        return JsonResponse(data, safe=False)

def buscarP(request):
    
    return render(request, 'templatesop/buscar.html')


class CambiarActivoAPIView(APIView):
    def post(self, request, format=None):
        producto_id = request.data.get('idProduc')

        try:
            producto = Producto.objects.get(idProduc=producto_id)

            # Decrementar la cantidad en uno
            producto.cantidadProducto -= 1
            producto.save()

            # Cambiar el estado activo a False si la cantidad es 0
            if producto.cantidadProducto == 0:
                producto.activo = False
                producto.save()

            return Response({'activo': producto.activo, 'cantidad': producto.cantidadProducto}, status=status.HTTP_200_OK)

        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
# Codigo para el template de buscar
class TablaCombinadaAPIView(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.filter(activo=True)
        productos_serializer = ProductoSerializer(productos, many=True)
        
        entradas_producto = EntradaProducto.objects.all()
        entradas_producto_serializer = EntradaProductoSerializer(entradas_producto, many=True)
        
        productos_fecha = ProductosdeFecha.objects.all()
        productos_fecha_serializer = ProductosdeFechaSerializer(productos_fecha, many=True)

        combined_data_pila = []
        combined_data_fecha = []
        combined_data = []

        for producto in productos_serializer.data:
            entrada_producto_relacionada = next((ep for ep in entradas_producto_serializer.data if ep['idEntrada'] == producto['idProduc']), None)

            combined_item_pila = {
                'id': producto['idProduc'],
                'nombre': producto['nombreProduc'],
                'nombreProducto': producto['nombreProduc'],
                'cantidad': producto['cantidadProducto'],
                'cate': producto['cate'],
                'subcate': producto['subcate'],
                'detalle': producto['Detalle'],
                'activo': producto['activo'],
                'fechaEntrada': entrada_producto_relacionada['fechaEntrada'] if entrada_producto_relacionada else None,
            }

            if producto['product_pila']:
                try:
                    pila = ProductosdePila.objects.get(idPila=int(producto['product_pila']))
                    combined_item_pila.update({
                        'peso': pila.PesoPila,
                        'controlPila': pila.ControlPila,
                        'fechaEntrada': entrada_producto_relacionada['fechaEntrada'] if entrada_producto_relacionada else None,
                    })
                    combined_data_pila.append(combined_item_pila)
                    combined_data.append(combined_item_pila)
                except ProductosdePila.DoesNotExist:
                    pass

            combined_item_fecha = {
                'id': producto['idProduc'],
                'nombre': producto['nombreProduc'],
                'nombreProducto': producto['nombreProduc'],
                'cantidad': producto['cantidadProducto'],
                'cate': producto['cate'],
                'subcate': producto['subcate'],
                'detalle': producto['Detalle'],
                'activo': producto['activo'],
                'fechaEntrada': entrada_producto_relacionada['fechaEntrada'] if entrada_producto_relacionada else None,
            }

            if producto['product_fecha']:
                try:
                    producto_fecha_relacionado = next(
                        (pf for pf in productos_fecha_serializer.data if pf['idProducFecha'] == producto['product_fecha']), None)

                    fecha = ProductosdeFecha.objects.get(idProducFecha=int(producto['product_fecha']))
                    combined_item_fecha.update({
                        'fechaElavoracionP': fecha.fechaElavoracionP,
                        'fechaVencimientoP': fecha.fechaVencimientoP,
                    })
                    combined_data_fecha.append(combined_item_fecha)
                    combined_data.append(combined_item_fecha)
                except ProductosdeFecha.DoesNotExist:
                    pass

        data = {'data_pila': combined_data_pila, 'data_fecha': combined_data_fecha, 'dataB' : combined_data}
        return JsonResponse(data, safe=False)

# registrar usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to = "gestor")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

# views del resumen

def resumen(request):
    productos = Producto.objects.all()

    # Crear un gráfico simple
    plt.bar(productos.values_list('nombreProduc', flat=True), productos.values_list('cantidadProducto', flat=True))
    plt.xlabel('Nombre del Producto')
    plt.ylabel('Cantidad')
    plt.title('Resumen de Productos')

    # Guardar la imagen del gráfico en un búfer de bytes
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convertir la imagen a base64 para incrustarla en la plantilla HTML
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Pasa la ruta de la imagen base64 a la plantilla HTML
    return render(request, 'templatesop/resumen.html', {'productos': productos, 'chart_image': image_base64})

# resumen de la javiera
class ProductoListAPI(View):
    def get(self, request):
        productos = Producto.objects.all()
        data = [{'id': producto.idProduc, 'nombre': producto.nombreProduc,
                        'nombreProducto':  producto.nombreProduc,
                        'cantidad':  producto.cantidadProducto,
                        'cate':  producto.cate,
                        'subcate': producto.subcate,
                        'detalle': producto.Detalle,
                        'activo': producto.activo,} for producto in productos]
        
        return JsonResponse(data, safe=False)