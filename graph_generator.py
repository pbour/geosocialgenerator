import sys
import getopt
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

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:n:m:a:b:g:d:i:o:p:", ["help", "type=", "nodes=", "edges=", "alpha=", "beta=", "gamma=", "delta_in=", "delta_out=", "p="])
    except getopt.GetoptError:
        print("graph_generator.py -t <type> [other options]")
        sys.exit(2)

    graph_type = None
    n = None
    m = None
    a = None
    b = None
    g = None
    dIn = None
    dOut = None
    p = None

    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            print("graph_generator.py -t <type> [other options]")
            sys.exit()
        elif opt == "-t" or opt == "--type":
            graph_type = arg
        elif opt == "-n" or opt == "--nodes":
            n = int(arg)
        elif opt == "-m" or opt == "--edges":
            m = int(arg)
        elif opt == "-a" or opt == "--alpha":
            a = float(arg)
        elif opt == "-b" or opt == "--beta":
            b = float(arg)
        elif opt == "-g" or opt == "--gamma":
            g = float(arg)
        elif opt == "-d" or opt == "--delta_in":
            dIn = float(arg)
        elif opt == "-o" or opt == "--delta_out":
            dOut = float(arg)
        elif opt == "-p":
            p = float(arg)

    if graph_type is None:
        print("You must specify a graph type using -t or --type.")
        sys.exit(2)

    generator = GraphGenerator()

    if graph_type == "barabasi":
        if n is None or m is None:
            print("For Barabasi-Albert, you must specify the number of nodes (-n) and edges (-m).")
            sys.exit(2)
        generator.barabasi_graph(n, m)
    elif graph_type == "scale_free":
        if n is None or a is None or b is None or g is None or dIn is None or dOut is None:
            print("For Scale-Free (Undirected), you must specify -n, -a, -b, -g, -d, and -o.")
            sys.exit(2)
        generator.scale_free_graph(n, a, b, g, dIn, dOut)
    elif graph_type == "scale_free_digraph":
        if n is None or a is None or b is None or g is None or dIn is None or dOut is None:
            print("For Scale-Free (Directed), you must specify -n, -a, -b, -g, -d, and -o.")
            sys.exit(2)
        generator.scale_free_digraph(n, a, b, g, dIn, dOut)
    elif graph_type == "power":
        if n is None or m is None or p is None:
            print("For Power Cluster Graph, you must specify -n, -m, and -p.")
            sys.exit(2)
        generator.power_graph(n, m, p)
    else:
        print("Invalid graph type. Supported types: barabasi, scale_free, scale_free_digraph, power.")
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
