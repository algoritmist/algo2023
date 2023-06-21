class AbstractTree:
    left_child = None
    right_child = None
    key = None
    height = 0
    size = 1


def find(t: AbstractTree, key) -> AbstractTree:
    if t is None:
        return None
    if t.key == key:
        return t
    return find(t.right_child, key) if t.key < key \
        else find(t.left_child, key)


def find_min(t: AbstractTree) -> AbstractTree:
    if t is None:
        return None
    if t.left_child is None:
        return t
    return find_min(t.left_child)

def lower_bound(t: AbstractTree, key):
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


def kth(t: AbstractTree, k):
    if t is None:
        return None
    if k == left_size(t) + 1:
        return t
    if k <= left_size(t):
        return kth(t.left_child, k)
    return kth(t.right_child, k - left_size(t) - 1)


def count_less(t: AbstractTree, key):
    return size(t) - size(lower_bound(t, key))


def size(t: AbstractTree):
    return 0 if t is None else t.size


def left_size(t: AbstractTree):
    if t.left_child is None:
        return 0
    return t.left_child.size


def right_size(t: AbstractTree):
    if t.right_child is None:
        return 0
    return t.right_child.size


def update(t: AbstractTree):
    t.height = 1 + max(left_height(t), right_height(t))
    t.size = 1 + left_size(t) + right_size(t)


def left_height(t: AbstractTree):
    if t.left_child is None:
        return 0
    return t.left_child.height


def right_height(t: AbstractTree):
    if t.right_child is None:
        return 0
    return t.right_child.height

