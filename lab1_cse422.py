# -*- coding: utf-8 -*-
"""22101617-suchitra barua-lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRJ14DenwRFMlabZf0CATfHcpYDfsf9c
"""

import heapq

def read_input(file_input):
    f_in=open(file_input,'r')
    lines=f_in.readlines()

    heuristic_values ={}
    graph ={}

    for i in lines:
        parts = i.split()
        city,heuristic,*neighbors=parts
        heuristic_values[city]=int(heuristic)
        graph[city]={neighbors[i]:int(neighbors[i+1]) for i in range(0, len(neighbors),2)}

    return graph,heuristic_values

def a_star_search(graph, heuristic_values, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic_values[start], 0, start, [start]))
    visited = set()
    while open_list:
        priority, cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, cost
        if current in visited:
            continue
        visited.add(current)

        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                total_cost = cost + distance
                heapq.heappush(open_list, (total_cost + heuristic_values[neighbor], total_cost, neighbor, path + [neighbor]))

    return None

file_input = "/content/Input file.txt"
graph,heuristic_values=read_input(file_input)

start_node=input("Start node:: ")
goal_node=input("Destination node:: ")
result=a_star_search(graph, heuristic_values, start_node, goal_node)

if result:
    path, total_dist = result
    print(f"Path: {' -> '.join(path)}")
    print(f"Total Distance: {total_dist} km")
else:
    print("NO PATH FOUND")