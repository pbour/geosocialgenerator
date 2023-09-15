# Geosocial Network Generator

We study the generation of realistic geosocial networks. For this purpose, we consider three types of synthetic networks which mimic the characteristics of real networks. The repository provides the code for the generation process. 

The geenration process comprises two phases. First, a graph and a spatial generator are independently employed to create a synthetic social network and a collection of geospatial objects, respectively. In the second phase, these intermediate datasets are then combined to construct a geosocial network. A combiner is defined for each type of synthetic geosocialnetwork, i.e., G<sub>s</sub>, G<sub>c</sub> and G<sub>p</sub>.
This repository provides the implementation for the paper "Towards Generating Realistic Geosocial Networks", which presents three combiners that build different types of geosocial networks.

## Dependencies

This project depends on the following Python package and spatial graph generator:

- [NetworkX](https://networkx.github.io/): A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
 
- [SPIDER](https://github.com/aseldawy/spider): A Spatial Data Generator for creating synthetic spatial datasets.

## Prerequisites
Before proceeding, ensure that you have the following prerequisites in place:

1. Python 3: Make sure you have Python 3 installed on your system. You can download it from python.org
   
2. Clone or Download this repository to your local machine.

3. NetworkX: Install the NetworkX library using 'pip':
```bash
   pip install networkx
```
4. SPIDER: Download the SPIDER code from the official source. Follow the SPIDER documentation for installation and usage instructions.

## Workflow
The process of generating a Geosocial Network involves two main steps:

### GR and CO Files
The user has the option to generate or upload his own GR and CO files, as they correspond to the correct form. 

#### GR File
Use the following command lines and run the 'graph_generator.py' program to generate a graph with NetworkX and save it to a GR file:

- **Barabasi-Albert Graph:**
```bash
python3 graph_generator.py -t barabasi -n <number_of_nodes> -m <number_of_edges>
```
 - **Scale-Free Graph (Undirected):**
```bash
python3 graph_generator.py -t scale_free -n <number_of_nodes> -a <alpha> -b <beta> -g <gamma> -d <delta_in> -o <delta_out>
```

 - **Scale-Free Graph (Directed):**
```bash
python3 graph_generator.py -t scale_free_digraph -n <number_of_nodes> -a <alpha> -b <beta> -g <gamma> -d <delta_in> -o <delta_out>
```

 - **Power Cluster Graph:**
```bash
python3 graph_generator.py -t power -n <number_of_nodes> -m <number_of_edges> -p <probability>
```
     
#### CO File
Generate Spatial Coordinates (CO file) using SPIDER:
- Using SPIDER to generate spatial coordinates for the graph nodes.
- Depending on your requirements, SPIDER can create spatial data that represent real world geographical data.

### Spatial Combiners
After you have created or uploaded the GR and CO files, you can now choose how you want to combine them and what type of geosocial graph you want to create.

#### G<sub>s</sub> Combiner
To run the `combiner_Gs.py` script, use the following command-line syntax:

```bash
python3 combiner_Gs.py -g graph.gr -c spatial.co -p 0.9
```

Command Line Options:
- *-g*: Specifies the input graph file.
- *-c*: Specifies the input spatial data file.
- *-p*: Sets the parameter for the percentage.

#### G<sub>p</sub> Combiner
To run the `combiner_Gp.py` script, use the following command-line syntax:

```bash
python3 combiner_Gp.py -g graph.gr -c spatial.co -m 3 -s 1.5 -n 10
```
Command Line Options:
- *-g*: Specifies the input graph file.
- *-c*: Specifies the input spatial data file.
- *-m*: Sets the parameter for the mean.
- *-s*: Sets the parameter for the standard deviation.
- *-n*: Sets the parameter for the number of nodes to combine.

#### G<sub>c</sub> Combiner
To run the `combiner_Gc.py` script, use the following command-line syntax:

```bash
python3 combiner_Gc.py -g graph.gr -c spatial.co -m 3 -s 1.5 -n 10
```

Command Line Options:
- *-g*: Specifies the input graph file.
- *-c*: Specifies the input spatial data file.
- *-m*: Sets the parameter for the mean.
- *-s*: Sets the parameter for the standard deviation.
- *-n*: Sets the parameter for the number of nodes to combine.


## Example

To illustrate the integration, here is an example:

1. Use the GraphGenerator class in the graph_generator.py file to generate various types of scale free graphs and save them to a gr file, representing a social network where the nodes represent users and the edges represent friendships.
   
3. Use SPIDER to generate spatial coordinates for each user and save them to a co file.

4. Combine the graph data (GR) with the spatial coordinates data (CO) to associate each user in the social network with their geographical location.
   
5. Export the combined dataset to GR and CO files, to be ready for further analysis or visualization.

In this repository you will find examples of GR and CO files that can be used to create a geosocial graph.
