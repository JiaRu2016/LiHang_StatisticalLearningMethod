import copy


class Node(object):
    """树节点
    """
    
    def __init__(self, idx):
        self.idx = idx
        self.father = None
        self.left = None
        self.right = None
        #self.brother = self.father.left if self.is_right else self.father.right
        self.is_right = False
        self.is_left = False
        
    def __repr__(self):
        return '<BinaryTree.Node> {}'.format(self.idx)
        
    def add_left_child(self, node):
        """添加左子树
        """
        node.father = self
        self.left = node
        self.is_left = True
        
    def add_right_child(self, node):
        """添加右子树
        """
        node.father = self
        self.right = node
        self.is_right = True
    
    
class BinaryTree(object):
    """二叉树
    """
    
    def __init__(self, root):
        assert isinstance(root, Node)
        self.root = root
        
def _preorder_iter(node):
    """前序遍历
    """
    #import pdb; pdb.set_trace()
    print('>>>>>>>> calling _preorder_iter, node={}'.format(node))
    yield node.idx
    print('>>>>>>>> yield node {}'.format(node))
    if node.left is not None:
        print('--> left tree')
        print(node.left)
        yield from _preorder_iter(node.left)
        print('--> {} left subtree search finished'.format(node))
    if node.right is not None:
        print('--> right tree')
        yield from _preorder_iter(node.right)
        print('--> {} right subtree search finished'.format(node))

# def preorder(self):
#     self._preorder_iter(self.root)
#     print('preoder_iter from root finished')


root = Node(0)
root.add_left_child(Node(1))
root.add_right_child(Node(2))

root.left.add_left_child(Node(3))
root.left.add_right_child(Node(4))

root.right.add_left_child(Node(5))
root.right.add_right_child(Node(6))


for node in _preorder_iter(root):
    print(node)