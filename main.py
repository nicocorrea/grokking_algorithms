##
# Binary Search
##

from collections import deque
from typing import Any


def binary_search(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lista[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


##
# Selection Sort
##

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))


##
# Recursion
##

def countdown(i):
    print(i)
    if i == 0:
        return
    countdown(i - 1)


countdown(10)


def suma(arr):
    if arr:
        return arr[0] + suma(arr[1::])
    return 0


print(suma([1, 2, 3]))


def count_numbers(arr):
    if arr:
        return 1 + count_numbers(arr[1::])
    return 0


print(count_numbers([1, 2, 3, 4]))


def find_maximum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_maximum(arr[1::])
    return arr[0] if arr[0] > sub_max else sub_max


print(find_maximum([3, 20, 9, 2]))


def binary_search_recursive(arr, item, start, end):
    mid = (start + end) // 2
    if arr[mid] == item:
        return item
    if arr[mid] > item:
        return binary_search_recursive(arr, item, start, mid)
    else:
        return binary_search_recursive(arr, item, mid, end)


lista = [1, 2, 3, 4, 5]
print(binary_search_recursive(lista, 2, 0, len(lista)))


##
# Quick Sort
##

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))


##
# Implementing a graph for Breadth First Search
##

graph = {}
graph['me'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(person):
    return person[-1] == 'm'

def search_mango_seller(name, graph):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller.')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search_mango_seller('me', graph)


##
# Dijkstra's algorithm
##

graph["start"] = {
    'a': 6,
    'b': 2
}

graph["a"] = {
    'fin': 1
}

graph["b"] = {
    'a': 3,
    'fin': 5
}

graph["fin"] = {}

infinity = float('inf')
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []

def find_lowest_cost_node(costs) -> Any:
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(processed)


##
# Approximation algorithm - Greedy approach
##

states_needed = set(['met', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az'])
}

final_stations = set()

n = len(states_needed)
while n != 0:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station) if best_station != None else 0
    n -= 1

print(final_stations)