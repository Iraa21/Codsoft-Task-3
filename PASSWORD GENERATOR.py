import random
import string

def generate_password(length):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting 'length' number of characters from 'characters'
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("PASSWORD GENERATOR")
    print("==================")
    
    # Prompt user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be greater than zero. Please enter a valid length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
