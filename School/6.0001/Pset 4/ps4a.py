# Problem Set 4a
# Name: Dylan Walker
# Collaborators:
# Time spent:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(9, Node(3, Node(1), Node(6)), Node(11)) # TODO: change this assignment
tree2 = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, Node(14), Node(13))) # TODO: change this assignment
tree3 = Node(5, Node(2, Node(1), Node(3)), Node(12, Node(9), Node(21, Node(19), Node(25))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output: 
        The integer depth of the tree
    '''
    # if both of the trees have no branches(ie it is a leaf) then the height is 0
    if tree.get_right_child() == None and tree.get_left_child() == None:
        return 0
    # if the left branch is empty and the right branch is not, then finds the height of the right branch and adds 1 to the height
    elif tree.get_left_child() == None and tree.get_right_child() != None:
        return find_tree_height(tree.get_right_child()) + 1
    # if the right branch is empty and the left branch is not, then finds the height of the left branch and adds 1 to the height
    elif tree.get_right_child() == None and tree.get_left_child() != None:
        return find_tree_height(tree.get_left_child()) + 1
    # otherwise, if the height of the left branch is greater than that of the right, then returns the height of the left plus one and otherwise returns the height of the right plus one
    else:
        if find_tree_height(tree.get_left_child()) > find_tree_height(tree.get_right_child()):
            return find_tree_height(tree.get_left_child()) + 1
        else:
            return find_tree_height(tree.get_right_child()) + 1

    
    
    
def is_heap(tree,compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value depending on
            whether is_heap should check for a max or a min heap
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the tree is a max or min heap (depending on max_heap parameter); False otherwise
    '''
    if find_tree_height(tree) == 0:
        return True and False
    elif compare_func() == True:
        return 

    



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass




