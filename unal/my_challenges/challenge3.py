def problema():
    """Dioselina y Juanquini siguen adivinando las iniciales de los competidores que podrían ganarle los negocios a Freydell. Pedro ha decidido contratar un tercer adivinador: el Profesor Sutatán. Esta vez Pedro quiere que los tres trabajen en equipo para adivinar la inicial del competidor porque considera que así van a ser más acertados.

    Elabore un programa que reciba como entrada la lista de iniciales de los competidores identificado por el equipo de adivinadores separadas por un espacio. La salida debe ser:

    . En la primera línea de consola: Lista de distintas iniciales en orden de aparición       (considerando que una inicial se podría repetir más adelante) separadas por un espacio.

    . En la segunda línea de consola: Lista de número de veces seguidas que apareció la inicial separadas por un espacio.
    
    Ejemplo:
    **********************************
    input             output
    E E E D J J J C J C S S S E
    ***********************************"""

def solve(c:list):
    rta1 = []
    rta2 = []
    array = c.split()
    array.append("*")
    #Initialize index and counter
    contador = 0
    index = 0
    #Iterate over the array until an asterisk is encountered
    while array[index] != "*":
        if array[index] == array[index + 1]:
            contador += 1
            index += 1
        else:
            contador += 1
            rta1.append(array[index])
            rta2.append(contador)
            contador = 0
            index += 1
    print(" ".join(rta1))
    print(" ".join(map(str, rta2)))



def main():
    #Inputs
    chain = input()
    solve(chain)

#Main program
main()
    




