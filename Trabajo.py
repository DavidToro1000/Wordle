from os import system
import random
#TRABAJO FINAL ESTRUCTURAS DE DATOS
"""
INTEGRANTES:
DAVID ESTEBAN TORO ARANGO  
MANUEL GALLEGO
CARLOS DAVID ARANGO
JERONIMO GOMEZ RESTREPO

Fuente del lemario: https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt
"""
#Importacion del lemario (10000 palabras en ingles)

original=open('1-10000.txt', mode='r')

lemario={4:list(), 5:list(), 6:list(), 7:list(), 8:list()} #Este diccionario contendrá el lemario, cada clave guarda las palabras con un determinado numero de digitos

for palabra in original:
    if '\'' in palabra:  #Es posible que las palabras tengan el caracter ', por simplicidad estas palabras no se toman en el lemario
        continue   
    elif len(palabra)==5:
        palabra=palabra[:-1]
        lemario[4].append(palabra.upper())
    elif len(palabra)==6:
        palabra=palabra[:-1]
        lemario[5].append(palabra.upper())
    elif len(palabra)==7:
        palabra=palabra[:-1]
        lemario[6].append(palabra.upper())
    elif len(palabra)==8:
        palabra=palabra[:-1]
        lemario[7].append(palabra.upper())
    elif len(palabra)==9:
        palabra=palabra[:-1]
        lemario[8].append(palabra.upper())

#Función que ejecuta el juego según la dificultad seleccionada
def juego(dificultad):
    global aciertos
    global fallos

    palabra=random.choice(lemario[dificultad]) #se selecciona palabra aleatoria del lemario
    
    for i in range(6): #dibujar un tablero de 6 filas que es el estandar de oportunidades y la columnas que corresponden a las letras de la dificultad
        for j in range(dificultad):
            print('🔲', end='')
        print()
    print('aciertos:', aciertos, 'fallos:', fallos) #Imprime el contador de aciertos y fallos en pantalla
    print("tiene 6 intentos para descubrir la palabra")
    for i in range(6): #aqui comienza el ciclo de intentos
        intento=str(input()).upper() #Se pone en mayuscula el intento para normalizarlo y que los caracteres hagan match

        while not (len(intento) == dificultad): #pequeño ciclo para manejo de errores
            print(f"La palabra debe contener: {dificultad} letras")
            intento=str(input()).upper()

        verde = set() #En este set se guardan las letras que estan en el lugar correcto
        cantidad={} #En este diccionario se guardan la cantidad de ocurrencia de las letras en el intento y la cantidad de letras en la palabra correcta, esto se usa para que no imprima mas cuadros amarillos que la cantidad de x letra en la palabra correcta
        for i in range(dificultad):
            if intento[i] == palabra[i] and intento[i] :
                verde.add(intento[i])

        for i in range(dificultad): #Se imprime un cuadrado verde si la letra esta en el lugar correcto, uno amarillo si la letra no esta en el lugar correcto y si no sobrepasa la cantidad de letras de la palabra original y uno negro si la letra no esta en la palabra o si hay mas letras de un tipo que en la palabra correcta, se sale del ciclo cuando terminan los intentos o acierta
            if intento[i] in palabra:
                if intento[i] not in cantidad:
                    cantidad[intento[i]]=[intento.count(intento[i]), palabra.count(intento[i])]
                if intento[i] != palabra[i] and intento[i] in verde and cantidad[intento[i]][0]<=cantidad[intento[i]][1]:
                    print('🟨', end='')
                    cantidad[intento[i]][0]-=1
                elif intento[i] != palabra[i] and intento[i] in verde:
                    print('⬛', end='')
                    cantidad[intento[i]][0]-=1
                elif intento[i] != palabra[i] and cantidad[intento[i]][0]<=cantidad[intento[i]][1]:
                    print('🟨', end='')
                    cantidad[intento[i]][0]-=1
                elif intento[i]==palabra[i]:
                    print('🟩', end='')
                    cantidad[intento[i]][0]-=1
                    cantidad[intento[i]][1]-=1
                else:
                    print('⬛', end='')
                    cantidad[intento[i]][0]-=1
            else:
                print('⬛', end='')
        print()
        if intento==palabra: #si se introduce la palabra correcta se añade un punto a aciertos
                print('GANASTE!')
                aciertos+=1
                break
    if intento!=palabra: #si no se logra adivinar se agrega un fallo
        print('PERDISTE :(')
        print('La palabra correcta era:', palabra)
        fallos+=1
    print('presiona cualquier tecla')
    input()

#Definición de variables

aciertos=0 #Esta variable guarda los aciertos para mostrarlos en pantalla
fallos=0 #Esta variable guarda los fallos para mostrarlos en pantalla

#Aqui comienza el juego
while True: #Ciclo general
    print('Bienvenido a wordle, selecciona una opción (escribe el numero correspondiente):')
    print('1. Nueva partida')
    print('2. Salir del juego')
    print('aciertos:', aciertos, 'fallos:', fallos)
    opcion=str(input())
    if opcion=='2': #Esta opcion termina el programa definitivamente
        print("Gracias por jugar")
        break
    elif opcion=='1': #Esto continua el juego
        system("cls")
        print('Seleccione un nivel de dificultad:')
        print('1. 4 letras')
        print('2. 5 letras')
        print('3. 6 letras')
        print('4. 7 letras')
        print('5. 8 letras')
        dificultad = input()
        if dificultad.isdigit():
            dificultad = int(dificultad)
            dificultad+=3
            if (dificultad > 3) and (dificultad < 9): #Ejecuta el juego
                juego(dificultad)
            else:
                print("Ese valor no está permitido ...")
                continue
        else:
            print("Ese valor no está permitido ...")
            continue
        
    else: #Opcion para que no lance error el juego
        continue

    #Impelementa método mimimi
    
    system("cls")