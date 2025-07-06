from textnode import TextNode, TextType


def main():
    test_node = TextNode(
        "Testing with Anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(test_node)


if __name__ == "__main__":
    main()
