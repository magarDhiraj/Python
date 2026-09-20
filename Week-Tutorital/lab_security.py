def generate_ascii_hash(ch1, ch2, ch3):
    ascii1 = ord(ch1)
    ascii2 = ord(ch2)
    ascii3 = ord(ch3)

    hash_value = ascii1 * ascii2 * ascii3

    return hash_value


def check_strength_level(hash_value):
    if hash_value > 500000:
        return "STRONG HASH"
    else:
        return "WEAK HASH"


ch1 = input("Enter first character: ")
ch2 = input("Enter second character: ")
ch3 = input("Enter third character: ")

ascii1 = ord(ch1)
ascii2 = ord(ch2)
ascii3 = ord(ch3)

hash_value = generate_ascii_hash(ch1, ch2, ch3)

strength = check_strength_level(hash_value)

print("\n--- Security Readout ---")
print("Character 1:", ch1)
print("ASCII Value 1:", ascii1)

print("Character 2:", ch2)
print("ASCII Value 2:", ascii2)

print("Character 3:", ch3)
print("ASCII Value 3:", ascii3)

print("Calculated Hash:", hash_value)
print("Hash Strength:", strength)