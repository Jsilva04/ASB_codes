import toytree
import toyplot
import numpy as np

print(toytree.__version__)
print(toyplot.__version__)
print(np.__version__)

def phylogen_tree_vizualizer(file):

    tree = toytree.tree(file)

    rtree = tree.root(wildcard = "prz")
    rtree.draw(tip_labels_align = True)


