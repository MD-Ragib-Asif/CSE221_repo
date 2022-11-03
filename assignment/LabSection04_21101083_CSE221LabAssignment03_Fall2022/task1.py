# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:18:13 2022

@author: Rubayat Khan
"""
# CSE221 Lab 03 Graphs

def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("graph.txt", "r")
    
    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    #1 print(n.strip())
    n = n.strip() # number of nodes/vertices
    #2 print(type(n))
    # n is of type string. we need to convert it to int
    n=int(n)
    #3 print(type(n))
    
    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    #4 print(c)
    
    buildGraphUsingDictionary(c,f)
    
    buildGraphUsingListofLists(c,f)



# we want to build an adjacency list like the following
# A -> B,C 
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}

def buildGraphUsingDictionary(c,f): 
    # creating a dictionary
    graph = {}
    # the following lines of the file contain the connections
    # creating a directed graph (a,b means a is connected to b)
    
    counter = 0
    while (counter<c):
        line = f.readline() # reading each libe
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        
        # we first search if the value inside variable a exists in the dictionary or not
        if(a in graph):
            # if yes, then append() the value in b to a
            graph[a].append(b)
        else:
            # create a new list in graph with a as the key and b as the value
            graph[a] = [b]
        #5 print(a)
        #6 print(b)
        counter+=1    
    
    #7 print(graph)
    printGraph(graph, None)
       
    
# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
 # 1 -> 2,4
 # 2 -> 4
 # 3 -> 1,4
 # 4 -> 2
# notice this method takes both the graphs and lists as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph,listGraph):  
    # Your code
    if graph == None:
        with open('outputList.txt', 'w') as file_out_list:
            for i in range(len(listGraph)):
                string = ""
                if len(listGraph[i]) == 0:
                    pass
                else:
                    for j in range(len(listGraph[i])-1):
                        string = string + str(listGraph[i][j]) + ','
                    string = string + str(listGraph[i][-1])
                    # print(string)
                    file_out_list.write(f'{i+1} -> {string} \n')
                    
    else:
        with open('outputGraph.txt', 'w') as file_out_graph:
            for k,v in graph.items():
                string = ""
                for i in range(len(v)-1):
                    string = string + v[i] + ','
                string = string + v[-1]
                file_out_graph.write(f'{k} -> {string} \n')

    # return # delete this line

# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c,f):
    listGraph = [] # do not change the name of the variable\
    f.seek(0,0)
    lst = f.read().split('\n')
    listGraph = [listGraph] * int(lst[0].strip())
    lst2 = lst[2:]
    for i in range(c):
        llst = [int(x) for x in lst2[i].strip().split(',')]
        if listGraph[llst[0]-1] == []:
            listGraph[llst[0]-1] = [llst[1]]
        else:
            listGraph[llst[0]-1] += [llst[1]]

    #print(listGraph)

    # your code
    
    printGraph(None,listGraph)
    # return # delete this line
# ======================Program starts here.========================

# read file using the readFile() method
readFile()