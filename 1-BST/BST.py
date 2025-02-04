class Node:
  def __init__(self, data):
    self.left = self.right = None
    self.data = data

class BST:
  def __init__(self, root):
    self.root = root
  def __init__(self):
    self.root = None

  def find(self, data):
    return self.find_from(self.root, data)
  def find_from(self, node, data):
    if node == None:
      return None
    if (data == node.data):
      return node
    if (data < node.data):
      return self.find_from(node.left, data)
    return self.find_from(node.right, data)
  
  def insert(self, data):
    if self.root == None:
      self.root = Node(data)
    else:
      self.insert_on(self.root, data)
  def insert_on(self, node, data):
    if (data <= node.data):
      if (node.left == None):
        node.left = Node(data)
      else:
        self.insert_on(node.left, data)
      return
    if (node.right == None):
      node.right = Node(data)
    else:
      self.insert_on(node.right, data)
  
  def preorder(self):
    self.preorder_from(self.root)
    print()
  def preorder_from(self, node):
    if node != None:
      print(node.data, end=" ")
      self.preorder_from(node.left)
      self.preorder_from(node.right)

  def inorder(self):
    self.inorder_from(self.root)
    print()
  def inorder_from(self, node):
    if node != None:
      self.inorder_from(node.left)
      print(node.data, end=" ")
      self.inorder_from(node.right)
  
  def postorder(self):
    self.postorder_from(self.root)
    print()
  def postorder_from(self, node):
    if node != None:
      self.postorder_from(node.left)
      self.postorder_from(node.right)
      print(node.data, end= " ")

def main():
  bst = BST()
  
  bst.insert(1)
  bst.insert(5)
  bst.insert(4)
  bst.insert(6)
  bst.insert(7)

  bst.preorder()
  bst.inorder()
  bst.postorder()

if __name__ == "__main__":
  main()