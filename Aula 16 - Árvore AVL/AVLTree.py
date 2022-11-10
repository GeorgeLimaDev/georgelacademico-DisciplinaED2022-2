class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return f'|{self.value}:h={self.height}|'
    
class AVLTree(object):

    def __init__(self, value:object = None):
        if value is None:
            self.__root = None
        else:
            self.__root = self.insert(value)
    
    def isEmpty(self)->bool:
        return self.__root == None
    
    def insert(self, key:object):
        if self.__root == None:
            self.__root = Node(key)
        else:
            self.__root = self.insert(self.__root, key)
        
    def __insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.value:
            return self.__rightRotate(root)
        if balance < -1 and key > root.right.value:
            return self.__leftRotate(root)
        if balance > 1 and key > root.right.value:
            root.left = self.__leftRotate(root.right)
            return self.__rightRotate(root)
        if balance  < -1 and key < root.right.value:
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)
        
        return root

    def __leftRotate(self, p:Node)->Node:
        u = p.right
        T2 = u.left

        u.left = p
        p.right = T2

        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        u.height - 1 + max(self.getHeight(u.left), self.getHeight(u.right))

        return u

    def __rightRotate(self, p:Node)->Node:
        u = p.left
        T2 = p.right

        u.right = p
        p.left = T2

        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        u.height = 1 + max(self.getHeight(u.left), self.getHeight(u.right))

        return u
    
    def getHeight(self, node:Node)->int:
        if node is None:
            return 0
        return node.height

    def getBalance(self, node:Node)->int:
        if not Node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def preOrder(self):
        self.__preOrder(self.__root)
    
    def __preOrder(self, root):
        if not root:
            return
        print('{0} '.format(root.value), end='')
        self.__preOrder(root.left)
        self.__preOrder(root.right)

    def delete(self, key:object):
        if self.__root is not None:
            self.__root = self.__delete(self.__root, key)

    def __delete(self, root:Node, key:object)->Node:
        if not root:
            return root
        elif key < root.value:
            root.left = self.__delete(root.left, key)
        elif key > root.value:
            root.right = self.__delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.__delete(root.right, temp.value)

            if root is None:
                return root
            
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

            balance = self.getBalance(root)
            if balance > 1 and self.getBalance(root.left) >= 0:
                return self.__rightRotate(root)
            if balance < -1 and self.getBalance(root.right) <= 0:
                return self.__leftRotate(root)
            if balance > 1 and self.getBalance(root.left) < 0:
                root.left = self.__leftRotate(root.left)
                return self.__rightRotate(root)
            if balance < -1 and self.getBalance(root.right) > 0:
                root.right = self.__rightRotate(root.right)
                return self.__leftRotate(root)
            
            return root

    def getRoot(self)->Node:
        return self.__root
    
    def getMinValueNode(self, root:Node)->Node:
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)