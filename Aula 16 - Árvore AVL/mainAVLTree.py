from AVLTree import *

tree = AVLTree()
TESTE = 1
if TESTE == 1:
    tree.insert(42)
    tree.insert(15)
    tree.insert(88)
    tree.insert(6)
    tree.insert(27)
    tree.insert(4)
    tree.preOrder()
    print()

elif TESTE == 2:
    tree.insert(120)
    tree.insert(100)
    tree.insert(130)
    tree.insert(80)
    tree.insert(110)
    tree.insert(150)
    tree.insert(200)
    tree.preOrder()

elif TESTE == 3:
    tree.insert(120)
    tree.insert(110)
    tree.insert(150)
    tree.insert(80)
    tree.insert(130)
    tree.insert(200)
    tree.insert(100)
    tree.preOrder()

key = 15
if TESTE == 1:
    print()
    tree.preOrder()
    print('Removendo o nó', key)
    root = tree.delete(key)
    tree.preOrder()