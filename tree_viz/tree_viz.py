from sklearn import tree
from sklearn.tree import _tree
import networkx as nx


def get_tree_graph(clf, feature_names):
    '''Creates an networkx.DirGraph object that represents the decision tree.
    
    Parameters:
    -----------
    clf: decision sklearn.tree
        The decision tree to extract the graph representation
    feature_names: list
        The feature names of the dataset used for building the decision tree

    Returns:
    --------
        graph: directed graph representation of the tree
    '''
    tree_ = clf.tree_
    # Create a list with the feature evaluated in each tree node.
    node_features = ['undefined' if f == _tree.TREE_UNDEFINED else feature_names[f] 
                     for f in tree_.feature]
    tree_graph = nx.DiGraph()
    def gen_tree_graph(node, depth, tree_graph):
        '''Recursively traverses the tree updating the graph.
        '''
    gen_tree_graph(tree_, node=0, depth=1, tree_graph=tree_graph)
    return tree_graph


    
 

def plot_tree(tree):
    tree_graph = get_tree_graph(tree)
    plot_tree_graph(g)
    return None

