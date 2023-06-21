from enum import Enum

from btrees.AbstractTree import AbstractTree, update


class Color(Enum):
    BLACK = 0
    RED = 1


class Tree(AbstractTree):
    def __init__(self):
        self.direction = None
        self.key = None
        self.value = None
        self.left_child = None
        self.right_child = None
        self.is_root = True
        self.is_leaf = True
        self.color = Color.BLACK
        self.height = 0
        self.size = 1

    def init_leaf(self):
        self.is_leaf = True
        self.is_root = False
        return self

    def set_key(self, key):
        self.key = key
        return self

    def set_value(self, value):
        self.value = value
        return self

    def __str__(self):
        return f"({self.key}, {self.value}, {self.color})"


def show(t: Tree):
    if t is None or t.is_leaf:
        return

    show(t.left_child)
    print(t)
    show(t.right_child)


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


def split_four_tree(t: Tree):
    if t is None or t.is_leaf:
        return t

    if t.left_child.color is Color.RED and t.right_child.color is Color.RED:
        t.color = Color.BLACK if t.is_root else Color.RED
        t.left_child.color = Color.BLACK
        t.right_child.color = Color.BLACK
    return t


def insert(t: Tree, key, value) -> Tree:
    if t.is_leaf:
        t.is_leaf = False
        t.key = key
        t.value = value
        t.color = Color.BLACK if t.is_root else Color.RED
        t.left_child = Tree().init_leaf()
        t.right_child = Tree().init_leaf()
        return t

    t = split_four_tree(t)
    if t.key == key:
        return t
    if key < t.key:
        t.left_child = insert(t.left_child, key, value)
    else:
        t.right_child = insert(t.right_child, key, value)
    t = repair(t)
    update(t)
    return t


def remove_min(t: Tree) -> Tree | None:
    pass


def remove(t: Tree, key) -> Tree | None:
    pass



def left_left_repair(t: Tree) -> Tree:
    if t is None:
        return None
    if t.left_child.color is Color.RED and t.left_child.left_child.color is Color.RED:
        t = right_rotate(t)
        t.color = Color.BLACK
        t.right_child.color = Color.RED
        print("fixing ll")
    return t


def left_right_repair(t: Tree):
    if t is None:
        return None
    if t.left_child.color is Color.RED and t.left_child.right_child.color is Color.RED:
        t = right_left_rotate(t)
        t.color = Color.BLACK
        t.right_child.color = Color.RED
        print("fixing lr")

    return t


def right_left_repair(t: Tree):
    if t is None:
        return None
    if t.right_child.color is Color.RED and t.right_child.left_child.color is Color.RED:
        t = left_right_rotate(t)
        t.color = Color.BLACK
        t.left_child.color = Color.RED
        print("fixing rl")
    return t


def right_right_repair(t: Tree):
    if t is None:
        return None
    if t.right_child.color is Color.RED and t.right_child.right_child.color is Color.RED:
        t = left_rotate(t)
        t.color = Color.BLACK
        t.left_child.color = Color.RED
        print("fixing rr")
    return t


def repair(t: Tree) -> Tree:
    t = left_left_repair(t)
    t = left_right_repair(t)
    t = right_left_repair(t)
    t = right_right_repair(t)
    return t


def left_rotate(x: Tree) -> Tree:
    if x is None:
        return None
    y = x.right_child
    swap_if_root(x, y)
    x.right_child, y.left_child = y.left_child, x
    update(x)
    update(y)
    return y


def swap_if_root(x, y):
    if x.is_root:
        x.is_root = False
        y.is_root = True


def right_rotate(x: Tree) -> Tree:
    if x is None:
        return None
    y = x.left_child
    swap_if_root(x, y)
    x.left_child, y.right_child = y.right_child, x
    update(x)
    update(y)
    return y


def right_right_rotate(x: Tree) -> Tree:
    return right_rotate(x)


def right_left_rotate(x: Tree) -> Tree:
    x.left_child = left_rotate(x.left_child)
    return right_rotate(x)


def left_right_rotate(x: Tree) -> Tree:
    x.right_child = right_rotate(x.right_child)
    return left_rotate(x)


def left_left_rotate(x: Tree) -> Tree:
    return left_rotate(x)
