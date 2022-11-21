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
#Importacion del lemario (1000 palabras en ingles)

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

    print(palabra) #BORRAR, ES PARA PRUEBAS
    
    for i in range(6): #dibujar un tablero de 6 filas que es el estandar de oportunidades y 4 columnas que corresponden a las letras
        for j in range(dificultad):
            print('🔲', end='')
        print()
    print('aciertos:', aciertos, 'fallos:', fallos)
    print("tiene 6 intentos para descubrir la palabra")
    for i in range(6): #aqui comienza el ciclo de intentos
        intento=str(input()).upper()

        while not (len(intento) == dificultad):
            print(f"La palabra debe contener: {dificultad} letras")
            intento=str(input()).upper()

        for i in range(dificultad): #Se imprime un cuadrado verde si la letra esta en el lugar correcto, uno amarillo si la letra no esta en el lugar correcto y uno negro si la letra no esta en la palabra, se sale del ciclo cuando terminan los intentos o acierta
            if intento[i] in palabra:
                if intento[i]==palabra[i]:
                    print('🟩', end='')
                else:
                    print('🟨', end='')
            else:
                print('⬛', end='')
        print()
        if intento==palabra: #si se introduce la palabra correcta se añade un punto a aciertos
                print('GANASTE!')
                aciertos+=1
                break
    if intento!=palabra: #si no se logra adivinar se agrega un fallo
        print('PERDISTE :(')
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
        dificultad=int(input())+3

        if (dificultad > 3) and (dificultad < 9):
            juego(dificultad)
        else:
            print("Ese valor no está permitido ...")
            continue
        
    else: #Opcion para que no lance error el juego
        continue

    #Impelementa método mimimi
    
    system("cls")