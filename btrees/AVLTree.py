class Tree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 0
        self.left_child = None
        self.right_child = None
        self.size = 1

    def __str__(self):
        return f"({self.key}, {self.value})"


#def list(t: Tree):
#    if t is None:
#        return []
#   return [(t, t.left_child, t.right_child)] + list(t.left_child) + list(t.right_child)


def find(t: Tree, key) -> Tree | None:
    if t is None:
        return None
    if t.key == key:
        return t
    return find(t.right_child, key) if t.key < key \
        else find(t.left_child, key)


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


def find_min(t: Tree) -> Tree | None:
    if t is None:
        return None
    if t.left_child is None:
        return t
    return find_min(t.left_child)


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


def lower_bound(t: Tree, key):
    if t is None:
        return None
    if t.key == key:
        return t

    if key < t.key:
        res = lower_bound(t.left_child, key)
        if res is None or t.key < res.key:
            return t
        return res

    return lower_bound(t.right_child, key)


def kth(t: Tree, k):
    if t is None:
        return None
    if k == left_size(t) + 1:
        return t
    if k <= left_size(t):
        return kth(t.left_child, k)
    return kth(t.right_child, k - left_size(t) - 1)


def count_less(t: Tree, key):
    return size(t) - size(lower_bound(t, key))


def size(t: Tree):
    return 0 if t is None else t.size


def left_size(t: Tree):
    if t.left_child is None:
        return 0
    return t.left_child.size


def right_size(t: Tree):
    if t.right_child is None:
        return 0
    return t.right_child.size


def update(t: Tree):
    t.height = 1 + max(left_height(t), right_height(t))
    t.size = 1 + left_size(t) + right_size(t)


def left_height(t: Tree):
    if t.left_child is None:
        return 0
    return t.left_child.height


def right_height(t: Tree):
    if t.right_child is None:
        return 0
    return t.right_child.height


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
