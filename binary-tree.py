# Define a tree
# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data

# #  adding nodes
#    def insert(self, data):
               

#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          elif data > self.data:
#                if self.right is None:
#                   self.right = Node(data)
#                else:
#                   self.right.insert(data)
#       else:
#          self.data = data


# # print inorder
#       def inOrderPrint(r):
#          ifr is None:
#          return
#          else:
#        inOrderPrint(r.left)
#          print(r.data)
#          inOrderPrint(r.right)   

  
#      # Inserting the nodes
# if __name__ == '__main__':
#    root = Node('R')
#    root.insert('a')
#    root.insert('b')
#    root.insert('c')
#    root.insert('d')
#    root.insert('e')
#    root.insert('f')
#    root.insert('g')
#    root.insert('h')
   


# # # Use the insert m111111111ethod to add nodes
# # root = Node(12)
# # root.insert(6)
# # root.insert(14)
# # root.insert(3)
# # root.PrintTree()

# inOrderPrint(root)





class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

#  adding nodes
   def insert(self, data):
               

      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data


# # Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
        


# # Use the insert method to add nodes
root = Node(30)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()