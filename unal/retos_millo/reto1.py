import math

def costo_envio(precio_elementos_comprados) -> int:
    if precio_elementos_comprados < 50000:
        return 8000
    elif precio_elementos_comprados >= 50000 and precio_elementos_comprados <= 200000:
        return int(precio_elementos_comprados * 3 / 100)
    else:
        return 0

def costo_bolsas(cantidad_elementos_comprados:int) -> int:
    cantidad_bolsas = math.ceil(cantidad_elementos_comprados / 3)
    precio_bolsa = 100
    return cantidad_bolsas * precio_bolsa

def precio_total(costo_envio, costo_bolsas, precio_elementos_comprados:int, cantidad_elementos_comprados:int) -> int:
    return precio_elementos_comprados + costo_envio(precio_elementos_comprados) + costo_bolsas(cantidad_elementos_comprados)

def numeros_letras(cantidad_elementos_comprados):
    unidades = ["cero", "una", "dos" ,"tres" ,"cuatro" ,"cinco" ,
                "seis" ,"siete" ,"ocho" ,"nueve","diez"]
    especiales = ["once", "doce","trece","catorce", "quince",
                "diezciseis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["veinte", "treinta","cuarenta","cincuenta", "sesenta",
                "setenta", "ochenta", "noventa"]

    #El dato ingresado lo convierte a entero y lo almacena en la variable num
    num = math.ceil(cantidad_elementos_comprados / 3)

    if (num >=0 and num <11):
        print(unidades[num])

    elif (num < 20):
        print(especiales[num-11])

    elif (num <100):
        
        unid = num% 10;
        #math.floor -> obtiene la parte entera de la division num/10
        #luego ese resultado lo convertimos a entero, 
        dec = int(math.floor(num/10))
        if (unid == 0):
            print(decenas[dec-2]) 
        else:
            print(decenas[dec-2], "y" , unidades[unid])
    else:
        print("El numero debe ser menor a 100")



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
numeros_letras(cantidad_elementos_comprados)
