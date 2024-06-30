class BinaryTree:
    def init(self, root=None):
        self.key = root
        self.left_child = None
        self.right_child = None
        
    def insert_node(self, new_node_value):
        if self.key is None:
            self.key = new_node_value
        elif new_node_value < self.key:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node_value)
            else:
                self.left_child.insert_node(new_node_value)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node_value)
            else:
                self.right_child.insert_node(new_node_value)
                
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key
    
    def preorderTrav(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorderTrav()
        if self.right_child:
            self.right_child.preorderTrav()

    def inorderTrav(self):
        if self.left_child:
            self.left_child.inorderTrav()
        print(self.key)
        if self.right_child:
            self.right_child.inorderTrav()

    def postorderTrav(self):
        if self.left_child:
            self.left_child.postorderTrav()
        if self.right_child:
            self.right_child.postorderTrav()
        print(self.key)

print("The binary tree will be created with your numbers.")
print("Please enter 10 numbers to create sorted binary tree")
tree = BinaryTree()

for i in range(10):
    number = int(input("Enter a number: "))
    tree.insert_node(number)
    print("root:", tree.get_root_val())
    if tree.get_left_child():
        print("left child", tree.get_left_child())
    if tree.get_right_child():
        print("right child", tree.get_right_child())
        
print("...***...\nPre-Order")
tree.preorderTrav()
print("...***...\nPost-Order")
tree.postorderTrav()
print("...***...\nIn-Order")
tree.inorderTrav()
