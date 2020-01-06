#Mision 1
#Crear desde la línea de comandos un sistema donde podrás ingresar el monto que deseas cambiar, 
#el sistema debe de solicitar al usuario desde la terminal que ingrese el monto en USD 
#y la salida debe ser el monto cambiado a PYG. 
#También puedes hacer otro programa que convierta de PYG a USD.

#Solicita tipo de conversión.
coin = input("Ingrese tipo de conversión USD/PYG o PYG/USD: ")

#Solicita costo actual del dólar.
price_us = input ("Ingrese precio del dólar: ")

#Según la conversión especificada transforma los datos ingresados a float y los procesa.
if coin == "USD/PYG" or coin == "usd/pyg":
    amount = input("Ingrese la cantidad de US Dólares: ")
    convertion = float(amount) * float(price_us)
    print("Usted tiene", convertion, "guaraníes.")
elif coin == "PYG/USD" or coin == "pyg/usd":
    amount = input("Ingrese la cantidad de PY Guaraníes: ")
    convertion = float(amount) / float(price_us)
    print("Usted tiene", convertion, "dólares.")