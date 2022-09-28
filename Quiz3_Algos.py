import graphviz

g = graphviz.Graph('simple forest')
nodes = [str(i) for i in range(10)]
for node in nodes:
    g.node(node)
g.edge('0','3')
g.edge('5','6')
g.edge('9','0')
g.edge('8','7')
g.edge('7','2')
g.edge('5','1')
g.render(directory='output', format='png')