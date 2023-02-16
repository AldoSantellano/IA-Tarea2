
import random

num_nodos = 10;

def create_instance():
    instance = {}
    for i in range(1,num_nodos+1):
        cantidad_adyacentes = random.randint(1, num_nodos-1);
        lista_adyacencia = random.sample(range(1, num_nodos),cantidad_adyacentes);
        while(i in lista_adyacencia):
            cantidad_adyacentes = random.randint(1, num_nodos-1);
            lista_adyacencia = random.sample(range(1, num_nodos),cantidad_adyacentes);
    
        lista_tuplas = [];
        for j in range(0,len(lista_adyacencia)):
            lista_tuplas.append((lista_adyacencia[j], random.randint(1,100)))

        instance[i] = lista_tuplas;
    #print(instance);
    return(instance);