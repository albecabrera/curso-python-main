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