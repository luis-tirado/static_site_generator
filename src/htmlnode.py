class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children    # list
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html has not been implemented.")
    
    def props_to_html(self): 
        if self.props is None:
            return ""
        props_converted = ""
        for prop in self.props:
            props_converted += f' {prop}="{self.props[prop]}"'
        return props_converted
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes must contain a value.")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        if self.value is None:
            raise ValueError("LeafNodes must contain a value.")   
        
        if self.tag is None and self.props is None:
            return f"LeafNode({self.value})"
        
        if self.tag is None or self.props is None:
            if self.tag is None:
                return f"LeafNode({self.value}, {self.props})"
            else:
                return f"LeafNode({self.tag}, {self.value})"

 
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        elif self.children is None:
            raise ValueError("ParentNode must have children nodes.")
        
        new_children_to_html = ""
        for child in self.children:
            new_children_to_html += child.to_html()

        return f'<{self.tag}>{new_children_to_html}</{self.tag}>'
            
    def __repr__(self):
        if self.props is None:
            return f"ParentNode({self.tag}, {self.children})"
        return f"ParentNode({self.tag}, {self.children}, {self.props})"