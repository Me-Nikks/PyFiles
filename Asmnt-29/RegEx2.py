import re

# exploring Metacharacters in RegEx

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":
# []	A set of characters
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


txt = "helljo planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he...o", txt)
print(x)

txt = "Hiii Team"

# '^' Starts with 

n = re.findall('^hii',txt)
o = re.findall('^Hii',txt)
print(n)
print(o)

txt = "hello planet"

# '$' ends with.

x = re.findall("planet$", txt)
print(x)

txt = "nikhil"

#Search for a sequence that starts with "ni", followed by 0 or more  (any) characters, and an "l":

x = re.findall("ni.*l", txt)

print(x)

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)