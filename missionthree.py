print("Este programa imprime los números de un rango cualquiera donde, para los múltiplos de tres imprime Fizz en lugar del número y para los múltiplos de cinco imprime Buzz. Para los números que son múltiplos de tres y cinco, escribe FizzBuzz")

def fizzbuzzgame(minimum,maximum): #Definimos la variable del juego
  list_number = [] #Creamos una lista vacía
  for x in range(minimum,maximum): #Iniciamos un bucle for con rangos a introducir
    if x % 3 == 0 and x % 5 == 0: #Verificamos si el número del rango es múltiplo de 3 y 5
        list_number.append("FizzBuzz") #Agregamos FizzBuzz en el lugar del número
    elif x % 5 == 0: #Verificamos si el número del rango es múltiplo de 5
        list_number.append("Buzz") #Agregamos Buzz en el lugar del número
    elif x % 3 == 0: #Verificamos si el número del rango es múltiplo de 3
        list_number.append("Fizz") #Agregamos Fizz en el lugar del número
    else:
        list_number.append(x) #Agregamos a la lista el resto de los números
  print(list_number) #Imprimimos la lista vacía

first= int(input("Inserte el valor mínimo del rango:")) #Introducimos el valor mínimo del rango
last= int(input("Inserte el valor máximo del rango:")) #Introducimos el valor máximo del rango
fizzbuzzgame(first,last) #Llamamos a la función

