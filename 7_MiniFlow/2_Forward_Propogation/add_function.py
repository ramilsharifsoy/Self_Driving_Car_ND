final_value = 0
for i in range(4):
    node_value = self.inbound_nodes[i].value
    final_value += node_value
    self.value = final_value