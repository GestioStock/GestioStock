from django.db import models
# Create your models here.
  
class ProductosdePila(models.Model):
    idPila = models.CharField(primary_key=True, max_length=50)
    ControlPila = models.IntegerField()
    PesoPila = models.IntegerField()

class ProductosdeFecha(models.Model):
    idProducFecha = models.CharField(primary_key=True, max_length=50)
    fechaElavoracionP = models.DateField()
    fechaVencimientoP = models.DateField()

class Producto(models.Model):
    idProduc = models.AutoField(primary_key=True)
    nombreProduc = models.CharField(max_length=25)
    cantidadProducto = models.IntegerField()
    activo = models.BooleanField(default=True)
    Detalle = models.TextField(max_length=500, blank=True, null=True)
    product_fecha = models.ForeignKey(ProductosdeFecha, on_delete=models.CASCADE, null=True, blank=True)
    product_pila = models.ForeignKey(ProductosdePila, on_delete=models.CASCADE, null=True, blank=True)

    cate = models.CharField(max_length=50)

    subcate = models.CharField(max_length=50)

    product_pila = models.CharField( max_length=50, blank=True)
    product_fecha = models.CharField( max_length=50, blank=True)


class EntradaProducto(models.Model):
    idEntrada = models.AutoField(primary_key= True)
    # rutPersona = models.CharField(max_length=10)
    fechaEntrada = models.DateField()

  
class controlGestor(models.Model):
    idControl = models.IntegerField(primary_key= True)
    fechaVencimiento = models.DateField()
    fechaEntrada = models.DateField()
  
class SubCategoria(models.Model):
    idSubCate = models.AutoField(primary_key=True, unique=True)    
    nombreSubCate = models.CharField(max_length=25)

class Categoria(models.Model):
    idCate = models.AutoField(primary_key=True)
    nombreCate = models.CharField(max_length=25)

class Sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key= True)
    nombreSucursal = models.CharField(max_length=25)
    Direccion = models.CharField(max_length=25)
    tipoProducto = models.CharField(max_length=25)
  
class SalidaProducto(models.Model):
    idSalidaProduct = models.AutoField(primary_key= True, )
    # rutPersona = models.CharField(max_length=10)
    fechaSalida = models.DateField()

  

class Empresa(models.Model):
    idEmpresa = models.IntegerField(primary_key= True, )
    nombreEmpresa = models.CharField(max_length=25)
    CantidadSucursal = models.IntegerField()

class Region(models.Model):
    idRegion = models.IntegerField(primary_key= True)
    nombreRegion = models.CharField(max_length=25)

class Ciudad(models.Model):
    idCiudad = models. IntegerField(primary_key= True)
    nombreCiudad = models.CharField(max_length=25)

class Comuna(models.Model):
    idComuna = models. IntegerField(primary_key= True)
    nombreComuna = models.CharField(max_length=25)
 