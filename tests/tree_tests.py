import unittest

from tree import RedBlackTree


class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert_single(self):
        self.tree.insert(5)
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_insert_multiple(self):
        values = [5, 3, 7, 6, 8]
        for val in values:
            self.tree.insert(val)
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_delete_leaf(self):
        self.tree.insert(5)
        self.tree.delete_node(5)
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_delete_internal_node(self):
        values = [20, 10, 30, 5, 15]
        for val in values:
            self.tree.insert(val)
        self.tree.delete_node(10)
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_insert_duplicate(self):
        self.tree.insert(5)
        self.tree.insert(5)  # Duplicate insert
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_large_tree_balance(self):
        for i in range(1, 100):
            self.tree.insert(i)
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def test_delete_nonexistent(self):
        self.tree.insert(10)
        self.tree.delete_node(20)  # Non-existent node
        self.assertTrue(self.check_red_black_properties(self.tree.root))

    def check_red_black_properties(self, node):
        if node is None:
            return True

        # Check for consecutive red nodes
        if node.color == "red":
            if (node.left is not None and node.left.color == "red") or \
                    (node.right is not None and node.right.color == "red"):
                return False

        # Check black height property
        return self.check_black_height(node) != 0

    def check_black_height(self, node):
        if node is None:
            return 1  # Count black height as 1 for leaf nodes

        left_black_height = self.check_black_height(node.left)
        if left_black_height == 0:
            return 0  # Left subtree is not balanced

        right_black_height = self.check_black_height(node.right)
        if right_black_height == 0:
            return 0  # Right subtree is not balanced

        # Both left and right subtrees should have the same black height
        if left_black_height != right_black_height:
            return 0  # Imbalance in black height

        # Add one to black height if the current node is black
        return left_black_height + (1 if node.color == "black" else 0)

    def test_search_existing(self):
        values = [20, 10, 30, 5, 15]
        for val in values:
            self.tree.insert(val)
        node = self.tree.search(15)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 15)

    def test_search_non_existing(self):
        values = [20, 10, 30, 5, 15]
        for val in values:
            self.tree.insert(val)
        node = self.tree.search(99)
        self.assertIsNone(node)

    def test_search_empty_tree(self):
        node = self.tree.search(5)
        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()
