# This is a sample Python script.
from tree import RedBlackTree


def solve_task() -> None:
    rbt = RedBlackTree()
    rbt.insert(55)
    rbt.print_whole_tree()
    rbt.insert(40)
    rbt.print_whole_tree()
    rbt.insert(65)
    rbt.print_whole_tree()
    rbt.insert(60)
    rbt.print_whole_tree()
    rbt.insert(75)
    rbt.print_whole_tree()
    rbt.insert(57)
    rbt.print_whole_tree()
    rbt.delete_node(40)
    rbt.print_whole_tree()


if __name__ == '__main__':
    solve_task()
