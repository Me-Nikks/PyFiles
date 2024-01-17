# List of names
names = ['Nikhil', 'Shidhar', 'Srujan', 'Bibin', 'Varsha','Ziya']

# List comprehension to create tuples of first and last letters of each name
first_last_letters = [(name, name[0].lower(), name[-1].lower()) for name in names]

# Display the list of tuples
print(first_last_letters)
