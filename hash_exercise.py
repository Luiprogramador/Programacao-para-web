import hashlib
import bcrypt
from time import sleep


def hash_string(input_string):
    """Returns the SHA-256 hash of the input string."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def bcrypt_hash_string(input_string):
    """Returns the bcrypt hash of the input string."""
    salt = bcrypt.gensalt()
    bcrypt_hash = bcrypt.hashpw(input_string.encode('utf-8'), salt)
    return bcrypt_hash


def main():
    user_input = input("Enter a string to hash: ")
    hashed_output = hash_string(user_input)
    print(f"SHA-256 Hash: {hashed_output}")

    sleep(1)  # Pause for a moment before generating bcrypt hash
    print("\nNow generating bcrypt hash...")
    bcrypt_hashed_output = bcrypt_hash_string(user_input)
    print(f"bcrypt Hash: {bcrypt_hashed_output.decode('utf-8')}")

    


if __name__ == "__main__":
    main()