# Ejercicio 1:
def make_set(lista):
    conj = {}
    for i in range(len(lista)):
        conj[lista[i]] = i
    return conj
# Ejercicio 2:
def find(elem, disjoint_set):
    return disjoint_set.get(elem)

# Ejercicio 3:
def union(id1, id2, dic):
    for k,v in dic.items():
        if v == id1:
            dic[k] = id2
    return dic

def componentes_conexas(grafo_lista):
    conj = make_set(grafo_lista[0])
    for comp in grafo_lista[1]:
        union(conj[comp[0]],conj[comp[1]],conj)
    values = set(conj.values())
    comp_conexas= []
    for val in values:
        componente = []
        for k,v in conj.items():
            if v == val:
                componente += [k]
        comp_conexas += [componente]
    return comp_conexas

def main():
    lista = ['a','b','c']
    conj = make_set(lista)
    print(conj)
    #print(find('a',conj))
    print(union(0, 1, conj))
    grafo = [['a','b','c','d'], [('a', 'b'), ('c','a')]]
    print(componentes_conexas(grafo))

main()
