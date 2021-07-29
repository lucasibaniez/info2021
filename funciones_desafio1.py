"""
Desafío 1
    150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

    Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

    Un trozo de chicle tarda 5 años en degradarse. 

    Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.
"""

def obtener_anios_degradacion(tipo_material):
	if tipo_material == 1:
		return 150
	elif tipo_material == 2:
		return 1000
	elif tipo_material == 3:
		return 30
	elif tipo_material == 4:
		return 5    

def devolver_opcion():
	print("====================")
	print("SALVEMOS EL PLANETA")
	print("====================")
	print("Ingrese una de las siguientes opciones: ")
	print("0: SALIR")
	print("1: Bolsa de plástico")
	print("2: Botella PET")
	print("3: Envase tetrabrik")
	print("4: Chicle")
	print("====================")
	return input()

salio = False
es_valido = False
while not es_valido and not salio:
	opcion = devolver_opcion()
	if not opcion.isdigit():
		opcion = devolver_opcion()
		continue
	opcion = int(opcion)
	if opcion == 0:
		salio = True
	elif opcion>= 5:
		continue
	else:
		es_valido = True

if es_valido and not salio:
	anios_degradacion = obtener_anios_degradacion(opcion)

	print("El materia ingresado demora %s años en degradarse." % (anios_degradacion))
