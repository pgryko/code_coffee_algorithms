# Binary Trees

A dynamic set, where a balanced tree with n nodes have operations that take $`\Theta \left(\lg n\right)`$.

They satisfy the property that, for node x in a binary search tree, node y is in the left subtree of x when $`y.key \leq x.key`$, and on the right when $`y.key \geq x.key`$.

An inorder tree walk, prints all the elements in a binary tree, in order $`\Theta \left(n\right)`$.

```
Inorder-Tree-Walk(x)

1: if x != NIL
2:    Inorder-Tree-Walk(x.left)
3:    print x.key
4:    Inorder-Tree-Walk(x.right)

```
## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./binarysearchtrees

Or manually using g++
$ g++ --std=c++1z main.cpp