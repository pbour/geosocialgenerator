# Geosocial Network Generator

We study the generation of realistic geosocial networks. For this purpose, we consider three types of synthetic networks which mimic the characteristics of real networks. The repository provides the code for the generation process. 

The figure below illustrates the generation process. Essentially, the process comprises two phases. First, a graph and a spatial generator are independently employed to create a synthetic social network and a collection of geospatial objects, respectively. In the second phase, these intermediate datasets are combined to construct a geosocial network. A combiner is defined for each type of synthetic geosocial network, denoted by G<sub>s</sub>, G<sub>c</sub> and G<sub>p</sub>.

<figure>
  <img src="/figures/generation.png" alt="Generation process" />
</figure>


## Dependencies

This project depends on the following Python packages:

- [NetworkX](https://networkx.github.io/): A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
 
- [SPIDER](https://github.com/aseldawy/spider): A Spatial Data Generator for creating synthetic spatial datasets.

## Prerequisites
Before proceeding, make sure that you have the following prerequisites in place:

1. Python 3: Make sure you have Python 3 installed on your system. You can download it from python.org
   
2. NetworkX: Install the NetworkX library using 'pip':
```bash
   pip install networkx
```
3. SPIDER: Download the SPIDER code from the official source. Follow the SPIDER documentation for installation and usage instructions.

## Workflow

### Generation phase
The graph generators from NetworkX and spatial generators from Spider are independently employed to create a social graph and a collection of geospatial objects, respectively. The outputs are stored inside a .gr and .co file, respectively. 

The user can also skip this phase either entirely or partally by using an existing .gr and/or .co file. 

#### Social graph generation
Currently, we consider three synthetic graph models from NetworkX. 
Execute `graph_generator.py` to generate the specified graph type with NetworkX; save the output to a .gr file, e.g., graph.gr

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
     
#### Spatial objects generation
Execute `generator.py` from Spider to generate a collection of spatial objects. Usage from https://github.com/aseldawy/spider/blob/master/README.md:
```shell
python3 generator.py <distribution> <cardinality> <dimensions> [geometry] [parameters]
```
The parameters are generally specified as a set of `key=value` pairs. The possible keys and their usage is described below.

- *distribution*: {uniform, diagonal, gaussian, parcel, bit, sierpinski}
- *cardinality*: Number of geometries to generate
- *dimensions*: Number of dimensions in generated geometries
- *geometry*: {point, box}. If geometry type is `box` and the distribution is NOT `parcel`, you have to specify the maxsize property
- *maxsize*: maximum size along each dimension (before transformation), e.g., 0.2,0.2 (no spaces)
- *percentage*: (for diagonal distribution) the percentage of records that are perfectly on the diagonal
- *buffer*: (for diagonal distribution) the buffer around the diagonal that additional points can be in
- *srange*: (for parcel distribution) the split range [0.0, 1.0]
- *dither*: (for parcel distribution) the amound of noise added to each record as a perctange of its initial size [0.0, 1.0]
- *affinematrix*: (optional) values of the affine matrix separated by comma. Number of expected values is d*(d+1) where d is the number of dimensions
- *compress*: (optional) { bz2 }
- *format*: output format { csv, wkt, geojson }
[affine matrix] (Optional) Affine matrix parameters to apply to all generated geometries

By default Spider outputs the generated objects in csv format; run the following command to tranform it to the necessary .gr. Replace NUM_OF_OBJECTS with the number of lines in the .csv file.
- **For points:**
```shell
awk -F',' '{lines++; print $1" "$2}' spatial.csv | sed '1s/^/NUM_OF_OBJECTS 2\n/' > spatial.co
```

- **For rectangles:**
```shell
awk -F',' '{lines++; print $1" "$2" "$3" "$4}' spatial.csv | sed '1s/^/NUM_OF_OBJECTS 4\n/' > spatial.co
```

### Combining phase
After you have created or uploaded the GR and CO files, you can now choose how you want to combine them and what type of geosocial graph you want to create.

#### Combiner G<sub>s</sub>
To run the `combiner_Gs.py` script, use the following command-line syntax:

```bash
python3 combiner_Gs.py -g graph.gr -c spatial.co -p 0.9
```

Command Line Options:
- *-g*: Specifies the input graph file.
- *-c*: Specifies the input spatial data file.
- *-p*: Sets the parameter for the percentage.

#### Combiner G<sub>c</sub>
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

#### Combiner G<sub>p</sub> 
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

## Samples
Inside folder `samples` you can find an example of a .gr and of a .co file
