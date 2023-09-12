import random
import sys
import getopt

def spatial_graph(gr_file, co_file, percentage):
    #read graph nodes from the GR file
    with open(gr_file, 'r', encoding="utf-8") as graph:
        lines = graph.readlines()[1:]
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
        for line_number, line in enumerate(co, start = 1):
            if line_number > 0:
                if num_coordinates == 2:
                    _, x, y = line.strip().split()
                    spatial_coordinates[line_number - 1] = (float(x), float(y))
                else:
                    _, x_low, y_low, x_high, y_high = line.strip().split()
                    spatial_coordinates[line_number - 1] = (float(x_low), float(y_low), float(x_high), float(y_high))

    total_nodes = len(graph_nodes)
    nodes_to_combine = int(total_nodes * percentage)
    number_spatial_nodes = len(spatial_coordinates)

    if number_spatial_nodes < nodes_to_combine:
        for i in range(nodes_to_combine - number_spatial_nodes):
            spatial_coordinates[number_spatial_nodes + i ] = spatial_coordinates[
                random.randint(0, number_spatial_nodes - 1)]


    #selected graph and spatial nodes
    selected_nodes = []

    #shuffle and choose a random spatial node from the spatial nodes
    random.shuffle(graph_nodes)
    keys =  list(spatial_coordinates.keys())
    random.shuffle(keys)

    output_co = 'spatial_output_percentage.co'
    with open(output_co, 'w', encoding="utf-8") as output_file:
        output_file.write(f"{nodes_to_combine} {num_coordinates}\n")
        for i in range(nodes_to_combine):
            selected_nodes.append(graph_nodes[i])
            spatial_nodes = [spatial_coordinates[key] for key in keys]
            output_file.write(f"{graph_nodes[i]} {' '.join(str(coord) for coord in spatial_nodes[i])}\n")

def main(argv):
    gr_file = ''
    co_file = ''
    percentage = 0

    try:
        opts, args = getopt.getopt(argv, "hg:c:p:", ["grfile=", "cofile=", "percentage="])
    except getopt.GetoptError:
        print("Usage: script.py -g <grfile> -c <cofile> -p <percentage>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("Usage: script.py -g <grfile> -c <cofile> -p <percentage>")
            sys.exit()
        elif opt in ("-g", "--grfile"):
            gr_file = arg
        elif opt in ("-c", "--cofile"):
            co_file = arg
        elif opt in ("-p", "--percentage"):
            percentage = float(arg)

    spatial_graph(gr_file, co_file, percentage)

if __name__ == "__main__":
    main(sys.argv[1:])
