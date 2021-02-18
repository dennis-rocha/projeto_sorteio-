import random

def raffle(numList): #FUNÇÃO PARA GERAR UM NUMERO RANDÔMICO... PENSEI QUE IRIA SER INTERESSANTE CRIAR UM MÓDULO SÓ PARA ISSO, MAS NEM CRIEI MUITA COISA
    numRuffle = random.randint(1,numList)
    return numRuffle