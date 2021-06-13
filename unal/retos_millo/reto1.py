import math

def costo_envio(precio_elementos_comprados) -> int:
    if precio_elementos_comprados < 50000:
        return 8000
    elif precio_elementos_comprados >= 50000 and precio_elementos_comprados <= 200000:
        return precio_elementos_comprados * 3 / 100
    else:
        return 0

def costo_bolsas(cantidad_elementos_comprados:int) -> int:
    cantidad_bolsas = math.ceil(cantidad_elementos_comprados / 3)
    precio_bolsa = 100
    return cantidad_bolsas * precio_bolsa

def precio_total(costo_envio, costo_bolsas, precio_elementos_comprados:int, cantidad_elementos_comprados:int) -> int:
    return precio_elementos_comprados + costo_envio(precio_elementos_comprados) + costo_bolsas(cantidad_elementos_comprados)

#Entradas
cantidad_elementos_comprados = int(input())
precio_elementos_comprados = int(input())

#salidas
print(precio_elementos_comprados)   #Precio total de los elementos comprados
#costos de envio
print(costo_envio(precio_elementos_comprados))
#Costo de las bolsas
print(costo_bolsas(cantidad_elementos_comprados))
#Precio total
print(precio_total(costo_envio, costo_bolsas, precio_elementos_comprados, cantidad_elementos_comprados))
#Cantidad bolsas
print(math.ceil(cantidad_elementos_comprados / 3))