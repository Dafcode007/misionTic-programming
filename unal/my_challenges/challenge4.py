import json
def problem():
    """challenge.4 Adquiriendo información adicional de los competidores de Freydell
       Dioselina, Juanquini y Sutatán a través han decidido apoyarse en la Red Sobrenatural Colombiana para obtener información adicional de los competidores que ellos no han podido obtener (la red les ofrece esta información a un precio que depende de la inicial del competidor). Realizar un programa que reciba un diccionario con la pareja inicial competidor: precio en formato JSON, así como la lista de las iniciales (separadas por un espacio) de los competidores de los cuales los tres adivinadores no tienen información adicional. Como salida del programa se debe entregar el costo total de la información adicional de los competidores que pueden comprar (de los que la red tiene información), junto con las iniciales (separada por un espacio) para las cuales se cuenta con información.

       Example:
       ****************************************************
       input                                      outputs
       ****************************************************
       {"Z": 150000, "O": 120000,                 890000
       "A": 100000, "X": 350000,                  
       "Q": 120000, "J": 200000,                  A J M O
       "M": 470000}
       
       A C F H J M N O
       ****************************************************"""

#Descerialice data -> convert json to dict
def json_to_dict(d:str) -> dict:
    data = json.loads(d)
    return data

def solve(d:dict, c:str) -> list:
    competitors = d
    rta = []
    initials = []
    total_cost = 0
    for letter in c:
        #Validate if each letter of the string("c") is found in the dictionary keys 
        if letter in competitors.keys():
            #Sum of each of the values for each competitor
            total_cost += competitors[letter]
            #Add the initial letter of each competitor in an array("rta")
            initials.append(letter)
    rta.append(total_cost)
    rta.append(" ".join(map(str, initials)))
    return rta
    #print(total_cost)
    #print(" ".join((map(str, rta))))
    
def main():
    #inputs
    data = input(''' ''')
    initials = input()
    #Outputs
    print(solve(json_to_dict(data), initials)[0])
    print(solve(json_to_dict(data), initials)[1])

#Main program
main()