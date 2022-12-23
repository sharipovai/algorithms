#bin tree
class Bin_tree:
    
    def __init__(self, a):
        self.value = None
        self.left_node = None
        self.right_node = None        
        for digit in a:
            self.write_value(digit)
    
    def write_value(self, digit):
        if self.value != None and digit < self.value:
            if self.left_node:
                self.left_node.write_value(digit)
            else:
                self.left_node = Bin_tree([digit])
        elif self.value !=None and digit > self.value:
            if self.right_node:
                self.right_node.write_value(digit)
            else:
                self.right_node = Bin_tree([digit])
        else:
            self.value = digit
        
    def __str__(self):
        if self.left_node:
            print(self.left_node, end='')
        print(self.value, end=' ')
        if self.right_node:
            print(self.right_node, end='')
        return ""     

a = [0, 5, -9, -10, 8, 4 , 1, 0, 3, -6, -10]
b = [0, 5, -9, 10]

bin_tree = Bin_tree(a)
print(bin_tree, end='')
            
        
        

