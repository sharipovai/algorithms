def make_parents_hash_table(graph):
    parents = {}
    for node in graph.keys():
        if node == "start":
            for i in graph[node].keys():
                parents[i] = node
    parents['end'] = None
    return parents

def make_costs_hash_table(graph):
    costs = {}
    for node in graph.keys():
        if node == "start":
            for i in graph[node].keys():
                costs[i] = graph[node][i]
        elif not(node in costs.keys()):
            costs[node] = float("inf")
            
    return costs
    
def find_lower_node(costs, done_nodes):
    lower_node = float("inf")
    lower_costs_node = None
    for node in costs:
        if node not in done_nodes and costs[node] < lower_node:
            lower_node = costs[node]
            lower_costs_node = node
    return lower_costs_node

def dijkstra_search(graph):
    #Создаем хеш таблицу для родителей
    parents = make_parents_hash_table(graph)
    #Создаем хеш таблицу для суммирования значений граней графов
    costs = make_costs_hash_table(graph)
    done_nodes = []
    node = find_lower_node(costs, done_nodes)
    while node is not None:
        for sub_node in graph[node].keys():
            cost = graph[node][sub_node]
            new_cost = costs[node] + cost
            if new_cost < costs[sub_node]:
                costs[sub_node] = new_cost
                parents[sub_node] = node
        done_nodes.append(node)
        node = find_lower_node(costs, done_nodes)  
    return costs['end']

#Создаем 1 граф связей
graph = {}
graph['start'] = {}
graph['start']['A'] = 5
graph['start']['C'] = 2
graph['A'] = {}
graph['A']['B'] = 4
graph['A']['D'] = 2
graph['B'] = {}
graph['B']['D'] = 6
graph['B']['end'] = 3
graph['C'] = {}
graph['C']['A'] = 8
graph['C']['D'] = 7
graph['D'] = {}
graph['D']['end'] = 1
graph['end'] = {}

#Создаем 2 граф связей
graph2 = {}
graph2['start'] = {}
graph2['start']['A'] = 10
graph2['A'] = {}
graph2['A']['B'] = 20
graph2['B'] = {}
graph2['B']['C'] = 1
graph2['B']['end'] = 30
graph2['C'] = {}
graph2['C']['A'] = 1
graph2['end'] = {}
            
print(dijkstra_search(graph))
print(dijkstra_search(graph2))