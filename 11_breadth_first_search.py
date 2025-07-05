# the shortest path problem
# breadth-first search is used to solve the shortest path problem.

from collections import deque

graph = {}
graph["you"] = ["bob", "claire", "alice"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")

