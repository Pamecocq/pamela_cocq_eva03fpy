from pathlib import Path
import json
home = Path (__file__).parents


import os
'''
Esta tienda vende pinturas 
---PARAMS---
----TIENDA DE PINTURAS----
jdonf_file
'''
lista = ('codigo, nombre')

menup = ['Ver listado de pinturas',
         'Buscar pinturas',
         'Agregar pinturas',
         'Eliminar pintura',
         'Exportar pintura']
stock = {380560: ['pintura acrilica', 'color', 1000],
         380560: ['pintuta latex', 'color', 1000]}
tipo = ('acrilico','latex')
os.system('cls')


while True:
    ans = (menup)
    if ans == '1':
        print('Quieres ver el Listado de pinturas\n1. si\n2. No')
        os.system('cls')
    elif ans =='2':
        print('Que buscas:')
        os.system('cls')
    elif ans =='3':
        while True:
            codigo = codigo 
        print(' agregar codigo: ')
        os.system('cls')
    elif ans =='4':
        pass
        os.system('cls')
    elif ans =='5':
        pass
    else:
        print('adios\n')


#Código: una serie numérica de 6 dígitos, que debe comenzar en 380560. Este dato debe asignarse automáticamente al crear la pintura.
#Nombre: nombre del color
#Tipo: Acrílico o Látex
#Valor: Precio guardado en formato numérico
#Stock: cantidad guardada en formato numérico