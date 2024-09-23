import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user for the password length
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
generated_password = generate_password(password_length)

# Display the generated password
print("Your generated password is:", generated_password)
