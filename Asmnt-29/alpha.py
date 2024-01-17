import string

def generate_letter_combinations():
    alphabet = string.ascii_uppercase
    combinations = []

    for letter1 in alphabet:
        for letter2 in alphabet:
            combination = letter1 + letter2
            combinations.append(combination)

    return combinations

if __name__ == "__main__":
    combinations = generate_letter_combinations()

    # Printing the combinations
    for combo in combinations:
        print(combo)
