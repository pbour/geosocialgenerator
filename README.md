# Geosocial Network Generator

This repository provides the implementation for the paper "Towards Generating Realistic Geosocial Networks", which presents three combiners that build different types of geosocial networks.

## Dependencies

This project depends on the following Python package and spatial graph generator:

- [NetworkX](https://networkx.github.io/): A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
 
- [SPIDER](https://github.com/aseldawy/spider): A Spatial Data Generator for creating synthetic spatial datasets.

## Prerequisites
Before proceeding, ensure that you have the following prerequisites in place:

1. Python 3: Make sure you have Python 3 installed on your system. You can download it from python.org

2. NetworkX: Install the NetworkX library using 'pip':
```bash
   pip install networkx
```
3. SPIDER: Obtain the SPIDER code from the official source. Follow the SPIDER documentation for installation and usage instructions.

## Overview
The process of generating GR and CO files involves two main steps:

1. Generate a Graph file using NetworkX:
Using NetworkX to create a graph structre that represents the connections between nodes.

## Usage
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
