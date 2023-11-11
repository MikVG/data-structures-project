"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class Test(unittest.TestCase):
    node1 = Node(3, None)
    stack = Stack()
    stack.push('data1')
    stack.push('data2')

    def test_class(self):
        self.assertEqual(self.node1.data, 3)
        self.assertEqual(self.node1.next_node, None)

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')

    def test_pop(self):
        self.assertEqual(self.stack.top.next_node.next_node, None)
