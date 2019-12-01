valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50,  'D':500}

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:
        #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
        if letra in valores:  
                numArabigo += valores[letra]
                if ultimoCaracter == '':
                    pass
                elif valores[ultimoCaracter] > valores[letra]:
                    numRepes = 1
                    pass
                elif valores[ultimoCaracter] == valores[letra]:
                    numRepes += 1
                    if numRepes > 3:
                        return 0
                elif valores[ultimoCaracter] < valores[letra]:
                    if numRepes > 1:
                        return 0
                    if ultimoCaracter in valores5:
                        return 0
                    numArabigo -= valores[ultimoCaracter]*2
                    numRepes = 1
            
            
        else: #si el símbolo romano no es permitido devolvemos error
            return 0
            
        ultimoCaracter = letra

    return numArabigo

