class Categoria:
    def __init__(self, id, name, has_children, url, children):
        self.id = id
        self.name = name
        self.has_children = has_children
        self.url = url
        self.children = children