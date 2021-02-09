Code implemented using Python Linked List. 
Linked List declaration:

class ingredient_count:

    def __init__(self,data,Node ):
        self.data = data
        self.next = Node

class pizza_id:

    def __init__(self,data,Node):
        self.data = data
        self.flag  = 1
        self.next = Node

class ingredients :

    def __init__(self,data):
        self.data = data

class delivered_pizza:
    def __init__(self,data):
        self.data = data

The input from the command line is acquired using split() method.
# Getting input data in form of linked list

while(i < int(number_of_pizza)):
    temp_list = []
    raw_input = input()
    temp_list_ingredients = raw_input.split(" ")[0]
    temp_list = raw_input.split(" ")[1: ]
    pizza_information.append(ingredient_count(temp_list_ingredients,pizza_id(i,ingredients(temp_list))))
    i = i+ 1

i = 0

The input from the user is then sorted. The Sort function is not optimized. The sort function can be optimized with Count Sort Algorithm.
Current  idea is to use loops within loops for each team starting with two member team ending with four member team. Improvements needs to be made with this loop function to reduce the number of loops in order to decrease the chances of the code being stuck in infinite loop.
Flag setting is being used to exit from the loop, any other efficient method of exiting from the loop might be required.
