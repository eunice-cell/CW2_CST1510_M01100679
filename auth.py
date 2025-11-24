import bcrypt
import os

USER_DATA_FILE = "DATA/users.txt"  #defining the user data file
#implement the Password Hashing Function
def hash_password(plain_text_password):
    bytes_password = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes_password, salt)
    return hashed_password.decode('utf-8')


#impliment password verification function
def verify_password(plain_text_password, hashed_password):
    bytes_plain_text_password = plain_text_password.encode('utf-8')
    bytes_hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(bytes_plain_text_password, bytes_hashed_password)

# implementing user registration
def register_user(username, password):
    # Check if user already exists
    if user_exists(username):
        print("User already exists.")
        return False

    # Hash the password
    hashed_pass = hash_password(password)

    # Append in correct format: username,hashed_password
    with open("DATA/users.txt", "a") as f:
        f.write(f"{username},{hashed_pass}\n")

    print(f"User '{username}' registered successfully.")
    return True


#USER EXISTENCE CHECK
def user_exists(username):
    # Handle case where file doesn't exist yet
    if not os.path.exists("DATA/users.txt"):
        return False

    # Read file and check each username
    with open("DATA/users.txt", "r") as f:
        for line in f:
            existing_username = line.strip().split(",")[0]# to compare only username
            if existing_username == username:
                return True

    return False


# implementing user login
import os


def login_user(username, password):
    # Handle case where file doesn't exist
    if not os.path.exists("DATA/users.txt"):
        print("No users registered yet.")
        return False

    # Search for username
    with open("DATA/users.txt", "r") as f:
        for line in f:
            stored_username, stored_hash = line.strip().split(",")

            if stored_username == username:
                # Verify password
                if verify_password(password, stored_hash):
                   print(f"Success: welcome {username}!")
                   return True
                else :
                    print("invalid password.")
                    return False
    # Username not found
    return False


# implement input validation
def validate_username(username):
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if len(username) > 20:
        return False, "Username cannot exceed 20 characters."
    if not username.isalnum():
        return False, "Username must contain only letters and numbers."
    return True, ""

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
        # Uppercase

    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

        # Lowercase
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

        # Digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    return True, ""


#impliment main menu

def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main():
    # Displays a welcome message when the program starts
    print("\nWelcome to the Week 7 Authentication System!")

    # Starts an infinite loop so the menu keeps showing until user chooses Exit
    while True:
        # Display the main menu
        display_menu()
        # Ask the user for their choice (1–3)
        choice = input("\nPlease select an option (1-3): ").strip()


        # Option 1: Register a new user

        if choice == '1':
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username using the function (will return True/False + message)
            is_valid, error_msg = validate_username(username)

            # If the username is not valid, print the error message and go back to the menu
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Ask user for a password
            password = input("Enter a password: ").strip()

            # Validate the password (you’ll define this function later)
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Ask user to confirm the password
            password_confirm = input("Confirm password: ").strip()

            # Check if the two passwords match
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # If everything is valid, register the user (you’ll define this function later)
            register_user(username, password)


        # Option 2: Login

        elif choice == '2':
            print("\n--- USER LOGIN ---")

            # Ask for login credentials
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt to log in (you’ll define this function later)
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the data)")

            if not user_exists(username):
                print("Error:User does not exist.")

            # Wait for user to press Enter before returning to main menu
            input("\nPress Enter to return to main menu...")


        # Option 3: Exit

        elif choice == '3':
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break  # Breaks the loop to end the program


        # Invalid Option: an option that isn't in the menu
        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


# This ensures the main() function only runs when this file is executed directly
if __name__ == "__main__":
    main()

#__name__ known for dunder name or double underscore name is a special variable that Python automatically creates for every module (file)...