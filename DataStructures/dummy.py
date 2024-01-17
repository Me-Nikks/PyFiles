# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# def print_inorder(root):
#     if root:
#         print_inorder(root.left)
#         print(root.val)
#         print_inorder(root.right)

# # Create a tree
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# # Print the tree using inorder traversal
# print("Inorder traversal of binary tree is:")
# print_inorder(root)


# def fun(arr):

#     arr=arr[::-1]

# arr=[1,2,3,4,5]

# fun(arr)

# print(arr)

def fun(n,res=1):

    if(n<=0):

        return res

    return fun(n-1,n*res)

print(fun(5))

 15