from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        text="some text", text_type=TextType.LINK, url="https://www.boot.dev"
    )
    print(text_node)


if __name__ == "__main__":
    main()
