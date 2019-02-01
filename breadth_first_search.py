import unittest


class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, node):
    self.children.append(node)

  def add_children(self, nodes):
    for node in nodes:
      self.add_child(node)


def breadth_first_search(root):
  values = []
  queue = [root]
  while len(queue) > 0:
    current = queue.pop(0)
    values.append(current.value)
    for child in current.children:
      queue.append(child)
  return values


class TestBreadthFirstSearch(unittest.TestCase):

  def test0(self):
    graph = Node('A')
    self.assertEqual(breadth_first_search(graph), ['A'])

  def test1(self):
    graph = Node('A')
    graph.add_children([Node('A'), Node('A'), Node('A')])
    graph.children[0].add_children([Node('A'), Node('A'), Node('A')])

    self.assertEqual(breadth_first_search(graph), ['A'] * 7)

  def test2(self):
    graph = Node('A')
    graph.add_children([Node('B'), Node('C'), Node('D')])
    graph.children[0].add_children([Node('E'), Node('F')])
    graph.children[0].children[0].add_children([Node('I'), Node('J'), Node('K')])
    graph.children[2].add_children([Node('L'), Node('M')])
    graph.children[2].children[1].add_child(Node('N'))
    self.assertEqual(breadth_first_search(graph), [ch for ch in 'ABCDEFLMIJKN'])


if __name__ == '__main__':
    unittest.main()
