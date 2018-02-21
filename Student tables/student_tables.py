import os
from random import choice as random_choice


# L[x::y] means a slice of L where the x is the index to start from and y is the step size.
#Betyder egentlig gå igennem en liste, sker dele af listen ud hver gang og tilføj til en ny liste.


def create_seats(student_list, tables):
    return [student_list[i::tables] for i in range(tables)]

def create_seats_with_print(student_list, tables):
    new_list = []
    for i in range(tables):
        new_list.append(student_list[i::tables])
        print("Table {} has the following students: {} ".format((i+1), student_list[i::tables]))

    return new_list

student_list = ["Test13", "Test14", "Test15", "Test16", "Test1", "Test2","Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10", "Test11", "Test12",]
randomized_list = []
tables = 6

while student_list:
    choice = random_choice(student_list)
    student_list.remove(choice)
    randomized_list.append(choice)

final_tables = create_seats_with_print(randomized_list, tables)
print(final_tables)

