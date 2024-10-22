# Importar módulos y funciones necesarios
from principal1 import *
from configuracion import *
import random
import math
from extras import *

# Lee el archivo y carga en la lista `lista_producto` todas las palabras
def lectura():
    archivo = open("productos.txt", "r")  # Abre el archivo productos.txt, es un texto sin formato
    productosSinFormato = archivo.readlines()  # Lee el archivo
    listaDeProductos = []

    # Recorre el texto por cadena
    for productoCadena in productosSinFormato:
        # Separa la cadena por cada coma: Ejemplo: 'Laptop,4650,4854\n'
        cadenaProducto = productoCadena.split(',')
        # Arma una lista con los 3 elementos de la cadena original: 'nombre del producto', precioEconomico, precioPremium
        productoFormateado = [cadenaProducto[0], int(cadenaProducto[1]), int(cadenaProducto[2])]
        # Agrega la lista a otra lista con todos los productos
        listaDeProductos.append(productoFormateado)

    archivo.close()  # Cierra el archivo
    return listaDeProductos  # Retorna la lista de listas de productos

# De la lista de productos elige uno al azar y devuelve una lista de 3 elementos:
# Primero el nombre del producto, el segundo si es económico o premium y el tercero el precio.
def buscar_producto(lista_productos):
    indiceDeProductoAleatorio = random.randrange(0, len(lista_productos)-1)  # Arroja un número aleatorio entre 0 y el largo de la lista de productos
    producto = lista_productos[indiceDeProductoAleatorio]  # Guarda el producto en variable. Ejemplo: ['Silla de oficina', 1111, 2222]
    calidadAleatoria = random.randrange(0, 2)  # Arroja un número aleatorio entre 0 y 1, representando 0 para calidad económico, 1 para calidad premium
    if calidadAleatoria == 0:  # Si la calidad es económico, guarda en la variable producto una nueva lista con el nombre del producto,
        # la leyenda correspondiente a la calidad "económico", y el precio correspondiente a esa calidad
        producto = [producto[0], "(económico)", producto[1]]
        return producto
    else:  # De lo contrario, la lista será conformada por la leyenda "premium" y el precio correspondiente
        producto = [producto[0], "(premium)", producto[2]]
        return producto

# Devuelve True si existe el precio recibido como parámetro y aparece al menos 3 veces. Debe considerar el margen.
def esUnPrecioValido(precio, lista_productos, margen):
    contador = 0
    for producto in lista_productos:
        precioComparar = producto[2]
        # Verifica que el producto candidato esté dentro del margen del producto principal
        if (abs(precioComparar - precio) <= margen):  # Toma el valor absoluto de la diferencia entre los precios
            contador += 1
    # Retorna True si el precio existe y aparece al menos 3 veces
    return contador >= 3

# Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    while True:
        productoPpal = buscar_producto(lista_productos)  # Ejemplo: Producto = ["Silla de oficina", "(premium)", 4391]
        productoValido = esUnPrecioValido(productoPpal[2], lista_productos, margen)
        if productoValido:
            return productoPpal  # Ejemplo: Producto = ["Silla de oficina", "(premium)", 4391]

# Compara los precios de dos productos para verificar si están dentro del margen.
# Retorna 1 si los precios son iguales o están dentro del margen, de lo contrario, retorna 0.
def procesar(producto_principal, producto_candidato, margen):
    precioPpal = producto_principal[2]
    precioCandidato = producto_candidato[2]

    if (abs(precioCandidato - precioPpal) <= margen):
        return precioPpal
    return 0


# Verifica si un producto está en una lista, sin repetidos
def estaEnLista(producto, lista):
    return any(p[0] == producto[0] for p in lista)

# Elige productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
# De manera aleatoria se deberá tomar el valor económico o el valor premium. Agregar al nombre '(económico)' o '(premium)'
# para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = []
    productos_seleccionados.append(producto)

    while len(productos_seleccionados) < 5:
        productoValido = dameProducto(lista_productos, margen)
        # Verificar que el producto no esté en la lista antes de agregarlo
        if not estaEnLista(productoValido, productos_seleccionados):
            productos_seleccionados.append(productoValido)

    return productos_seleccionados
