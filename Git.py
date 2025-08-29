#1)
	print(‘Hola Mundo!’)

#2)
	nombre = input('¿Cómo te llamas? ')
print(f"Hola, {nombre}!")
#3)
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
residencia = input("Lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#4)
	#Calcular área y perímetro de una circunferencia
#A = πr²
#P = 2πr

from math import pi

radio = float(input("Ingrese el radio de su circunferencia: "))
area = pi*radio**2
perimetro = 2*pi*radio

print(f"Perímetro: {perímetro:.2f}\nÁrea: {area:.2f}")

#5) 
#Conversión de segundos a horas
#horas=segundos/3600

segundos = int(input("Ingrese el total de segundos: "))
horas = segundos/3600

print(f"Horas: {horas:.2f}.")
#6)
	#Tabla de multiplicar de un número ingresado por el usuario
num = int(input("Ingrese un número: "))
i = 1

print(f"Tabla de multiplicar de {num}")
while i>=1 and i<=10:
	print(f"{i} x {num} = ({i*num}"))
	i+=1




#7)
	#Ingreso de dos números distintos de cero, sumarlos, restarlos, multiplicarlos y dividirlos.
while True:
    num1 = float(input("Ingrese el primer número (distinto de 0): "))
    num2 = float(input("Ingrese el segundo número (distinto de 0): "))

    if num1 != 0 and num2 != 0:
        break
    print("Ambos números deben ser distintos de 0. Intente nuevamente.")

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")


#8)
#Calcular el IMC de una persona
#IMC = peso en kg/(altura en metros)^2

peso = float(input("Ingrese su peso, en kg: "))
altura = float(input("Ingrese su altura, en metros: "))

imc = peso/(altura**2)

print(f"IMC: {imc:.2f}")


#9)
#Celsius a Fahrenheit
#F = 9/5*Celsius+32

celsius = float(input("Ingrese su temperatura, en °C: "))
fahrenheit = 1.8*celsius+32

print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F.")


#10)
#Promedio de tres números ingresados por el usuario

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = (num1+num2+num3)/3

print(f"Promedio: {promedio:.2f}")
