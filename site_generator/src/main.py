from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "www.boot.dev")
    print(node)



if __name__ == "__main__":
    main()