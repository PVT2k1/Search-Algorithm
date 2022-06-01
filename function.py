from turtle import pos
from matplotlib.pyplot import close
import numpy as np

def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:
    path=[]
    visited={}
    Open = []   #danh sách các đỉnh đã mở
    Open.append(start)
    beforeNode = [] #danh sách các đỉnh trước đó, mục đích đưa vào visited để truy vết ngược lại
    beforeNode.append(-1)
    Closed=[]   #danh sách các đỉnh đã ghé thăm

    while True:
        if len(Open)==0:
            print("failed!")    #Không có đường đi từ start --> end
            return None,None
        
        currentNode=Open.pop(0)
        visited[currentNode]=beforeNode.pop(0)
        Closed.append(currentNode)

        #Nếu đã đến đích
        if currentNode==end:
            #truy vết lộ trình đi từ start --> end
            i=0
            path.append(end)
            while path[i]!=start:
                i+=1
                path.append(visited[path[i-1]])

            #đảo path lại
            for i in range(int(len(path)/2)):
                path[i],path[len(path)-1-i]=path[len(path)-1-i],path[i]
            return path, visited
        
        #Chưa đến đích
        pos=0
        for i in range(len(matrix[0])):
            if matrix[currentNode][i]==1:
                if i not in Open and i not in Closed:
                    Open.insert(pos,i)
                    beforeNode.insert(pos,currentNode)
                    pos+=1

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:
    path=[]
    visited={}
    Open = []   #danh sách các đỉnh đã mở
    Open.append(start)
    beforeNode = [] #danh sách các đỉnh trước đó, mục đích đưa vào visited để truy vết ngược lại
    beforeNode.append(-1)
    Closed=[]   #danh sách các đỉnh đã ghé thăm

    while True:
        if len(Open)==0:
            print("failed!")    #Không có đường đi từ start --> end
            return None,None
        
        currentNode=Open.pop(0)
        visited[currentNode]=beforeNode.pop(0)
        Closed.append(currentNode)

        #Nếu đã đến đích
        if currentNode==end:
            #truy vết lộ trình đi từ start --> end
            i=0
            path.append(end)
            while path[i]!=start:
                i+=1
                path.append(visited[path[i-1]])

            #đảo path lại
            for i in range(int(len(path)/2)):
                path[i],path[len(path)-1-i]=path[len(path)-1-i],path[i]
            return path, visited

       #Chưa đến đích
        for i in range(len(matrix[0])):
            if matrix[currentNode][i]==1:
                if i not in Open and i not in Closed:
                    Open.append(i)
                    beforeNode.append(currentNode)

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:
    path=[]
    visited={}
    openAndCost = []   #danh sách các đỉnh đã mở, và chi phí nhỏ nhất để đi đến các đỉnh đó từ start
    openAndCost.append([start,0])
    beforeNode = [] #danh sách các đỉnh trước đó, mục đích đưa vào visited để truy vết ngược lại
    beforeNode.append(-1)
    closed=[]   #danh sách các đỉnh đã ghé thăm

    while True:
        if len(openAndCost)==0:
            print("failed!")    #Không có đường đi từ start --> end
            return None,None
        
        currentNodeAndCost=openAndCost.pop(0)   #lưu node (đỉnh) đang xét hiện tại và chi phí đi đến đó từ start
        visited[currentNodeAndCost[0]]=beforeNode.pop(0)
        closed.append(currentNodeAndCost[0])

        #Nếu đã đến đích
        if currentNodeAndCost[0]==end:
            #truy vết lộ trình đi từ start --> end
            i=0
            path.append(end)
            while path[i]!=start:
                i+=1
                path.append(visited[path[i-1]])

            #đảo path lại
            for i in range(int(len(path)/2)):
                path[i],path[len(path)-1-i]=path[len(path)-1-i],path[i]
            return path, visited
        
        #Chưa đến đích
        for i in range(len(matrix[0])):
            if matrix[currentNodeAndCost[0]][i]!=0:
                if i not in openAndCost and i not in closed:
                    openAndCost.append([i,matrix[currentNodeAndCost[0]][i]+ currentNodeAndCost[1]])
                    beforeNode.append(currentNodeAndCost[0])

                    #sắp xếp lại theo thứ tự tăng dần trong danh sách đỉnh mở và chi phí (openAndCost)
                    for i in range(len(openAndCost)-1):
                        for j in range(i+1,len(openAndCost)):
                            if openAndCost[i][1]>openAndCost[j][1]:
                                openAndCost[i],openAndCost[j]=openAndCost[j],openAndCost[i]
                                beforeNode[i],beforeNode[j]=beforeNode[j],beforeNode[i]

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:
    path=[]
    visited={}
    openAndEdgeWeight= []   #danh sách các đỉnh đã mở và chi phí đi từ đỉnh liền trước đi đến đỉnh đó
    openAndEdgeWeight.append([start,0])
    beforeNode = [] #danh sách các đỉnh trước đó, mục đích đưa vào visited để truy vết ngược lại
    beforeNode.append(-1)
    closed=[]   #danh sách các đỉnh đã ghé thăm

    while True:
        if len(openAndEdgeWeight)==0:
            print("failed!")    #Không có đường đi từ start --> end
            return None,None
        
        currentNodeAndEdgeWeight=openAndEdgeWeight.pop(0)   #lưu node (đỉnh) đang xét hiện tại và chi phí đi từ đỉnh liền trước đi đến đỉnh đó
        visited[currentNodeAndEdgeWeight[0]]=beforeNode.pop(0)
        closed.append(currentNodeAndEdgeWeight[0])

        #Nếu đã đến đích
        if currentNodeAndEdgeWeight[0]==end:
            #truy vết lộ trình đi từ start --> end
            i=0
            path.append(end)
            while path[i]!=start:
                i+=1
                path.append(visited[path[i-1]])

            #đảo path lại
            for i in range(int(len(path)/2)):
                path[i],path[len(path)-1-i]=path[len(path)-1-i],path[i]
            return path, visited
        
        #Chưa đến đích
        for i in range(len(matrix[0])):
            if matrix[currentNodeAndEdgeWeight[0]][i]!=0:
                if i not in openAndEdgeWeight and i not in closed:
                    openAndEdgeWeight.append([i,matrix[currentNodeAndEdgeWeight[0]][i]])
                    beforeNode.append(currentNodeAndEdgeWeight[0])

                    #sắp xếp lại theo thứ tự tăng dần trong danh sách đỉnh mở và chi phí (openAndEdgeWeight)
                    for i in range(len(openAndEdgeWeight)-1):
                        for j in range(i+1,len(openAndEdgeWeight)):
                            if openAndEdgeWeight[i][1]>openAndEdgeWeight[j][1]:
                                openAndEdgeWeight[i],openAndEdgeWeight[j]=openAndEdgeWeight[j],openAndEdgeWeight[i]
                                beforeNode[i],beforeNode[j]=beforeNode[j],beforeNode[i]

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path