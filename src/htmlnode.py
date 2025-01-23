class HTMLNode:
    def __init__(self,tag=None ,value=None ,children=None ,props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return_str = ""
        if not self.props:
            return ""
        else:
            for item in self.props:
                return_str += " " + item + '="' + self.props[item] +'"'
            return return_str
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
    
