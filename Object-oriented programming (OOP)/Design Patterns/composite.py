# We are going to create a class called Component which will have move and delete methods:
# Create two more classes: Folder and File, which inherit from Component.The Folder class should have an add_child method:
# Create a root folder and implement the method get_path:



class Component:

    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        self.parent = new_folder
        new_folder.children[self.name] = self

    def delete(self):
        del self.parent.children[self.name]


class Folder(Component):

    def __init__(self, name):
        super().__init__(name)
        self.children = {}


root = Folder("root")


def get_path(path):
    names = path.split("/")[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node
