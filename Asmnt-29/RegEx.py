import re

# Sample text
text = "Hello, I am learning python from past 30  @ various resources"
# findall: Finds all occurrences of a pattern in the text
pattern_findall = r'\d'  # Matches one or more digits
matches_findall = re.findall(pattern_findall, text)
print("findall:")
print("All matches of digits:", matches_findall)

# search: Searches for the first occurrence of a pattern in the text
pattern_search = r'python'
match_search = re.search(pattern_search, text)
print("\nsearch")
print("First occurrence of 'Python' found at index:", match_search.start())

# split: Splits the text based on a pattern
pattern_split = r'\W+'  # Splits by non-word characters
split_result = re.split(pattern_split, text)
print("\nsplit:")
print("Text split by non-word characters:", split_result)

# sub: Substitutes occurrences of a pattern in the text with a new string
pattern_sub = r'\W+'  # Matches non-word characters
sub_result = re.sub(pattern_sub, ' ', text)
print("\nsub:")
print("Text with non-word characters replaced:", sub_result)
