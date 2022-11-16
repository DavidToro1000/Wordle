#TRABAJO FINAL ESTRUCTURAS DE DATOS
"""
INTEGRANTES:
DAVID ESTEBAN TORO ARANGO  
MANUEL GALLEGO
CARLOS DAVID ARANGO
JERONIMO GOMEZ RESTREPO

Fuente del lemario: https://gist.github.com/deekayen/4148741
"""
#Importacion del lemario (1000 palabras en ingles)

original=open('1-1000.txt', mode='r')

lemario={4:set(), 5:set(), 6:set(), 7:set(), 8:set()} #Este diccionario contendrá el lemario, cada clave guarda las palabras con un determinado numero de digitos

for palabra in original:
    if '\'' in palabra:  #Es posible que las palabras tengan el caractr ', por simplicidad estas palabras no se toman en el lemario
        continue   
    elif len(palabra)==5:
        palabra=palabra[:-1]
        lemario[4].add(palabra.upper())
    elif len(palabra)==6:
        palabra=palabra[:-1]
        lemario[5].add(palabra.upper())
    elif len(palabra)==7:
        palabra=palabra[:-1]
        lemario[6].add(palabra.upper())
    elif len(palabra)==8:
        palabra=palabra[:-1]
        lemario[7].add(palabra.upper())
    elif len(palabra)==9:
        palabra=palabra[:-1]
        lemario[8].add(palabra.upper())
original.close()
print(lemario)