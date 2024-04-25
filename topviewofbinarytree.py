#Top view of binary tree

class TreeNode:
   def __init__(self, val):
       self.data = val
       self.left = None
       self.right = None
  
def topView(root):
   if root == None:
       return
   Q = [[root, 0]]
   result = []
   visited = dict()


   while Q:
       curr = Q.pop(0)
      
       if curr[1] not in visited:
           visited[curr[1]] = curr[0].data


       if curr[0].left != None:
           Q.append([curr[0].left, curr[1] - 1])


       if curr[0].right != None:
           Q.append([curr[0].right, curr[1] + 1])


   for ele in sorted(visited.keys()):
       result.append(visited[ele])


   for ele in result:
       print(ele, end = " ")
   
root = TreeNode(11)
root.left = TreeNode(7)
root.right = TreeNode(15)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.left.left.left = TreeNode(3)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(10)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(14)
root.right.right.left = TreeNode(18)
root.right.right.right = TreeNode(25)








topView(root)


