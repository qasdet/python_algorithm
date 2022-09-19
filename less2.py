
class WrongInsert(Exception):
    def __init__(self, root, node):
        self.text_error = f'Нарушение требований бинарного дерева. ' \
                          f'Попытка вставить {node} {"левее" if node > root else "правее"} корня {root}.'
        super().__init__(self.text_error)


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None


    def insert_left(self, new_node):
        try:
            assert new_node < self.root
        except AssertionError:
            raise WrongInsert(self.root, new_node)

        if self.left_child is None:

            self.left_child = BinaryTree(new_node)

        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj


    def insert_right(self, new_node):
        try:
            assert new_node > self.root
        except AssertionError:
            raise WrongInsert(self.root, new_node)

        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(7)
# r.insert_child(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
# r.insert_child(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert_right(14)
# r.insert_child(14)
print(r.get_right_child().get_root_val())  # -> 14
print(r.get_right_child().get_right_child().get_root_val())  # -> 16