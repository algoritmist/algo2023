from btrees.AbstractTree import AbstractTree, left_height, right_height, update


class Tree(AbstractTree):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 0
        self.left_child = None
        self.right_child = None
        self.size = 1

    def __str__(self):
        return f"({self.key}, {self.value})"


def insert(t: Tree, key, value) -> Tree:
    if t is None:
        return Tree(key, value)
    if key == t.key:
        return t
    if key < t.key:
        t.left_child = insert(t.left_child, key, value)
    else:
        t.right_child = insert(t.right_child, key, value)
    update(t)
    return balance(t)


def remove_min(t: Tree) -> Tree | None:
    if t is None:
        return None
    if t.left_child is None:
        return t.right_child
    t.left_child = remove_min(t.left_child)
    return balance(t)


def remove(t: Tree, key) -> Tree | None:
    if t is None:
        return None
    if key == t.key:
        if t.right_child is None:
            return t.left_child
        min_node = find_min(t.right_child)
        min_node.right_child = remove_min(t.right_child)
        min_node.left_child = t.left_child
        return balance(min_node)
    if key < t.key:
        t.left_child = remove(t.left_child, key)
    else:
        t.right_child = remove(t.right_child, key)
    return balance(t)


def balance(t: Tree):
    if t is None:
        return None
    diff_root = left_height(t) - right_height(t)
    if diff_root == -2:
        diff_right = left_height(t.right_child) - right_height(t.right_child)
        if diff_right == -1:
            return right_right_rotate(t)
        else:
            return right_left_rotate(t)
    if diff_root == 2:
        diff_left = left_height(t.left_child) - right_height(t.left_child)
        if diff_left == -1:
            return left_right_rotate(t)
        else:
            return left_left_rotate(t)
    return t


def right_rotate(x: Tree):
    if x is None:
        return None
    y = x.right_child
    x.right_child, y.left_child = y.left_child, x
    update(x)
    update(y)
    return y


def left_rotate(x: Tree):
    if x is None:
        return None
    y = x.left_child
    x.left_child, y.right_child = y.right_child, x
    update(x)
    update(y)
    return y


def right_right_rotate(x: Tree):
    return right_rotate(x)


def right_left_rotate(x: Tree):
    x.right_child = left_rotate(x.right_child)
    return right_rotate(x)


def left_right_rotate(x: Tree):
    x.left_child = right_rotate(x.left_child)
    return left_rotate(x)


def left_left_rotate(x: Tree):
    return left_rotate(x)
