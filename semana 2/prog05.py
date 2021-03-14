user = 'Admin'
logged_in = True

if user == 'Admin' and logged_int:
    print('Admin Page')
else:
    print("Bad Creds")


p = [1, 2, 3]
s = [3, 2, 1]

print(id(p))
print(id(s))
print(p is s)


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
