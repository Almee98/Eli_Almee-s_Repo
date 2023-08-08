import hashlib

from direct.showbase.ShowBaseGlobal import aspect2d
from panda3d.core import TextNode
from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.bg = self.loader.loadModel("models/ripple")
        self.bg.reparentTo(self.render)

        # Create a TextNode to display the name and birthdate
        text_node = TextNode('name')
        text_node.setText("Almee")
        text_node.setTextColor(1, 1, 1, 1)  # Set text color (white)
        text_node.setAlign(TextNode.ACenter)  # Set text alignment (centered)

        # Create a TextNodePath to attach the TextNode to the scene
        text_node_path = aspect2d.attachNewNode(text_node)
        text_node_path.setScale(0.1)  # Set the scale of the text

        # Position the TextNodePath in the window
        text_node_path.setPos(0, 0, -0.3)

        birthdate = "January 1, 1998"

        # Calculate MD5 hash of the birthdate
        hash_object = hashlib.md5(birthdate.encode())
        hashed_birthdate = hash_object.hexdigest()

        # Create a TextNode to display the hashed birthdate
        text_node1 = TextNode('birthdate')
        text_node1.setText(hashed_birthdate)
        text_node1.setTextColor(1, 1, 1, 1)  # Set text color (white)
        text_node1.setAlign(TextNode.ACenter)  # Set text alignment (centered)

        # Create a TextNodePath to attach the TextNode to the scene
        text_node_path1 = aspect2d.attachNewNode(text_node1)
        text_node_path1.setScale(0.1)  # Set the scale of the text

        # Position the TextNodePath in the window
        text_node_path1.setPos(0, 0, -0.5)


app = MyApp()
app.run()