import grafo_ponderado as GRP


# Grafo ejemplo con listas de adyacencia y pesos asociados
grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]}


def testGrafo():
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('C'))   # Arcos desde un nodo

    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())                    # Comprobar si grafo vacío
    """
    print('Existe nodo A:', g.existNode('A'))       # Comprobar si existe nodo
    print('Existe nodo Z:', g.existNode('Z'))
    print('Existe arco A-C:', g.existEdge(['A', 'C']))  # Comprobar arco
    print('Existe arco A-Z:', g.existEdge(['A', 'Z']))

    print('\nAñadir nodos y arcos')
    g.addNode('E')              # Añadir nodo
    g.addEdge(('A', 'E'), 6)    # Añadir arco con el peso
    g.addEdge(('B', 'F'), 4)
    g.addEdge(('B', 'G'), 5)
    print('Grafo resultante')
    print(g)

    print('Medidas')
    print('Grado de B:', g.degree('B'))     # Obtener grado de un nodo
    print('Grado de D:', g.degree('D'))
    print('Delta:', g.Delta())              # Obtener Delta del grafo
    print('Orden:', g.order())              # Obtener orden
    print('Tamaño:', g.size())              # Obtener tamaño

    print('\nRecorridos')
    print("DFS('A'):", g.DFS('A'))          # Recorrido DFS
    print("BFS('A'):", g.BFS('A'))          # Recorrido BFS
    
    # Obtener todos los caminos posibles entre dos nodos
    print(g.findPaths('A', 'C'))
    # Obtener el camino más corto entre dos nodos
    path, weight = g.shortestPath('D', 'G')
    print(f'Dijkstra: ruta D-G:{path} peso:{weight}')
    
    print('\nEliminar arcos y nodos')
    g.removeEdge(['D', 'A'])    # Eliminar arco
    g.removeNode('C')           # Eliminar nodo
    print('Grafo resultante')
    print(g)
    print('Nodos aislados:', g.isolatedNodes()) # Visualizar nodos aislados
"""

if __name__ == '__main__':
    testGrafo()