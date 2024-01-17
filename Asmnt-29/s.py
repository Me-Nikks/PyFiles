sentence = "Some words start with s, such as srujan, sridhar, and sun and some not."

# List comprehension to extract words starting with 's'
words_starting_with_s = [word for word in sentence.split() if word.lower().startswith('s')]

# Display the list of words starting with 's'
print(words_starting_with_s)


# Pythagorean triples

# Limit for the maximum value of 'a', 'b', and 'c'
limit = 20

# List comprehension to generate Pythagorean triples (a, b, c)
pythagorean_triples = [(a, b, c) for a in range(1, limit) for b in range(a, limit) for c in range(b, limit) if a**2 + b**2 == c**2]

# Display the list of Pythagorean triples
print(pythagorean_triples)

