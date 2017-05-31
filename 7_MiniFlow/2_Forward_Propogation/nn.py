from miniflow import *

x, y, z, k = Input(), Input(), Input(), Input()

f = Add(x, y, z, k)

feed_dict = {x: 4, y: 5, z: 10, k: 10}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

print("Output is {}, (According to miniflow)".format(output))