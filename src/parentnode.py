from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if self.children ==  []:
            raise ValueError("Parent node must have child nodes")
        return_str = ""
        for child in self.children:
            if isinstance(child,LeafNode):
                return_str += child.to_html()
            else:
                return_str += child.to_html()
        return f"<{self.tag}>{return_str}</{self.tag}>"



