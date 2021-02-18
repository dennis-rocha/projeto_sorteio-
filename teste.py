import time

for i in range(0,101):
    time.sleep(0.1)
    if i < 19:
        print(f"Carregando base de dados {i}")
    elif i < 46:
        print(f"Escolhendo valor aleatorio {i}")
    elif i < 75:
        print(f"Recuperando dados {i}")
    elif i < 88:
        print (f"carregando nome {i}")
    elif i < 99:
        print(f"Só mais alguns instantes... {i}")
    elif i < 100:
        print(f"Finalizado")
        
    #setText("")
        
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    