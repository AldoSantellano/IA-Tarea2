import grafo_ponderado as GRP
import instance_generator as ig

# Grafo ejemplo con listas de adyacencia y pesos asociados
'''grafo = {'A': [('B', 1), ('C', 2), ('D', 3)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5), ('E', 5)],
         'D': [('A', 3), ('C', 5), ('E', 5), ('G', 6)],
         'E': [('C', 2), ('G', 4), ('D', 5)],
         'G': [('A', 3), ('C', 5)]} '''
#Modifique el grafo de ejemplo para probar mejor Dijkstra, pero el inicial lo guarde en la pestaña "grafo.py"

def testGrafo():
    grafo = ig.create_instance(50)
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo
    while (len(g.isolatedNodes())>0):
        grafo = ig.create_instance(50);
        g = GRP.WeightedGraph(grafo); 

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    #print('Arcos desde el nodo C:', g.edges('C'))   # Arcos desde un nodo

    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())                    # Comprobar si grafo vacío

        
     # Obtener el camino más corto entre dos nodos
    #path, weight = g.shortestPath('1', '50')
    #print(f'Dijkstra: ruta 1-10:{path} peso:{weight}')

if __name__ == '__main__':
    testGrafo()