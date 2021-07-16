def determinar_tipo_contrato(l:list) -> list:
    rta = []
    for i in l:
        if i not in rta:
            rta.append(i);
    return rta

def buscar_mas_informacion(lc:list, ln: list, c:str) -> list:
    rta = []
    for i in lc:
        if ln[i] == c:
            rta.append(i)
    return rta

def comprar_informacion(lr:list, lc:list) -> list:
    rta = []
    for i in lr:
        if i not in lc:
            rta.append(i)
    return rta

def intercambiar_informacion(lr:list, lc:list) -> list:
    counter1 = 0
    counter2 = 0
    for i in lr:
        if i not in lc:
            counter1 += 1
    for i in lc:
        if i not in lr:
            counter2 += 1
    if counter1 < counter2:
        return counter1
    else:
        return counter2
