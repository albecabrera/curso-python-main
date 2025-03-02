camiseta = {
"color" : "rojo",
"talla" : "L",
"precio" : 100,
"unidades" : 10
}
 # Acceso a los elementos del diccionario
print(camiseta["color"])
print(camiseta["talla"])
print(camiseta["precio"])
print(camiseta["unidades"])

camiseta["unidades"] = 25
print(f"Hay {camiseta['unidades']} unidades en el almacen")

numero1 = 10
numero2 = 20.5
suma = numero1 + numero2
print(f"El resultado de la suma es: {suma}")


# otro ejemplo más:
numero = 100.43
					  
numero_entero = int(numero) # Se convierte en int

print(numero)
print() # Esto deja un espacio
print(numero_entero)
