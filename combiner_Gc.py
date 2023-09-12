import itertools
import random
import numpy as np
import sys
import getopt

def foursquare_like_graph(gr_file, co_file, mean, standard_dev, nodes_to_combine):

    #read graph nodes from the GR file
    with open(gr_file, 'r', encoding="utf-8") as gr:
        lines = gr.readlines()[1:]
        graph_edges = [line.strip() for line in lines]

    graph_nodes = []
    for edge in graph_edges:
        edge = edge.split(" ")
        if int(edge[0]) not in graph_nodes:
            graph_nodes.append(int(edge[0]))
        if int(edge[1]) not in graph_nodes:
            graph_nodes.append(int(edge[1]))

    #read spatial coordinates from the CO file
    spatial_coordinates = {}
    with open(co_file, 'r', encoding="utf-8") as co:
        metadata = co.readline().strip().split()
        num_coordinates = int(metadata[1])
        for line_number, line in enumerate(co, start=1):
            if line_number > 0:
                if num_coordinates == 2:
                    _, x, y = line.strip().split()
                    spatial_coordinates[line_number - 1] = (float(x), float(y))
                else:
                    _, x_low, y_low, x_high, y_high = line.strip().split()
                    spatial_coordinates[line_number - 1] = (float(x_low), float(y_low), float(x_high), float(y_high))

    selected_nodes = {}
    spatial_edges = []
    selected_spatial_nodes = []
    number_spatial_nodes = len(spatial_coordinates)

    if number_spatial_nodes < nodes_to_combine:
        for i in range(nodes_to_combine - number_spatial_nodes):
            spatial_coordinates[number_spatial_nodes + i] = spatial_coordinates[
                random.randint(0, number_spatial_nodes - 1)]
    else:
        spatial_coordinates = dict(itertools.islice(spatial_coordinates.items(), nodes_to_combine))

    #id for the new spatial nodes
    sNode_id = len(graph_nodes)

    for spatial_node, coordinates in spatial_coordinates.items():
        #number of graph nodes for the selected spatial node
        num_graph_nodes = np.random.normal(mean, standard_dev)
        num_graph_nodes = max(1, int(round(num_graph_nodes)))
        num_graph_nodes = min(num_graph_nodes, len(graph_nodes))

        graph_node_keys = random.sample(graph_nodes, num_graph_nodes)

        #connect the selected graph node with the spatial coordinates
        selected_nodes[coordinates] = graph_node_keys

        #create new edges between the graph nodes and the spatial node
        selected_spatial_nodes.append((sNode_id, coordinates))
        spatial_edges.extend([(graph_node, sNode_id) for graph_node in graph_node_keys])

        sNode_id += 1

    num_nodes = len(graph_nodes) + len(selected_spatial_nodes)
    num_edges = len(graph_edges) + len(spatial_edges)

    with open('spatial_output_foursquare.co', 'w', encoding="utf-8") as output_file:
        output_file.write(f"{len(selected_spatial_nodes)} {num_coordinates}\n")
        for spatial_node, coordinates in selected_spatial_nodes:
            output_file.write(f"{spatial_node} {' '.join(str(coord) for coord in coordinates)}\n")

    with open(gr_file, 'r', encoding="utf-8") as gr:
        lines = gr.readlines()[1:]
        with open('graph_output_foursquare.gr', 'w', encoding="utf-8") as output_file:
            output_file.write(f"{num_nodes} {num_edges}\n")
            for line in lines:
                gNode1, gNode2 = line.strip().split()
                output_file.write(f"{gNode1} {gNode2}\n")
            for graph_node, spatial_node in spatial_edges:
                output_file.write(f"{graph_node} {spatial_node}\n")

    return selected_nodes


def main(argv):
    gr_file = ''
    co_file = ''
    mean = 0
    standard_dev = 0
    nodes_to_combine = 0

    try:
        opts, args = getopt.getopt(argv, "hg:c:m:s:n:", ["grfile=", "cofile=", "mean=", "stddev=", "nodes="])
    except getopt.GetoptError:
        print("Usage: script.py -g <grfile> -c <cofile> -m <mean> -s <stddev> -n <nodes_to_combine>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("Usage: script.py -g <grfile> -c <cofile> -m <mean> -s <stddev> -n <nodes_to_combine>")
            sys.exit()
        elif opt in ("-g", "--grfile"):
            gr_file = arg
        elif opt in ("-c", "--cofile"):
            co_file = arg
        elif opt in ("-m", "--mean"):
            mean = float(arg)
        elif opt in ("-s", "--stddev"):
            standard_dev = float(arg)
        elif opt in ("-n", "--nodes_to_combine"):
            nodes_to_combine = int(arg)

    foursquare_like_graph(gr_file, co_file, mean, standard_dev, nodes_to_combine)

if __name__ == "__main__":
    main(sys.argv[1:])
