import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("this is one text node", TextType.LINK)
        node4 = TextNode("this is the other text node", TextType.LINK)
        self.assertNotEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()