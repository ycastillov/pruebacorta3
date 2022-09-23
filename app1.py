#Modificación 1
import random as rnd 
aleatorio = rnd.randint(1,1000)
c_i = 0
nrnd = 0

print('Intente adivinar el numero entre 1 y 1000 elegido por el programa')
while c_i <= 10 and nrnd != aleatorio:
  while True:
    try:
      nrnd = int(input('Ingrese un numero: '))
      break
    except ValueError:
      print('Ha introducido un valor no valido!')
  c_i = c_i + 1
    
  if nrnd == aleatorio:
    print('Felicidades!!, adivinaste el numero que es: ',aleatorio)
    print('La cantidad de intentos que realizo fueron: ',c_i)
  if nrnd < aleatorio:
    print('El numero buscado es mayor al ingresado')
  if nrnd > aleatorio:
    print('El numero buscado es menor al ingresado')

if c_i > 10 and nrnd != aleatorio:
  seguir = input('Te quedaste sin intentos y has perdido :c, pero puedes seguir jugando si quieres :3 [1. Si / 2. No]: ')

  while seguir != '2':
    if seguir == '1':
      while True:
        try:
          nrnd = int(input('Ingrese un numero: '))
          break
        except ValueError:
          print('Ha introducido un valor no valido!')
      c_i = c_i + 1
    
      if nrnd == aleatorio:
        print('Felicidades!!, adivinaste el numero que es: ',aleatorio)
        print('La cantidad de intentos que realizo fueron: ',c_i)
        break
      if nrnd < aleatorio:
        print('El numero buscado es mayor al ingresado')
      if nrnd > aleatorio:
        print('El numero buscado es menor al ingresado')
    else:
      print('Error al ingresar las opciones')
    
    seguir = input('Quieres seguir jugando ? [1. Si / 2. No]: ')
  