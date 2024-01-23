import networkx as nx 
import matplotlib.pyplot as plt 

# Create the dictionary with graph elements
graph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())
    
    def getEdges(self):
        edges = []
        for vrtx in self.gdict:
            for nstVrtx in self.gdict[vrtx]:
                if [vrtx, nstVrtx ] not in edges:
                    edges.append([ vrtx, nstVrtx])
        return edges
    
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 
    
print(Graph(graph).getEdges())