valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50,  'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

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
                    if letra in valores5:
                        return 0
                    if numRepes > 3:
                        return 0                               
                
                elif valores[ultimoCaracter] < valores[letra]:
                    if numRepes > 1: #No permite repeticiones en las restas
                        return 0
                    
                    if ultimoCaracter in valores5: #No permite restas de valores de 5
                        return 0
                    
                    distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                    if distancia > 2:
                        return 0
                    
                    numArabigo -= valores[ultimoCaracter]*2
                    numRepes = 1

                     
            
        else: #si el símbolo romano no es permitido devolvemos error
            return 0
            
        ultimoCaracter = letra

    return numArabigo



def arabigo_a_romano(numeroArabigo):
    numRomano = ''
    numero = numeroArabigo
    
    lenNumStr= len(str('%s'%(numero,))) 

    udArToRom = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
    decArToRom = {'0':'','1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
    centArToRom = {'0':'','1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
    udMillArToRom = {'0':'','1':'M', '2':'MM', '3':'MMM', '4':'(IV)', '5':'(V)', '6':'(VI)', '7':'(VII)', '8':'(VIII)', '9':'(IX)'}

    unidades = 0
    decenas = 0
    centenas = 0
    udMillar = 0

    # X
    if lenNumStr == 1:
        unidades = (str(numero)[-1])
        
        #conversión a romano
        udRom = udArToRom[str(unidades)]
        numRomano = udRom
        return numRomano
        
    # XX
    if lenNumStr == 2:
        unidades = (str(numero)[-1])
        decenas = (str(numero)[-2])
        
        #conversión a romano
        udRom = udArToRom[str(unidades)]
        decRom = decArToRom[str(decenas)]
        
        numRomano = decRom + udRom
        return numRomano
    
    # XXX
    if lenNumStr == 3:
        unidades = (str(numero)[-1])
        decenas = (str(numero)[-2])
        centenas = (str(numero)[-3])

        #conversión a romano
        udRom = udArToRom[str(unidades)]
        decRom = decArToRom[str(decenas)]
        centRom = centArToRom[str(centenas)]

        numRomano = centRom + decRom + udRom
        return numRomano
    
        
    # XXXX
    if lenNumStr == 4:
        unidades = (str(numero)[-1])
        decenas = (str(numero)[-2])
        centenas = (str(numero)[-3])
        udMillar = (str(numero)[-4])

        #conversión a romano
        udRom = udArToRom[str(unidades)]
        decRom = decArToRom[str(decenas)]
        centRom = centArToRom[str(centenas)]
        udMillRom = udMillArToRom[str(udMillar)]

        numRomano = udMillRom + centRom + decRom + udRom
        return numRomano



