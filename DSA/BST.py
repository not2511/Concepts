class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
                
    def contains(self,value):
        temp=self.root
        while (temp is not None):
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    
    #Here starts the recursive methods
    
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
        
    def __r_contains(self,current_node,value):
        if current_node==None:
            return False
        if value==current_node.value:
            return True
        if value<current_node.value:
            return self.__r_contains(current_node.left,value)
        if value>current_node.value:
            return self.__r_contains(current_node.right,value)
        
    #BFS AND DFS STARTS HERE
    
    def BFS(self):
        current_node=self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
        
    def dfs_pre_order(self):
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    
# my_tree=BST()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.dfs_pre_order())
# print(my_tree.dfs_post_order())
# print(my_tree.dfs_in_order())
# print(my_tree.r_contains(27))
# print(my_tree.r_contains(17))