import random
import string

# Define the character sets to use
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Combine the character sets into a single string
all_chars = lowercase_chars + uppercase_chars + digits + symbols

# Generate a random password by selecting 12 characters from the combined set
password = ''.join(random.sample(all_chars, 12))

# Print the password to the console
print(password)