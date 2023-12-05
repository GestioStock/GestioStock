"""
URL configuration for GestioStock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ges import views
from ges.views import ProductoListCreateView,ProductosdeFechaCreateView,EntradaProductoCreateView, ProductosdePilaCreateView,AddCate,CategoriaDeleteView,CategoriaListAPI,SubCategoriaListAPI, SubcategoriaDeleteView,AddSubCate,TablaCombinadaAPIView,CambiarActivoAPIView

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/addProduct/', ProductoListCreateView.as_view(), name='addProduct'),
    path('api/addProductosFecha/', ProductosdeFechaCreateView.as_view(), name='addProductosFecha'),
    path('api/addProductosPila/', ProductosdePilaCreateView.as_view(), name='addProductosPila'),
    path('api/addEntradaProducto/', EntradaProductoCreateView.as_view(), name='addEntradaProducto'),
    path('addProduct/', views.addProduct, name='addProduct'),


    path('api/AddCate/', AddCate.as_view(), name='AddCate'),
    path('api/categorias/<int:idCate>/', CategoriaDeleteView.as_view(), name='delete_categoria'),  # Cambia 'id' a 'idCate'
    path('api/categorias/', CategoriaListAPI.as_view(), name='categoria-list-api'),
    

    path('api/AddSubCate/', AddSubCate.as_view(), name='AddSubCate'),
    path('api/subcategorias/', SubCategoriaListAPI.as_view(), name='subcategoria-list-api'),
    path('api/subcategorias/<int:idSubCate>/', SubcategoriaDeleteView.as_view(), name='delete_subcategoria'),  # Cambia 'id' a 'idCate'


    path('delProduct/', views.eliminar_producto, name='delProduct'),  # Ruta para ver la tabla de productos a eliminar

    path('gestor/', views.gestor, name='gestor'),

    path('cate/', views.cate, name='cate'),

    path('buscar/', views.buscarP, name='buscarP'),
    path('api/tabla-combinada/', TablaCombinadaAPIView.as_view(), name='tabla_combinada'),
    path('api/cambiar-activo/', CambiarActivoAPIView.as_view(), name='cambiar_activo'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.registro, name='registro'),

    path('resumen/', views.resumen, name='resumen'), 
       
]
