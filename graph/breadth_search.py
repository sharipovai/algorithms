#Реализация поиска в ширину на графе через очередь
from collections import deque
def breadth_search(name):
    people_queue = deque()
    people_queue += graph[name]
    searched = []
    while people_queue:
        guy = people_queue.popleft()
        if guy not in searched and isSeller(guy):
            return guy
        else:
            searched.append(guy)
            people_queue += graph[guy]
    return "Nobody is seller"

def isSeller(name):
    return True if name == "Kate" else False

#Граф списка друзей
graph = {'I': ['Mike', 'John'],
         'Mike': ['Ann', 'Ted'],
         'John': ['Rose'],
         'Ann': ['Jack'],
         'Ted': ['Karen', 'Alex'],
         'Rose': [],
         'Jack': [],
         'Karen': ['Kate'],
         'Alex': []        
        }
print(breadth_search('I'))