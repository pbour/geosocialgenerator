import networkx as nx

class GraphGenerator:
    def __init__(self):
        self.graph = None


    def graph_to_file(self, filename, directed = False):
        with open(filename, 'w') as file:
            file.write(f'{self.number_of_nodes()} '
                       f'{self.number_of_edges()}\n')
            for edge in self.edges():
                if directed:
                    file.write(f'{edge[0]} {edge[1]}\n')
                else:
                    file.write(f'{edge[0]} {edge[1]}\n')
                    file.write(f'{edge[1]} {edge[0]}\n')


    # Barabasi Scale Free Model
    def barabasi_graph(self, n, m):
        self.graph = nx.Graph(nx.barabasi_albert_graph(n, m))
        GraphGenerator.graph_to_file(self.graph, 'graph.gr')
        return "graph.gr"


    # Scale Free Graph Model (Undirected)
    def scale_free_graph(self, n, a, b, g, dIn, dOut):
        self.graph = nx.Graph(nx.scale_free_graph(n, a, b, g, dIn, dOut))
        # remove any self loop in the graph
        self.graph.remove_edges_from(nx.selfloop_edges(self.graph))
        GraphGenerator.graph_to_file(self.graph, 'graph.gr')
        return "graph.gr"


    # Scale Free Graph Model (Directed)
    def scale_free_digraph(self, n, a, b, g, dIn, dOut):
        self.graph = nx.DiGraph(nx.scale_free_graph(n, a, b, g, dIn, dOut))
        # remove any self loop in the graph
        self.graph.remove_edges_from(nx.selfloop_edges(self.graph))
        GraphGenerator.graph_to_file(self.graph, 'graph.gr', directed = True)
        return "graph.gr"


    # Holme and Kim algorithm (Power Cluster Graph)
    def power_graph(self, n, m, p):
        self.graph = nx.Graph(nx.powerlaw_cluster_graph(n, m, p))
        GraphGenerator.graph_to_file(self.graph, 'graph.gr')
        return "graph.gr"
