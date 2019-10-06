# Determina si un camino es euleriano.

import unittest

def esCaminoEuleriano(grafo, camino):
    aristas = grafo[1]
    corregidas = []
    longCamino = len(camino)

    if longCamino != len(aristas):
        return False

    if longCamino != 0:
        ultimaVisitada = camino[0][0]

    for arista in camino:
        if arista in aristas and arista not in corregidas and arista[0] == ultimaVisitada:
            corregidas.append(arista)
            ultimaVisitada = arista[1]
        else:
            return False

    return True

def esCicloEuleriano(grafo, ciclo):
    longCiclo = len(ciclo)
    flag = esCaminoEuleriano(grafo, ciclo)

    if flag and longCiclo != 0:
        flag = ciclo[0][0] == ciclo[longCiclo - 1][1]

    return flag

def esCaminoHamiltoniano(grafo, camino):
    vertices = grafo[0]
    aristas = grafo[1]
    corregidas = []
    longCamino = len(camino)

    if longCamino == 0:
        return len(vertices) == 0

    if longCamino != len(vertices) - 1:
        return False

    ciudadInicial = camino[0][0]
    ultimaVisitada = camino[0][0]

    for arista in camino:
        if arista in aristas and ultimaVisitada not in corregidas and arista[0] == ultimaVisitada:
            corregidas.append(ultimaVisitada)
            ultimaVisitada = arista[1]
        else:
            return False

    return True

def esCicloHamiltoniano(grafo, ciclo):
    vertices = grafo[0]
    aristas = grafo[1]
    corregidas = []
    longCiclo = len(ciclo)

    if longCiclo == 0:
        return len(vertices) == 0

    if longCiclo != len(vertices):
        return False

    ciudadInicial = ciclo[0][0]
    ultimaVisitada = ciclo[0][0]

    for arista in ciclo:
        if arista in aristas and ultimaVisitada not in corregidas and arista[0] == ultimaVisitada:
            corregidas.append(ultimaVisitada)
            ultimaVisitada = arista[1]
        else:
            return False

    return ciudadInicial == ultimaVisitada

def tieneCaminoEuleriano(grafo):
    vertices = grafo[0]
    aristas = grafo[1]
    grados = [0] * len(vertices)

    if len(aristas) == 0:
        return True

    for arista in aristas:
        grados[vertices.index(arista[0])] += 1
        grados[vertices.index(arista[1])] += 1

    cantImpares = 0

    for grado in grados:
        if grado % 2 != 0:
            cantImpares += 1

    return cantImpares == 2
