
# Created by Arul Prakash Samathuvamani on 1st Feb 2021
# Practice Problem for Google HashCode 2021
# Contact - hello@arulprakash.dev
# Team - Arul Prakash Samathuvamani, Pravin Srinivasan, Elamathi S
# ------

# Sort Function Definition

#Definition of Linked List Classes

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

#another comment

def sort_function(pizza_information, number_of_pizza):
    i = 0
    while(i < int(number_of_pizza)):
        j = i+1
        while(j < int(number_of_pizza)):
            if(pizza_information[i].data < pizza_information[j].data):
                temp = pizza_information[i].data
                temp_node = pizza_information[i].next
                pizza_information[i].data = pizza_information[j].data
                pizza_information[i].next = pizza_information[j].next
                pizza_information[j].data = temp
                pizza_information[j].next = temp_node
            j = j + 1
        i = i + 1
    return pizza_information

# Function to find the difference in list

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

# get raw input from the user
raw_input = input()
# split the input based on the space " " character
number_of_pizza , two_member , three_member , four_member = raw_input.split(" ")

i = 0

pizza_information = []

# Getting input data in form of linked list

while(i < int(number_of_pizza)):
    temp_list = []
    raw_input = input()
    temp_list_ingredients = raw_input.split(" ")[0]
    temp_list = raw_input.split(" ")[1: ]
    pizza_information.append(ingredient_count(temp_list_ingredients,pizza_id(i,ingredients(temp_list))))
    i = i+ 1

i = 0

"""
while (i<int(number_of_pizza)):
    print("new loop")
    print(pizza_information[i].data)
    print(pizza_information[i].next.data)
    print(pizza_information[i].next.next.data)
    i = i + 1
"""
pizza_information = sort_function(pizza_information,number_of_pizza)

## Always initialise i=0 before starting of while loop - NOTE FOR ARUL PRAKASH SAMATHUVAMANI

remaining_teams = int(four_member) + int(three_member) + int(two_member)
remaining_pizza = int(number_of_pizza)
flag = 1
pizza_delivered = 0
delivery_information = []

# Test Comment

print(pizza_information[0].next.next.data)
print(pizza_information[2].next.next.data)

print("difference")

#print(len(Diff(pizza_information[0].next.next.data,pizza_information[2].next.next.data)))


while (remaining_teams > 0 && flag == 1):
    if(two_member > 0 && remaining_pizza >2):

        i=0
        j=remaining_pizza-1
        best_diff = 0
        ## Assingn Pizza
        while(i<int(number_of_pizza)):
            while(j > 0):
                if(i == 0 && j == (remaining_pizza-1)):
                    best_diff = len(Diff(pizza_information[0].next.next.data,pizza_information[2].next.next.data)
                if(len(Diff(pizza_information[0].next.next.data,pizza_information[2].next.next.data))

    elif(three_member > 0 && remaining_pizza > 3):


    elif(four_member >0 && remaining_pizza >4):

    else:
        flag = 0