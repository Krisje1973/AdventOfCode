import functools
from functools import cache
from collections import defaultdict,deque 
import sys
import re
from queue import PriorityQueue
from queue import Queue
import heapq
from math import inf
import numpy as np
from enum import Enum

def open_file(filename) :
    return open(filename).read()

def readinput_dict_as_ints(filename):    
    input = {}
    file = open(filename, "r")
    for line in file:
      input[int(line)] = int(line)
    return input

def readinput_dict_as_ints_with_separator(filename,separator):    
    input = {}
    file = open(filename, "r")
    for line in [x.split(separator) for x in file]:
        for val in line:
            input[int(val)] = int(val)
    return input

def readinput_lines_with_separator(filename,separator):   
    file = open(filename, "r")    
    input=[]
    for line in [line.split(separator) for line in file]:
        for val in line:
            input.append(val.strip()) 
    return input

def readinput_as_pairs(filename):
    return [[x for x in pair.splitlines()] for pair in open(filename).read().split("\n\n")]

def readinput_lines(filename):   
    file = open(filename, "r")    
    return [line.strip() for line in file]


def readinput_lines_no_strip(filename):   
    file = open(filename, "r")    
    return [line for line in file if line.strip() != '']

def readinput_lines_no_strip_no_enter(filename):   
    file = open(filename, "r")    
    return [line.replace("\n","") for line in file if line.strip() != '']

def readinput_as_string(filename):   
    file = open(filename, "r")    
    return ''.join(line for line in file)

def readinput_lines_skip_enters(filename):   
    file = open(filename, "r")    
    return [line.strip() for line in file if line.strip() != '']

def readinput_lines_as_int_list(filename):   
    file = open(filename, "r")    
    input=[]
    for line in [line.strip() for line in file]:
      input.append(list(map(int, line.split()))) 

    return input

def readinput_lines_as_str(filename):   
    file = open(filename, "r")    
    input=""
    for line in [line.strip() for line in file]:
        for s in line:
            input += s
    return input

def readinput_lines_as_ints_with_separator(filename,separator):   
    file = open(filename, "r")    
    input=[]
    for line in [line.split(separator) for line in file]:
        for val in line:
            input.append(int(val)) 
    return input
    
def removekeyfromdict(d, key):
   r = dict(d)
   if key in d.keys():
      del r[key]
   
   return r  

#Accepts string and shift it around
#ABC, 1=CAB, 2=BCA
def shift_string(s, shift):
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]


def char_position(letter):
    return ord(letter) - 97

def pos_to_char(pos):
    return chr(pos + 97)


""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1 = edge.pop()
        if edge:
            # not a loop
            vertex2 = edge.pop()
        else:
            # a loop
            vertex2 = vertex1
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def find_path(self, start_vertex, end_vertex, path=[]):
        """ find a path from start_vertex to end_vertex 
            in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None
    
    def yieldAllPathsUtil(self, u, d, visited, path):
     
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            yield path
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.yieldAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    if p not in paths:
                        paths.append(p)
        return paths

    def is_connected(self, 
                     vertices_encountered = None, 
                     start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = gdict.keys() 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices =  self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def is_degree_sequence(sequence):
        """ Method returns True, if the sequence "sequence" is a 
            degree sequence, i.e. a non-increasing sequence. 
            Otherwise False is returned.
        """
        # check if the sequence sequence is non-increasing:
        return all( x>=y for x, y in zip(sequence, sequence[1:]))
  

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def density(self):
        """ method to calculate the density of a graph """
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V *(V - 1))

    def diameter(self):
        """ calculates the diameter of the graph """
        
        v = self.vertices() 
        pairs = [ (v[i],v[j]) for i in range(len(v)-1) for j in range(i+1, len(v))]
        smallest_paths = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list, 
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1])
        return diameter

    @staticmethod
    def erdoes_gallai(dsequence):
        """ Checks if the condition of the Erdoes-Gallai inequality 
            is fullfilled 
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        if Graph.is_degree_sequence(dsequence):
            for k in range(1,len(dsequence) + 1):
                left = sum(dsequence[:k])
                right =  k * (k-1) + sum([min(x,k) for x in dsequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True
        
class Binary:
  def get_binary_as_string(self,val,length=0):
    bval = bin(int(val)).replace("0b","")  
    return "".ljust(length-len(bval), "0") + bval

  def get_binary_as_string_from_mask(self,val,mask,match):
    bval = self.get_binary_as_string(val,len(mask))
    binstr = ""
    for i in range(len(bval)):     
      if mask[i] == match:
          binstr+=bval[i]
      else:
          binstr+=mask[i]
    return binstr
  
  def split_binary_as_list(self,val,match):
    splitted = []
    matches = pow(2,val.count(match))
    for i in range(matches):
        splitted.append("")       
    for n in range(len(val)):       
        v=False  
        splitted.sort()                      
        for i in range(matches):  
            v = v == False                 
            if val[n] == match:
                splitted[i] += str(int(v))
            else:
                  splitted[i] += val[n] 
    return splitted

  def get_int_from_binary_string(self,s):
    return int(s,2)

  def get_int_from_binary_reversed_string(self,s):
    return int(s[::-1],2)



class FileHelper:
  
  def readinput_dict_as_ints(self,filename):    
      input = {}
      file = open(filename, "r")
      for line in file:
        input[int(line)] = int(line)
      return input

  def readinput_lines(self,filename):   
      file = open(filename, "r")    
      return [line.strip() for line in file]
  
  def readinput_lines_and_replace(self,filename,replaces):  
      #Usage :  input = file.readinput_lines_and_replace(r"Day17\input_ex.txt",[[".","0"],["#","1"]]) 
      file = open(filename, "r")    
      lines = []
      for line in [line.strip() for line in file]:
        for replace in replaces:
          line = line.replace(replace[0],replace[1])
        lines.append(line)

      return lines

  def readinput_lines_as_list_ints(self,filename):   
      file = open(filename, "r")    
      input=[]
      for line in [line.strip() for line in file]:
          for i in line:
            input.append(int(i)) 
      return input
  
  def readinput_lines_as_ints(self,filename):   
      file = open(filename, "r")    
      input=[]
      for line in [line.strip() for line in file]:
        input.append(int(line)) 
      return input

  def get_arrays_from_separator(self,lines,separator):
    # Reads all lines and creates array for each seperator found (mostly blanc line)
    arrays = []    
    lineid = 0
   
    while lineid < len(lines):
        arr = []
        while lineid < len(lines) and lines[lineid]:
            if lines[lineid]==separator: break
            arr.append(lines[lineid].strip())
            lineid += 1
        lineid += 1
        arrays.append(arr)

    return arrays

  def get_arrays_ints_from_separator(self,lines,separator):
    # Reads all lines and creates array for each seperator found (mostly blanc line)
    arrays = []    
    lineid = 0
   
    while lineid < len(lines):
        arr = []
        while lineid < len(lines) and lines[lineid]:
            if lines[lineid]==separator: break
            arr.append(int(lines[lineid].strip()))
            lineid += 1
        lineid += 1
        arrays.append(arr)

    return arrays

class Compass:
    compasspoints = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)} # Can be used for north/south, east/west calculation
    compasspoints_reversed = {'N': (0, 1), 'E': (-1, 0), 'S': (0, -1), 'W': (1, 0)} 
    hexaspoints = {"N": (0,-1), "E": (1, 0), "W": (-1, 0), "S": (0,1),  "SE": (1, 1), "SW": (-1, 1), "NE": (1, -1), "NW": (-1, -1)}
    hexaspoints_reversed = {"N": (0,1), "E": (-1, 0), "W": (1, 0), "S": (0,-1),  "SE": (-1, -1), "SW": (1, -1), "NE": (-1, 1), "NW": (1, 1)}
    
    def getHexasPoints(self,dir,reversed=False):
        if reversed:
            points = self.hexaspoints_reversed
        else:
            points=self.hexaspoints

        match dir:
            case "N":
                return points["N"],points["NW"],points["NE"]
            case "E":
                return points["E"],points["NE"],points["SE"]
            case "S":
                return points["S"],points["SE"],points["SW"]
            case "W":
                return points["W"],points["NW"],points["SW"]

    def turnCompassPoint(self,currentdirection,turndirection,degrees):     
        degrees = (degrees // 90)   
        if turndirection == "L":
            degrees=-degrees
        dirs = list(self.compasspoints.keys())
        idx = dirs.index(currentdirection) + degrees
        idx %= len(dirs)
        return (dirs[idx:] + dirs[:idx])[0]     

class NeighbourghType(Enum):
        INCLUDEDIAGONALS = 1
        EXCLUDEDIAGONALS = 2
        ONLYDIAGIONALS = 3

class TupleHelper():
    def add_tuples(self,tuple1,tuple2):
        return tuple(sum(tup) for tup in zip(tuple1,  tuple2))
        
    def get_neighbours4(self,tuple):
        x,y = tuple
        for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            yield (nx, ny)

    def get_neighbours_array(self,tuple):
        x,y = tuple
        return [(y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)]


    def get_neighbours(self,start, offset, grid_limits, neighbourtype:NeighbourghType = NeighbourghType.EXCLUDEDIAGONALS,excludestart=False):
       
        # th.get_neighbours((x,y),3,(len(row),len(input)),NeighbourghType.INCLUDEDIAGONALS) 
        x, y = start
        max_row, max_col = grid_limits
        directions = [] 

        if not neighbourtype == neighbourtype.ONLYDIAGIONALS:
            directions = [
                (1, 0),   # Rechts
                (-1, 0),  # Links
                (0, 1),   # Boven
                (0, -1),  # Onder
            ]
        if neighbourtype == NeighbourghType.INCLUDEDIAGONALS or neighbourtype == NeighbourghType.ONLYDIAGIONALS:
            directions = [*directions,*
            [
                (1, -1),  # Diagonaal rechtsonder
                (-1, 1),  # Diagonaal linksboven
                (-1, -1), # Diagonaal linksonder
                (1, 1)    # Diagonaal rechtsboven
            ]]

        results = []
        for dx, dy in directions:
            path = []
            for i in range(offset + 1):
                new_x = x + i * dx
                new_y = y + i * dy
                if 0 <= new_x < max_row and 0 <= new_y < max_col:
                    path.append((new_x, new_y))
                else:
                    break 

            results = [*results,*path[excludestart:]]

        return set(results)


    def get_neighbours_with_bounderies(self,tuple,bound,allowunderzero=False):
        r,c = tuple
        maxr,maxc = bound
        res = []
        for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if not allowunderzero and 0 <= nr <= maxr and 0<= nc <= maxc: 
                res.append((nr,nc))
            if allowunderzero and nr <= maxr and nc <= maxc: 
                res.append((nr,nc))
        return res
    
    def get_neighbours_with_diag(self,tuple):
        x,y = tuple
        for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x-1,y-1), (x+1,y+1),(x-1,y+1), (x+1,y-1):
            yield (nx, ny)
            
def add_tuples(tup1,tup2):
    return tuple(sum(tup) for tup in zip(tup1,  tup2))

class GridHelper:
  def get_adjacent(self,input):
    maxx = len(str(input[0]))
    maxy = len(input)
    for line in input:  
        for y,x in enumerate(line):
            x= int(x)
            y=int(y)
            xy = defaultdict(list)
            for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= nx < maxy and 0 <= ny < maxx:
                    xy[(x,y)] += [(nx,ny), input[nx][ny]]
            if len(xy) > 0: yield xy

  def get_adjacent_pos_with_diag(self,x, y,maxx,maxy):
    adj = []
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) , (x-1,y-1), (x+1,y+1),(x-1,y+1), (x+1,y-1):
        if 0 <= nx < maxy and 0 <= ny < maxx:
           adj.append((nx, ny))
    return adj
    
  def get_adjacent_pos(self,x, y,maxx,maxy):
     for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < maxy and 0 <= ny < maxx:
            yield (nx, ny)


  def get_suroundings(self,grid,x,y,count):
    start =-1
    end = count -1 + start
    # Gets a new grid with offset
    return [grid[y + dy][x + dx] 
    
    for dx in range(start, end) 
    for dy in range(start, end) 
    if 0 <= y + dy < len(grid) # Check y bounds
    and 0 <= x + dx < len(grid[x]) # check x bounds
    and (dx, dy) != (0, 0)]  # not self

  def get_3d_suroundings(self,x,y,z):
    sur = [(0, 0, 1),(0, 1, 0),(1, 0, 0),(0, 0, -1),(0, -1, 0),(-1, 0, 0)]
    for side in sur:
        yield tuple(sum(tup) for tup in zip((x,y,z), side))
 
  def join_lines_from_list(self,mylist): 
      return "\n".join("".join(row) for row in mylist)


  def calculate_combinations(self,data,offset):

    dist = [1]
    data.sort()
    for val in range(1, len(data)):
          total = 0
          for tot in range(val):
              if data[tot] + offset >= data[val]:
                  total += dist[tot]
          dist.append(total)  
          
    return dist
  
  def get_int_combinations(self,data,offsets):
    # =============================================================
    # Data is list of int's.
    # Each val in list needs to connect within the offset parameter
    # =============================================================

    combis = {}
    combi_vals = {}
    data.sort()
    for offset in offsets:
      combi = []
      combi_val = []  
      start = 0
      for val in data:
        if val - start == offset:
          combi.append(1) 
          combi_val.append(val)  
        start = val
      
      combis[offset] = combi
      combi_vals[offset] = combi_val      
         
    return combis,combi_vals

class ChineseReminder():
  def calculate_chinese_remainder(self,rem, mod):
    #
    # Solves and finds X for a system of congruences:
    #   X = a_1 (mod n_1)
    #   X = a_2 (mod n_2)
    #   ...
    #   X = a_N (mod n_N)
    #
    # Solutions afterwards can be made by adding/subtracting by MOD
    # Returns X (the initial value), and MOD (the interval where it repeats)
    #
    # Additional Info: https://brilliant.org/wiki/chinese-remainder-theorem/

    a1 = rem[0]
    m1 = mod[0]
    for a2, m2 in zip(rem[1:], mod[1:]):
        gcd, x, y = self.extended_gcd(m1, m2)
        if a1 % gcd != a2 % gcd:
            raise ValueError("No solutions for given input.")
        _, x, y = self.extended_gcd(m1 // gcd, m2 // gcd)
        MOD = m1 // gcd * m2
        X = (a1 * (m2 // gcd) * y + a2 * (m1 // gcd) * x) % MOD
        a1 = X
        m1 = MOD
    return a1, MOD
    
  def extended_gcd(self,a, b):
      x, y, u, v = 0, 1, 1, 0
      while a != 0:
          q, r = b // a, b % a
          m, n = x - u * q, y - v * q
          b, a, x, y, u, v = a, r, u, v, m, n
      gcd = b
      return gcd, x, y  # x, y are for [ax + by = gcd]

class RegexHelper():
    def extract_digits(self,line):
        return list(map(int,re.findall(r'\d',line)))
    
    def extract_numerics(self,line):
        return list(map(int, re.findall(r"-?\d+", line)))
    
    def extract_numerics_from_list(self,lines):
        for line in lines:
            yield list(map(int, re.findall(r"-?\d+", line)))[0]

    def extract_numerics_from_list_as_List(self,lines):
        for line in lines:
            yield list(map(int, re.findall(r"-?\d+", line)))
        
    def is_string_numeric_regex(self,s):
        return re.search('^[-+]?[0-9]+$',s)

    def is_list_numeric_regex(self,l):
        for s in l:
            if not re.search('^[0-9]+$',s):
                return False

        return True
    
    def has_string_numeric_regex(self, s):
        for i in s:
            if re.search('^[0-9]+$',i):
                return True

        return False

    def has_list_numeric_regex(self,l):
        for s in l:
            if re.search('^[0-9]+$',s):
                return True
            
        return False

class IndexedReader():
    def __init__(self,input:str,start:int=0):
      self.input = input
      self.index = start
      self.positions = defaultdict(int)

    def read(self,chars:int) ->str:
        self.index+=chars
        return self.input[self.index-chars:self.index]
    def eof(self)->bool:
        return self.index>=len(self.input)-1
    def getindex(self):
        return self.index
    def addpointer(self,key,index=None):
        self.positions[key] = index if index != None else self.index
    def delpointer(self,key):
        del self.positions[key]
    def getpointer(self,key):
        return self.positions[key]

def bfs(Adj, s):  # Adj: adjacency list, s: starting vertex
    parent = [None for v in Adj]  # O(V) (use hash if unlabeled)
    parent[s] = s  # O(1) root
    dist = [None for v in Adj]
    dist[s] = 0
    levels = [[s]]  # O(1) initialize levels
    while levels[-1]:  # O(?) last level contains vertices
        frontier = []  # O(1), make new level
        for u in levels[-1]:  # O(?) loop over last full level
            for v in Adj[u]:  # O(Adj[u]) loop over neighbors
                if parent[v] is None:  # O(1) parent not yet assigned
                    parent[v] = u  # O(1) assign parent from levels[-1]
                    dist[v] = dist[u] + 1
                    frontier.append(v)  # O(1) amortized, add to border
        levels.append(frontier)  # add the new level to levels
    return parent, dist    

def dijkstra(adj, start, target):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited: continue
        if u == target:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))


    return parent, d

def dfs(visited, graph, node):  #function for dfs 
    #  graph = {
    #     '5' : ['3','7'],
    #     '3' : ['2', '4'],
    #     '7' : ['8'],
    #     '2' : [],
    #     '4' : ['8'],
    #     '8' : []
    # }
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def dfs_order(adj, v, parent, order):
    if not parent:
        parent[v] = None
    # checking neighbours of v
    for n in adj[v]:
        if n not in parent:
            parent[n] = v
            dfs(adj, n, parent, order)

    # we're done visiting a node only when we're done visiting
    # all of its descendents first
    order.append(v)


def topological_sort(adj):
    parent = {}
    order = []
    for v in adj.keys():
        if v not in parent:
            parent[v] = None
            dfs(adj, v, parent, order)

    return list(reversed(order))

def dag_shortest_path(adj, source, dest):
    order = topological_sort(adj)
    parent = {source: None}
    d = {source: 0}

    for u in order:
        if u not in d: continue  # get to the source node
        if u == dest: break
        for v, weight in adj[u]:
            if v not in d or d[v] > d[u] + weight:
                d[v] = d[u] + weight
                parent[v] = u

    return parent, d

class BfsGraph:
     
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True  
                    
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

class Cart:
    def __init__(self, x, y, direction,grid=[]):
        self.x = x
        self.y = y
        self.grid = grid
        self.directions = deque("^>v<")
        self.movements = {"^":(0,-1),"v":(0,1),"<":(-1,0),">":(1,0)}
        self.direction = direction
        self.current_direction = self.set_direction(direction)
        self.intersection_count = 0
        self.visited = set()
       
    def set_direction(self,direction):  
        while self.directions[0] != direction:
            self.directions.rotate(1)
        return self.directions
    
    def move(self):
        x,y = self.movements[self.direction]
        self.x += x
        self.y += y

    def move_if_valid(self):
        x,y = self.movements[self.direction]
        self.x += x
        self.y += y
        valid = not (self.x < 0 or self.x > len(self.grid[0]) -1 or self.y < 0 or self.y > len(self.grid) -1)
        return valid

    def turn(self,track_char=""):
        if track_char == "": 
            track_char = self.get_char()
        if track_char == "/":
            direction = { "^":">","v":"<","<":"v",">":"^"}
            self.direction = self.set_direction(direction[self.direction])[0]
        if track_char == "\\":
            direction = { "^":"<","v":">","<":"^",">":"v"}
            self.direction = self.set_direction(direction[self.direction])[0]
        if track_char == "+":
            self.turn_intersection()

        if track_char == "-":
            if self.direction in "^v":
                return (Cart(self.x + 1 ,self.y,">",self.grid),Cart(self.x-1,self.y,"<",self.grid))
        if track_char == "|":
            if self.direction in "<>":
                return (Cart(self.x,self.y - 1,"^",self.grid),Cart(self.x,self.y + 1,"v",self.grid))

    def turn_intersection(self):
        self.set_direction(self.direction)
        
        if self.intersection_count % 3 == 0:
            self.current_direction.rotate(1)
            
        elif self.intersection_count % 3 == 1:  
            pass  # Go straight
        elif self.intersection_count % 3 == 2:
            self.current_direction.rotate(-1)
        
        self.direction = self.current_direction[0]
        self.intersection_count += 1

    def get_char(self):
        if len(self.grid) == 0: 
            return None
        if not self.x < 0 and not self.x > len(self.grid[0]) and not self.y < 0 and not self.y > len(self.grid) :
            return self.grid[self.y][self.x]

        return None
# Extract all numbers by text annotation as list of tuples
# Tuple pos 1 = position in text, pos 2 = found number 
# Can be sorted with min and max functions
def findStringNumbers(s,sort=False) -> list:
    results = []
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    for i,num in enumerate(numbers):
        p=0
        s2=s
        while s2.find(num)>-1:
            p+=s2.index(num)
            results.append((p,i+1))
            p+=1
            s2 = s[p::]
    if sort:
        return results.sort()
    
    return results 

def findNumbersInString(s,sort=False) -> list:
    results = []
    for i,num in enumerate(s):
        if(num.isdigit()):
            results.append((i,int(num)))

    if sort:
        return results.sort()
    
    return results 

def getFirstAndLastNumberFromString(s):
    return next(c for c in s if c.isdigit()), next(c for c in s[::-1] if c.isdigit())

# retrieve digits from string --> 1,2,3 ...  
def getDigitsFromString(s):
    return list(map(int,re.findall(r'\d',s)))

# retrieve numbers from string --> 1,25,367 ...
def getNumbersFromString(s):
    return list(map(int,re.findall(r'-?\d+\.?\d*',s)))

# Get replacements for char in string
# Return array with all replaced char string
# ex: s="ABCB",replacements "DEF",charToReplace "B"
# returns ['ADCD', 'ADCE', 'ADCF', 'AECD', 'AECE', 'AECF', 'AFCD', 'AFCE', 'AFCF']
def getReplacements(s,replacements,charToReplace):
    if s == "":
        return [""]

    return [
        x + y
        for x in (replacements if s[0] == charToReplace else s[0])
        for y in getReplacements(s[1:],replacements,charToReplace)
    ]

def isbetween(value: int, low: int, high: int) -> bool:
    if low > high: low, high = high, low
    return low < value < high   

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return r
        
    return 0


def find_mirror2(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

def shoelace_outsides(xs,ys,n_outsides):
    # Gets the full area filled 
    assert len(xs) == len(ys)
    if n_outsides:
        n_outsides = n_outsides // 2 + 1 
    intern = abs(sum((ys[i] + ys[i+1]) * (xs[i] - xs[i+1]) for i in range(len(xs)-1))) // 2
    return intern + n_outsides

def shoelace(xs,ys):
    assert len(xs) == len(ys)   
    result = 0
    for i in range(len(xs)-1):
        result += xs[i] * ys[i+1] - ys[i] * xs[i+1]
        
    return abs((result + xs[len(xs)-1] * ys[0]- ys[len(ys)-1] * xs[0]) // 2)

def find_char_in_grid(grid,char):
    return [(c,r) for r,row in enumerate(grid) for c, ch in enumerate(row) if ch==char]