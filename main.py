import descripcion
animal = input('ingresa que animal quiers registrar: ')

if animal == 'perro':
    nombre = input('escribe su nombre: ')
    edad = int(input('escribe su edad: '))
    raza = input('escribe su raza: ')
    color = input('escribe su color: ')
    print(descripcion.perro(nombre, edad, raza, color))

elif animal == 'gato':
    nombre = input('escribe su nombre: ')
    edad = input('escribe su edad: ')
    raza = input('escribe su raza: ')
    color = input('escribe su color: ')
    descripcion.perro(nombre, edad, raza, color)
    print(descripcion.gato(nombre, edad, raza, color))
else:
    print('dato incorrecto !')

#algoritmos de busqueda
#bubble sort
#insertion sort
#merge sort
#quick sort
#selection sort
#binary shearch tree