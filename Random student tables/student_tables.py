import os
from random import choice as random_choice


# L[x::y] means a slice of L where the x is the index to start from and y is the step size.
#Betyder egentlig gå igennem en liste, sker dele af listen ud hver gang og tilføj til en ny liste.


def create_tables(student_list, max_seats):
    return [student_list[i::max_seats] for i in range(max_seats)]

def create_test(student_list, max_seats):
    new_list = []
    for i in range(max_seats):
        new_list.append(student_list[i::4])

    return new_list


student_list = ["Test13", "Test14", "Test15", "Test16", "Test1", "Test2","Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10", "Test11", "Test12",]
randomized_list = []
max_seats = 4
tables = 6

while student_list:
    choice = random_choice(student_list)
    student_list.remove(choice)
    randomized_list.append(choice)

final_tables = create_tables(randomized_list, 4)
final_test = create_test(randomized_list, 4)

print(final_tables)
print(final_test)

