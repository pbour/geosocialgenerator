# Geosocial Network Generator

This repository provides the implementation for the paper "Towards Generating Realistic Geosocial Networks", which presents three combiners that build different types of geosocial networks.

## Dependencies

This project depends on the following Python package and spatial graph generator:

- [NetworkX](https://networkx.github.io/): A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
 
- [SPIDER](https://github.com/aseldawy/spider): A Spatial Data Generator for creating synthetic spatial datasets.

## Prerequisites
Before proceeding, ensure that you have the following prerequisites in place:

1. Python 3: Make sure you have Python 3 installed on your system. You can download it from python.org
   
2. Download the code from this repository.

3. NetworkX: Install the NetworkX library using 'pip':
```bash
   pip install networkx
```
4. SPIDER: Download the SPIDER code from the official source. Follow the SPIDER documentation for installation and usage instructions.

## Workflow
The process of generating GR and CO files involves two main steps:

1. Generate a Graph (GR file) using NetworkX:
- Using NetworkX to create a graph structre that represents the connections between nodes and the social network.
- We define the nodes and the edges to establish connections between the nodes.

2. Generate Spatial Coordinates (CO file) using SPIDER:
- Using SPIDER to generate spatial coordinates for the graph nodes.
- Depending on your requirements, SPIDER can create spatial data that represent real world geographical data.
  
3. Combine the Data:
Combine the graph data (GR) generated by NetworkX, the spatial coordinates data (CO) generated by SPIDER, and the individual parameters of the models to create a geosocial network.

The user has the possibility to upload his own GR and CO, as they correspond to the correct form. 

### Percentage Spatial Combiner
To run the `combiner_Gs.py` script, use the following command-line syntax:

```bash
python3 combiner_Gs.py -g graph.gr -c spatial.co -p 0.9
```

Command Line Options:
- *-g*: Specifies the input graph file.
- *-c*: Specifies the input spatial data file.
- *-p*: Sets the parameter for the percentage.

### Geo-Tweet Combiner
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

### Foursquare Combiner
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

1. Use NetworkX to create a graph representing a social network, where nodes are users, and edges represent friendships.
   
2. Use SPIDER to generate spatial coordinates for each user.

3. Combine the graph data (GR) with the spatial coordinates data (CO) to associate each user in the social network with their geographical location.
   
4. Export the combined dataset to GR and CO files, to be ready for further analysis or visualization.
