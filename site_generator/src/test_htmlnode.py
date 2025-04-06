from htmlnode import HTMLNode

def test_props_to_html_single():
    node = HTMLNode(tag="a", value="Link", props={"href": "https://example.com"})
    assert node.props_to_html() == ' href="https://example.com"'

def test_props_to_html_multiple():
    node = HTMLNode(
        tag="a",
        value="Google",
        props={"href": "https://google.com", "target": "_blank"}
    )
    output = node.props_to_html()
    assert 'href="https://google.com"' in output
    assert 'target="_blank"' in output
    assert output.startswith(" ")

def test_repr():
    node = HTMLNode(tag="p", value="Hello", props={"class": "text"})
    expected_repr = 'HTMLNode(tag=p, value=Hello, children=[], props={\'class\': \'text\'})'
    assert repr(node) == expected_repr

if __name__ == "__main__":
    test_props_to_html_single()
    test_props_to_html_multiple()
    test_repr()
    print("All tests passed.")
