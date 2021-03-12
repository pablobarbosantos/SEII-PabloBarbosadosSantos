courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.append('Art')
#courses.insert(0, 'Art')
# courses2 = ['Art', 'Education']
# #courses.insert(0, courses2)
# courses.extend(courses2)
# print(len(courses))
# print(courses[-3])
# print(courses[0:2])

# poped = courses.pop()
# courses.reverse()
courses.sort()
print(courses)

print(courses.index('Math'))

for course in courses:
    print(course)
########################################################

# # Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# # print(list_1)
# # print(list_2)

# # # list_1[0] = 'Art'

# # # print(list_1)
# # # print(list_2)


# # # Immutable
# # # tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# # # tuple_2 = tuple_1

# # # print(tuple_1)
# # # print(tuple_2)

# # # tuple_1[0] = 'Art'

# # # print(tuple_1)
# # # print(tuple_2)

# # # Sets
# # cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# # print(cs_courses)


# # # Empty Lists
# # empty_list = []
# # empty_list = list()

# # # Empty Tuples
# # empty_tuple = ()
# # empty_tuple = tuple()

# # # Empty Sets
# # empty_set = {} # This isn't right! It's a dict
# # empty_set = set()
