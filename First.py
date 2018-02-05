import networkx as nx
from operator import itemgetter 
import networkx as nx 
import wikipedia

source = "Machine Learning".title()
visited = set()
queue = [(0,source)]

G = nx.DiGraph()
depth,node = queue[0]
visited.add(source)
while depth < 2:
    depth, node = queue[0]
    print(node)
    del queue[0]
    try:
        wiki = wikipedia.page(node)
    except:
        print("Could not load",node)
        continue
    for link in wiki.links:
        link = link.title()
        if not link.startswith("List of"):
            if link not in visited:
                visited.add(link)
                queue.append((depth + 1,link))
            G.add_edge(node,link)

print("{}nodes,{}edges".format(len(G),nx.number_of_edges(G)))
        
        