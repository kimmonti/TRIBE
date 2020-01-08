#Mision 1
#Crear desde la línea de comandos un sistema donde podrás ingresar el monto que deseas cambiar, 
#el sistema debe de solicitar al usuario desde la terminal que ingrese el monto en USD 
#y la salida debe ser el monto cambiado a PYG. 
#También puedes hacer otro programa que convierta de PYG a USD.

price_us = input ("Este programa permite convertir monedas USD/PYG. Ingrese precio del dólar: ") #Solicita costo actual del dólar.
coinUSD = input("Ingrese la cantidad de dólares que desea convertir: ") #Solicita tipo de conversión.
print("Usted tiene", float(coinUSD) * float(price_us), "guaraníes.") #Según la conversión especificada transforma los datos ingresados a float y los procesa.

"""
price_us = input ("Este programa permite convertir monedas PYG/USD. Ingrese precio del dólar: ")
coinPYG = input("Ingrese la cantidad de guaraníes que desea convertir: ")
print("Usted tiene", float(coinPYG) / float(price_us), "dólares.")
"""
