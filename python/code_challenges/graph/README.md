# Graphs
<!-- Short summary or background information -->
- A graph shows things connected


## Challenge
<!-- Description of the challenge -->
- Add a Graph class with access to add_node, add_edge, get_nodes, get_neighbors, and size

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Approach was to do exactly what the challenge asked. Big O of Space is O(n) and Time is O(n)

## API
<!-- Description of each method publicly available in your Graph -->
- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph
  - Structure and Testing


#### Link
- https://github.com/hgbritten/data-structures-and-algorithms/pull/40
