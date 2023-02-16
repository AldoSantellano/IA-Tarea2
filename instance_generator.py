 
import random


'''
def create_instance(num_nodos):
    instance = {}
    for i in range(1,num_nodos+1):
        # Cantidad de nodos adyacentes tiene el nodo i
        cantAdyacentes = random.randint(1,num_nodos-1)
        lista_nodos_adyacentes = random.sample(range(1,num_nodos),cantAdyacentes)
        while(i in lista_nodos_adyacentes):
            cantAdyacentes = random.randint(1, num_nodos-1)
            lista_nodos_adyacentes = random.sample(range(1,num_nodos),cantAdyacentes)

        lista_tuplas=[]
        for j in range(0,len(lista_nodos_adyacentes)):
            lista_tuplas.append((lista_nodos_adyacentes[j],random.randint(1,1000)))
        instance[i] = lista_tuplas

    return(instance) '''