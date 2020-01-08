print("Este programa imprime los números de un rango cualquiera donde, para los múltiplos de tres imprime Fizz en lugar del número y para los múltiplos de cinco imprime Buzz. Para los números que son múltiplos de tres y cinco, escribe FizzBuzz")

def fizzbuzzgame(minimum,maximum):
  list_number = []
  for x in range(minimum,maximum):
    if x % 3 == 0:
        list_number.append("Fizz")
    elif x % 5 == 0:
        list_number.append("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        list_number.append("FizzBuzz")
    else:
        list_number.append(x)
  print(list_number)

first= int(input("Inserte el valor mínimo del rango:"))
last= int(input("Inserte el valor máximo del rango:"))
fizzbuzzgame(first,last)

