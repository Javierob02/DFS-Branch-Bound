from node import *


# Añadir parámetro 'item_count' a Node

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []

    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...
    nodo_raiz = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(nodo_raiz)

    # Mientras haya nodos en la lista de nodos vivos
    # ...
    taken = []
    value = 0

    while alive:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)


        # Node(index, taken, value, room, item_count)
        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append) | Pasa value y room de Padre | Calcular estimate
        #    2) Ramificamos (branch) por la izquierda (append) | Value = Value de Padre + Vindex | Room = Room de Padre - Windex | Calcular estimate
        # ...
        #Node(index, taken, value, room)

        if (current.estimate(items) < value) or (current.index >= len(items)) or (current.room < 0):
            continue
        else:
            NodoDer = Node(current.index + 1, current.taken, current.value, current.room)
            alive.append(NodoDer)
            val_izq = current.value + items[current.index][1]
            room_izq = current.room - items[current.index][2]
            taken_izq = current.taken.copy()
            taken_izq.append(current.index + 1)
            NodoIzq = Node(current.index + 1, taken_izq, val_izq, room_izq)
            alive.append(NodoIzq)

        if ((current.value + items[current.index][1]) > value):
            if ((current.room - items[current.index][2]) > 0):
                value = current.value + items[current.index][1]
                taken = taken_izq

    return value, taken, visiting_order