from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#creando mi primera vista por defecto
def inicio_ver(request,*cadena,**cadenaID):
    return render(request,"home.html")
#Creando mi vista inicio
def home_ver(*cadena,**cadenaID):
    return HttpResponse("hola mundo. Esta tiene un descuento del 20%")
#Creando mi vista inicio

#Creando vista descuento '''
'''

def descuento(*cadena,**cadenaID):
    return HttpResponse("hola mundo. Esta tiene un descuento del 50%")
'''

#--Semana 9--#

#Primera pregunta
potencias = []
for number in [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]:
    cuadrado = number * number
    potencias.append(cuadrado)
suma_pot = 0
for i in potencias:
  suma_pot= suma_pot + i
respuesta1 = suma_pot



#Segunda pregunta
sum_p=0
n=200
for i in range(n+1):
    sum_p=sum_p+i

#------------------#

#Tercera pregunta
perritos = ["dálmata", "labrador", "doberman","chihuahua","pastor alemán", "perro peruano", "alaska", "bulldog francés", "Shih Tzu", "Gran Danés"]
for i in perritos:
    print(i)
respuesta3 = perritos



#Cuarta pregunta
pot_5 = []
n = 1
#Estructura repetitiva for
for i in range(0,15):
    n = n * 5
    pot_5.append(n)
#-------------------------------------------
#Quinta pregunta
import random  
numbers = [ ]  
for val in range(0, 11):  
    numbers.append( random.randint( 0, 11 ) )  
for num in range( 0, 11 ):  
    for i in numbers:  
        if num == i:  
            print( num, end = " " )  


# Semana 11
#Pregunta1
sem11_num = []
current_number = 1
#Mientras que el current_number sea menor o igual a 10
while current_number <=30: 
    #Imprimir current_number mientras se le suma 1
    sem11_num.append(current_number)
    current_number += 1
    
#Pregunta2
#Variable acumuladora
suma=0
#Entrada del usuario
n= 5837564
#Bucle con while cuando n es diferente de 0
while n!=0:
    digito=n%10
    suma+=digito
#División sin el cociente
    n=n//10
dígitos_sum = suma

#Pregunta 3
#Tabla 
tabla_mult = 15
inicio = 1
tabla = []
while inicio <= 12:
  resultado = tabla_mult * inicio
  línea = str(tabla_mult) + " * " + str(inicio) + " = " + str(resultado)
  tabla.append(línea)
  inicio += 1
respuesta6 = tabla

#Pregunta 4
números = [45, 68, 96, 32, 41, 53, 25, 36, 99, 25,12,13,55,98,102,115,117,36,127, 205]
mayor_num = números[0]
i = 1

while i < len(números):
  if números[i] > mayor_num:
    respuesta7 = números[i]
  i += 1

#Pregunta5
# Número a evaluar
evaluado = 23

# empezamos con 2
divisor = 2

# bucle while para verificar que sí sea prino
while divisor < evaluado:
    if num % divisor == 0:
        # Si es divisible entonces no es primo
        negativo = str(evaluado) + " no es un número primo"
        break
    else:
        divisor += 1
else:
    positivo = str(evaluado) + " sí es un número primo"
positivo = str(evaluado) + " sí es un número primo"

#Semana 12
# Pregunta 1
#Variable a: Número designado
a = 50
#Variable b: Acumulador
b = 0
#Ciclo while
while b < a:
  b = b + 1
if a % 2 == 0:
  b = b - 1
else:
  b = b + 0
respuesta11 = (b - 1) / 2

#Pregunta 2
import random
n = 0
lanzamientos = []
while True:
  n = n + 1
  dado1 = random.randint(1, 6) 
  dado2 = random.randint(1, 6)
  print(f"Resultados de los dados: {dado1} y {dado2}")
  lanzamientos.append("Resultado "+ str(n) + ": " + str(dado1) + " y " + str(dado2))
  if dado1 == dado2:
    print("Los dos dados dieron el mismo número")
    break
respuesta12 = lanzamientos
print (respuesta12)

#Pregunta 3
import random
import string

#imprimer contraseñas
a = 0
n = 5
contraseñas = []
letters = string.ascii_lowercase
while a < 10:
  a = a + 1
  n = n + 1
  print (''.join(random.choice(letters) for i in range(n)))
  contraseñas.append(''.join(random.choice(letters) for i in range(n)))
  if a > n:
    break
print(contraseñas)
respuesta13 = contraseñas

#Pregunta 4
radio_estado = ["encendido", "apagado", "encendido", "apagado", "encendido"]

chequeo_radio = []
compare_status = "encendido"


i = 0
while i < len(radio_estado):

    print(f"Radio {i+1} está {radio_estado[i]}")
    chequeo_radio.append(f"Radio {i+1} is {radio_estado[i]}")

    if radio_estado[i] == len(radio_estado):
        break 
    
    i += 1 
respuesta14 = chequeo_radio

#Pregunta 5 
import random
num_list = []
while True:
    num = random.randint(1, 10) 
    print(num)
    num_list.append(num)
    if num == 5:
        break
print (num_list)
respuesta_15 = num_list 





#Impresión
def actividades_ver(request,*cadena,**cadenaID):
    return render(request,"Tarea.html" ,{'respuesta1':respuesta1, 'respuesta2':sum_p , 'perritos': perritos, 
    'pot_5': pot_5,'numbers': numbers, 'sem11_num': sem11_num,'dígitos_sum':dígitos_sum, 'respuesta6': respuesta6,'números':números, 
    'respuesta7':respuesta7, 'positivo':positivo, 'respuesta11':respuesta11, 'respuesta12': respuesta12, 'respuesta13': respuesta13, 'radio_estado':radio_estado,'respuesta14':respuesta14, 'respuesta15':num_list,},)
    


    

#------------------------------------------------------------#
#Una página dinámica con variables
def descuento(request,*cadena,**cadenaID):
    return render(request,"descuento50.html", {'valor':suma})
#return HttpResponse("hola mundo. Esta tiene un descuento del 50%")
#