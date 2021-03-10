message = 'Hello world'
print(message)

print(len(message))

print(message[0])

print(message[-1])

print(message[0:5])

print(message[:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('Hello'))

print(message.count('l'))

print(message.find('world'))

print(message.find('universe'))

message.replace('world', 'universe')
print(message)

new = message.replace('world', 'universe')
print(new)

message = message.replace('world', 'universe')
print(message)

##############################################################

greeting = 'Hello'
name = 'Michael'

message = greeting + name
print(message)

##############################################################

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)
##############################################################

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

##############################################################

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'

message = f'{greeting}, {name}'
print(message)

print(dir(name))

#print(help(str))
