'''
01 - Bucles (while)
 Se utiliza para ejecutar un bloque de código repetidamentee mientras se cumpla una condición
'''

# print('\n Bucle while:')
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1 # es super importante parra evitar un bucle infinito

# otra opción es cuando se hace un break
# while True:
#     print(contador)
#     contador =+1
#     if contador == 5:
#         break # sale del bucle

# continue, que lo que hace es saltar esa iteración en concreto
print('\n Bucle con continue')
contador = 0
while contador < 10:
    contador += 1
    
    if contador % 2 == 0:
        continue
        #👇
    print(contador)

    # else, esta condición cuando se ejecuta?
    print("\ Bucle while con else:")
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
    else:
        print('El bucle ha terminado')