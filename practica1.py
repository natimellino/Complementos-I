import sys

# Lee un grafo desde entrada éstandar y devuelve su representación como lista.

def lee_grafo_stdin():
    vertices = []
    aristas = []
    grafo = (vertices, aristas)
    nroLinea = 0
    cantVertices = 0
    for line in sys.stdin:
        if nroLinea == 0:
            cantVertices = int(line)
        elif nroLinea <= cantVertices:
            vertices.append(line[:len(line)-1:])
        else:
            linea = line.split()
            aristas.append((linea[0], linea[1]))
        nroLinea += 1
    return grafo

# Lee un grafo desde un archivo y devuelve su representación como lista.

def lee_grafo_archivo(nombre):
    vertices = []
    aristas = []
    grafo = (vertices, aristas)
    cantVertices = 0
    with open(nombre, 'r') as archivo:
        nroLinea = 1
        cantVertices = int(archivo.readline())
        for line in archivo.readlines():
            if nroLinea <= cantVertices:
                vertices.append(line[:len(line)-1:]) 
            else:
                line = line.split()
                aristas.append((line[0], line[1]))
            nroLinea += 1

    return grafo

# Recibe un grafo y lo muestra por pantalla.

def imprime_grafo_lista(grafo):
    print("Vértices:")
    for i in range(0, len(grafo[0])):
        print(grafo[0][i])
    print("Aristas: ")
    for j in range(0, len(grafo[1])):
        print(grafo[1][j])

# Recibe un grafo en forma de lista y devuelve su representación en la matriz de incidencia.

def crear_matriz(filas, cols):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(cols):
            matriz[i].append(0)
    return matriz

def grafo_a_incidencia(grafo):
    filas = len(grafo[1]) # Cantidad de aristas.
    cols = len(grafo[0]) # Cantidad de vértices.
    matriz = []
    # Creamos la matriz.
    for i in range(filas):
        matriz.append([])
        for j in range(cols):
            matriz[i].append(0)
    # Llenamos la matriz de incidencia como corresponde.
    for v in range(cols):
        for  a in range(filas):
            if grafo[0][v] in grafo[1][a]:
                matriz[a][v] = 1
    print(matriz)

# Dada una matriz de incidencia devuelve el grafo en forma de lista.

# Función auxiliar: devuelve los índices de la lista donde aparece un elemento dado.
def lista_indices(lista, elemento):
    indices = []
    for i in range(0, len(lista)):
        if lista[i] == elemento:
            indices.append(i)
    return indices


def incidencia_a_lista(matriz):
    cantVertices = len(matriz[0])
    cantAristas = len(matriz)
    vertices = []
    for j in range(0, cantVertices):
        vertices.append(j)
    aristas = []
    grafo = (vertices, aristas)
    for i in range(0, cantAristas):
        for vertice in vertices:
            arista = lista_indices(matriz[i], vertice)
            if len(arista) == 2:
                aristas.append(arista)
    return grafo

# Imprime un grafo en forma de matriz de incidencia.

def imprime_matriz_incidencia(matriz):
    filas = len(matriz)
    for i in range(filas):
        print(matriz[i])

# Transforma un grafo representado por listas a su representacion en matriz de adyacencia.   

def index(lista, elem):
    index = -1
    i = 0
    while index == -1 and i < len(lista):
        if lista[i] == elem:
            index = i
        i += 1
    return index


def lista_a_adyacencia(grafo):
    filas = len(grafo[1])
    cols = len(grafo[0])
    matriz = crear_matriz(filas, cols)
    vertices = grafo[0]
    aristas = grafo[1]
    for i in range(len(aristas)):
        v1 = aristas[i][0]
        v2 = aristas[i][1]
        indice1 = index(vertices, v1)
        indice2 = index(vertices, v2)
        matriz[indice1][indice2] = 1
        matriz[indice2][indice1] = 1
    return matriz

# defe

def adyacencia_a_lista(matriz):
    longitud = len(matriz)
    vertices = []
    for j in range(0, longitud):
        vertices.append(j)
    aristas = []
    grafo = (vertices, aristas)
    for i in range(longitud):
        for j in range(i, longitud):
            if matriz[i][j] == 1:
                aristas.append((i, j))
    return grafo


def main():
    #print(lee_grafo_stdin())
    #print(lee_grafo_archivo("grafo.txt"))
    matriz = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    grafo = lee_grafo_archivo("grafo.txt")
    # grafo_a_incidencia(grafo)
    imprime_grafo_lista(adyacencia_a_lista(matriz))
    #imprime_matriz_incidencia(lista_a_adyacencia(grafo))
main()