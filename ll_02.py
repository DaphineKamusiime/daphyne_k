from email import header
from tempfile import tempdir


class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
    def get_data(self):
        return self.value
class LinkedList(object):
    def _init_(self,head=None):
        self.head=head
    def insert_first(self,new_element):
        new_element=head
        self.head=new_element
    def delete_first(self):
        if self.head:
            temp=self.head
        self.head.next
           return temp
        else:
        return None
    class stack(object):
        def __init__(self,top=None):
            self.lil=LinkedList(top)
            
        def push(self,new_element)
            self.lil.insert_first(new_element) 
       
       def push(self):
           self.lil.delete_first()
           
n1=Node('a')        
n2=Node('b')
n3=Node('c')
n4=Node('d')

stack=Stack(n1)
print(stack)

stack.push(n2)
stack.push(n3)
print(stack.pop())