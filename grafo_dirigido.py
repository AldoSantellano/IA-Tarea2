# Grafo dirigido

import grafo as GR

class DirectedGraph(GR.Graph):
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de los nodos siguientes al nodo
    def __init__(self, graph={}):
        super().__init__(graph)

    # Devuelve una lista de los nodos aislados
    def isolatedNodes(self):
        return [n for n, e in self.graph.items() if self.inDegree(n) == 0]

    # Semigrado interior 
    def inDegree(self, node):
        return len([n for n, e in self.graph.items() if node != n and node in e])