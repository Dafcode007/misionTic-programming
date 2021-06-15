'''Challenge.2 adivinando competidores
Luego del poco éxito de Barbarita para obtener los nombres de competidores que le podrían ganar un negocio a Freydell a través de ingeniería social, Pedro ha decidido contratar a la Bruja Dioselina y al Mago Juanquini, quienes prometen darle esta información, pero con un costo muy alto. Pedro logró negociar a un precio que considera justo para que Dioselina y Juanquini le den al menos la inicial de los competidores que le podrían ganar un nuevo negocio.

Dioselina y Juanquini entregaron las iniciales de competidores que lograron identificar. Ante la pérdida de un nuevo negocio, Pedro revisó si empezaba las letras iniciales que Dioselina o Juanquini habían entregado. Si Dioselina identificó más iniciales correctas de competidores se especifica una ‘D’ y si Juanquini es quien identificó más se escribe 'J', pero si ambos identificaron el mismo número entonces se especifica una 'L'.

Realice un programa que reciba las iniciales adivinadas por Dioselina y las iniciales adivinadas por Juanquini (como cadena de caracteres) y una cadena de caracteres con las primeras letras de los competidores identificados por Pedro e imprima en consola lo que él escribió después de la revisión y verificación con la Bruja Dioselina y el Mago Juanquini.'''

#This function counts how many times a letter is found in a word
def letters_in_word(l:str, w:str) -> int:
    #we initialize one counter to zero
    counting_letters = 0
    #iterate over the string and count the number of times the letter of interest is present.
    for i in w:
        if i == l:
            counting_letters += 1
    return counting_letters

#solve
def solve(d:str, j:str, p:str) -> str:
    rta = []
    #we initialize two counters to zero
    count_dioselina = 0
    count_juanquini = 0
    for i in p:
        #We count how many times each letter of pedro's chain is in dioselina's and juanquini's chains.
        count_dioselina += letters_in_word(i, d)
        count_juanquini += letters_in_word(i, j)
        #We compare the number of letters guessed by Diocelina and juanquini and save the respective output in a array.
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
