#importamos biblioteca y declaramos variable
import random

caracteres = ['!','#','$','%','&','?','¿','¡','*','+','"']

frase = (input('Ingrese su contraseña: '))



#primera condicion hacer fuincion
while (4 > (len(frase.split())) or 10 < (len(frase.split()))):
	frase = input ("Ingrese una contraseña que este en el rango de 4 a 10 en palabras: ")




#segunda condicion (hacer funcion)
while ( (6 > len(frase.replace (" ","")))  or (50 < len(frase.replace (" ","")))):
	frase = input ('Ingresa una contraseña que este en el rango de 6 a 50 caracteres: ')


#Quitar espacios a frase
contrasena = frase.replace(' ','')

#Poner dos simbolos aleatorios
contrasena = (random.choice(caracteres)+random.choice(caracteres)+contrasena+random.choice(caracteres)+random.choice(caracteres))


#cambiar letras a numeros

letras_mayus =  'AEIOTB'
letras_minus = 'aeiotb'
numeros = '431078'

cambio = contrasena.maketrans(letras_mayus,numeros)
contrasena = contrasena.translate(cambio)
cambio = contrasena.maketrans(letras_minus,numeros)
print (frase)
print (contrasena.translate(cambio))




