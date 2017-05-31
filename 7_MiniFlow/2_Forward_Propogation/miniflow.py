
class Node(object):
    def __init__(self, inbound_nodes=[]):
        self.inbound_nodes = inbound_nodes  # Nodes from which this Node receives values
        self.outbound_nodes = []            # Nodes to which this Node passes values
        self.value = None                   # A calculated value
        for n in self.inbound_nodes:        # Add this node as an outbound node on its inputs.
            n.outbound_nodes.append(self)
    
    # Compute the output value based on `inbound_nodes` and store the result in self.value.
    def forward(self):                      # These will be implemented in a subclass.
        raise NotImplemented                # Forward propagation.

# An Input Node has no inbound nodes, so no need to pass anything to the Node instantiator
class Input(Node):
    def __init__(self):
        Node.__init__(self)

    def forward(self, value=None):           # Overwrite the value if one is passed in.
        if value is not None:
            self.value = value

class Add(Node):
    # You may need to change this...
    def __init__(self, *inputs):
        Node.__init__(self, inputs)

    def forward(self):
        final_value = 0
        for i in range(4):
            node_value = self.inbound_nodes[i].value
            final_value += node_value
            self.value = final_value

def topological_sort(feed_dict):               # Sort the nodes in topological order using Kahn's Algorithm.

# feed_dict`: A dictionary where the key is a `Input` Node and the value is the respective value feed to that Node.
    input_nodes = [n for n in feed_dict.keys()]

    G = {}
    nodes = [n for n in input_nodes]
    while len(nodes) > 0:
        n = nodes.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_nodes:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            nodes.append(m)

    L = []
    S = set(input_nodes)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_nodes:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L                                        # Returns a list of sorted nodes. 

def forward_pass(output_node, sorted_nodes):        # Performs a forward pass through a list of sorted nodes.
    """
    Arguments:
        `output_node`: A node in the graph, should be the output node (have no outgoing edges).
        `sorted_nodes`: A topologically sorted list of nodes.
    Returns the output Node's value
    """

    for n in sorted_nodes:
        n.forward()

    return output_node.value