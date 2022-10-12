# Huffmans code
# Huffmans code is a type of data compression that takes phrases, orders frequency of characters
# and turns it into a binary tree (e.g. 01=most used character) and so on. I wrote this in college. 


class Node:
    def __init__(self,value,char):
            self.left=None
            self.right=None
            self.value=value
            self.char=char

    def get_char(self)
        return self.char

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def insert(self, value, char):
        if self.value:
            if value >= self.value:
                if self.left is None:
                    self.left = Node(value,char)
                else:
                    self.left.insert(value,char)
            elif value < self.value:
                if self.right is None:
                    self.right = Node(value,char)
                else:
                    self.right.insert(value,char)
        else:
            self.value = value
    def encoder_path(self, char)

def build_encode_table(tree, f_table):

    e_table = {}



def get_frequency(message):

    f_table = {}

    for char in message:
        if char in f_table:
            f_table[char] += 1
        else:
            f_table[char] = 1
    print(f_table)
    return f_table


def build_binary_tree(f_table):
    #print(sorted(f_table, key=f_table.get, reverse=True))
    tree = None;
    for k in f_table:
        if tree is None:
            tree = Node(f_table[k],k)
        tree.insert(f_table[k],k)
    tree.print_tree() 
    return tree


def main():
  
    #If conditions to check encode or decode
    encode_or_decode = input("Choose One:  Encode (1), Decode (2) \n")
    if encode_or_decode == '1':
        message = input("Please enter the message you wish to encode \n")
        f_table = get_frequency(message)
        tree    = build_binary_tree(f_table)
        e_table = build_encode_table(tree, f_table)

    elif encode_or_decode == '2':
        message = input("Please enter the message you wish to decode \n")
        #TODO tree = something, we need to supply a unique tree to decode the message. 

  



main()
