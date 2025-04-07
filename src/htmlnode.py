

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclasses")
    
    def props_to_html(self):
        if not self.props:
            return "" 
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
       if self.value is None:
           raise ValueError("Value is None")
       if self.tag is None:
           return self.value
       else:
            props_str = ""
            if self.props:
                props_str = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, props)
        self.children = children
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is None")
        if self.children is None:
            raise ValueError("Children is None")
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"



   
    
