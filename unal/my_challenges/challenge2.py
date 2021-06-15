'''Challenge.2 adivinando competidores
Luego del poco éxito de Barbarita para obtener los nombres de competidores que le podrían ganar un negocio a Freydell a través de ingeniería social, Pedro ha decidido contratar a la Bruja Dioselina y al Mago Juanquini, quienes prometen darle esta información, pero con un costo muy alto. Pedro logró negociar a un precio que considera justo para que Dioselina y Juanquini le den al menos la inicial de los competidores que le podrían ganar un nuevo negocio.

Dioselina y Juanquini entregaron las iniciales de competidores que lograron identificar. Ante la pérdida de un nuevo negocio, Pedro revisó si empezaba las letras iniciales que Dioselina o Juanquini habían entregado. Si Dioselina identificó más iniciales correctas de competidores se especifica una ‘D’ y si Juanquini es quien identificó más se escribe 'J', pero si ambos identificaron el mismo número entonces se especifica una 'L'.

Realice un programa que reciba las iniciales adivinadas por Dioselina y las iniciales adivinadas por Juanquini (como cadena de caracteres) y una cadena de caracteres con las primeras letras de los competidores identificados por Pedro e imprima en consola lo que él escribió después de la revisión y verificación con la Bruja Dioselina y el Mago Juanquini.

Ejemplo:
**************************************
Entrada         Salida
**************************************
SDA             LLLLDDDDDDDDDDDDDDDDDDDD

AHS

AJSSDSAASASASSASADAJAJSS
**************************************'''


#This function evaluates whether a given letter is found in a given word
def letters_in_word(l:str, w:str) -> bool:
    for i in w:
        if i == l:
            return True
    return False

#solve
def solve(d:str, j:str, p:str) -> str:
    rta = []
    #we initialize two counters to zero
    count_dioselina = 0
    count_juanquini = 0
    for i in p:
        #The existence of the letter in both strings is validated and the counter is incremented by one if the letter is in the word.
        if letters_in_word(i, d) == True and letters_in_word(i, j) == False:
            count_dioselina += 1
        elif letters_in_word(i, d) == False and letters_in_word(i, j) == True:
            count_juanquini += 1
        
        #The two counters are compared and the respective letter is stored in an array
        if count_dioselina > count_juanquini:
            rta.append("D")
        elif count_juanquini > count_dioselina:
            rta.append("J")
        else:
            rta.append("L")
    #We return the elements of the array converted into a string
    return "".join(rta)
        
#main function
#inputs
dioselina_chain = input()
juanquini_chain = input()
pedro_chain = input()

#outputs
print(solve(dioselina_chain, juanquini_chain, pedro_chain))
