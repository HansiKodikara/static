from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("A leaf node must have a value.") 
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

node = LeafNode("b", "Bold text", {"class": "bold"})
print(node.to_html())



