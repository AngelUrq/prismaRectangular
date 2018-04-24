import math

def distancia(x1,y1,z1,x2,y2,z2):
	return math.sqrt((x2 - x1)**2 +(y2 - y1)**2 + (z2 - z1)**2)

def productoPunto(vector1, vector2):
	return (vector1[0] * vector2[0]) + (vector1[1] * vector2[1]) + (vector1[2] * vector2[2])

def calcularVectores(coordenadas, indice1, indice2, tam):
	lista_vectores = []
	for i in range(tam):
		if(coordenadas[i] != coordenadas[indice1] and coordenadas[i] != coordenadas[indice2]):
			lista_vectores.append([coordenadas[i][0] - coordenadas[indice1][0],coordenadas[i][1] - coordenadas[indice1][1],coordenadas[i][2] - coordenadas[indice1][2]])
	return lista_vectores

def calcularVectoresPerpendiculares(vectores):
	vectores_perpendiculares = []

	for i in range(len(vectores)):
		cantidad_vectores_perpendiculares = 0
		for j in range(len(vectores)):
			if(vectores[i] != vectores[j]):
				if(productoPunto(vectores[i], vectores[j]) == 0):
					cantidad_vectores_perpendiculares += 1	
					if(cantidad_vectores_perpendiculares == 2):
						vectores_perpendiculares.append(vectores[i])	

	return vectores_perpendiculares

def calcularMagnitud(vector):
	return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

def calcularVolumen(vectores_perpendiculares):
	return calcularMagnitud(vectores_perpendiculares[0]) * calcularMagnitud(vectores_perpendiculares[1]) * calcularMagnitud(vectores_perpendiculares[2])

def calcularArea(vectores_perpendiculares,i1,i2):
	return calcularMagnitud(vectores_perpendiculares[i1]) * calcularMagnitud(vectores_perpendiculares[i2])

def calcularPerimetro(vectores_perpendiculares):
	return 2 * (calcularMagnitud(vectores_perpendiculares[0]) + calcularMagnitud(vectores_perpendiculares[2])) + 2 * (calcularMagnitud(vectores_perpendiculares[0]) + calcularMagnitud(vectores_perpendiculares[1])) + 2 * (calcularMagnitud(vectores_perpendiculares[1]) + calcularMagnitud(vectores_perpendiculares[2]))

def esPrismaRectangular(coordenadas):
	distancias_al_origen = []
	indice_primer_punto = 0

	for i in range(cantidad_coordenadas):
		distancias_al_origen.append(distancia(0,0,0,coordenadas[i][0],coordenadas[i][1],coordenadas[i][2]))
	for i in range(cantidad_coordenadas):
		if(distancias_al_origen[i] == min(distancias_al_origen)):
			indice_primer_punto = i

	distancias_al_primer_punto = []
	indice_vertice_opuesto = 0

	for i in range(cantidad_coordenadas):
		distancias_al_primer_punto.append(distancia(coordenadas[indice_primer_punto][0],coordenadas[indice_primer_punto][1],coordenadas[indice_primer_punto][2],coordenadas[i][0],coordenadas[i][1],coordenadas[i][2]))
	for i in range(cantidad_coordenadas):
		if(distancias_al_primer_punto[i] == max(distancias_al_primer_punto)):
			indice_vertice_opuesto = i

	vectores_primer_punto = calcularVectores(coordenadas, indice_primer_punto,indice_vertice_opuesto, cantidad_coordenadas)
	vectores_primer_punto_perpendiculares = calcularVectoresPerpendiculares(vectores_primer_punto)

	vectores_vertice_opuesto = calcularVectores(coordenadas, indice_vertice_opuesto, indice_primer_punto, cantidad_coordenadas)
	vectores_vertice_opuesto_perpendiculares = calcularVectoresPerpendiculares(vectores_vertice_opuesto)

	magnitudes_iguales = 0
	for i in range(len(vectores_primer_punto_perpendiculares)):
		for j in range(len(vectores_vertice_opuesto_perpendiculares)):
			if(calcularMagnitud(vectores_primer_punto_perpendiculares[i]) == calcularMagnitud(vectores_vertice_opuesto_perpendiculares[j])):
				magnitudes_iguales += 1
				
	if(magnitudes_iguales == 3):
		print("Perímetro: " + str(calcularPerimetro(vectores_primer_punto_perpendiculares)))
		print("Área 1: " + str(calcularArea(vectores_primer_punto_perpendiculares,0,1)))
		print("Área 2: " + str(calcularArea(vectores_primer_punto_perpendiculares,0,2)))
		print("Área 3: " + str(calcularArea(vectores_primer_punto_perpendiculares,1,2)))
		print("Volumen: " + str(calcularVolumen(vectores_primer_punto_perpendiculares)))
		return True
	else:
		return False

coordenadas = []
cantidad_coordenadas = 8

datos_ingresados_correctamente = True

try:
	for i in range(cantidad_coordenadas):
		coordenadas.append([])
		x = float(input(str(i + 1) + ". x: "))
		y = float(input(str(i + 1) + ". y: "))
		z = float(input(str(i + 1) + ". z: "))
		coordenadas[i].append(x)
		coordenadas[i].append(y)
		coordenadas[i].append(z)
		print()
except:
	print("Error al ingresar los datos. Inténtalo de nuevo")
	datos_ingresados_correctamente = False

if(datos_ingresados_correctamente):
	print("Coordenadas: " + str(coordenadas))
	if(esPrismaRectangular(coordenadas)):
		print("Es un prisma rectangular! :D")
	else:
		print("No es un prisma rectangular :(")