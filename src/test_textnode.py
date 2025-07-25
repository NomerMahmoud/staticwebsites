import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noneurl(self):
        node = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1",
        )
        self.assertNotEqual(node.url, None)

    def test_text_type(self):
        node = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://www.boot.dev/lessons/0abc7ce4-3855-4624-9f2d-7e566690fee1",
        )
        self.assertNotEqual(node.text_type.value, TextType.BOLD)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
