"""

Heap / Priority Queue

1. Structure property: BST needs to be complete. Fill nodes from l->r (next avail position)
2. Order property: min/max

** Binary heap's are implemented as arrays under the hood
** Duplicate node values are allowed
** Place root node in index[1], for mathematical reasoning

-> leftChild = 2 * i
-> rightChild = 2 * i + 1
-> parent = i / 2

^^ only true for a complete BT

"""