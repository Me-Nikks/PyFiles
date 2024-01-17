age = 54
txt = "Jennifer is {} old!"
print(txt.format(age))

# f-string formatting string literals
name = 'Charlli'
age = 2
formatted_string = f'He is {name} and he is just {age} years old.'
print(formatted_string)

# % operator 
name = 'The Taj Mahal Palace'
age = 120
formatted_string = ' %s, mumbai is %d years old.' % (name, age)
print(formatted_string)

# separator
print('DD', 'MM','YY', sep='//')

# end
print('Hey, You look amazing', end='!!!')