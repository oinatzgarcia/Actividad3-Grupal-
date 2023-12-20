import filecmp
import hashlib
import re

# Function to create a hash of votes
def create_vote_hash(vote):
    # Creating a hash of the vote using SHA-256
    hash_object = hashlib.sha256(vote.encode())
    return hash_object.hexdigest()

# Function to validate the ID format
def validate_dni(dni):
    # Verifying if the ID has the correct format: 8 numbers followed by a letter
    return bool(re.match(r'^\d{8}[A-Za-z]$', dni))

# Function to write the hash to an external file
def write_hash_to_file(hashed_vote):
    filename = 'hashed_votes.txt'
    try:
        with open(filename, 'a') as file:
            file.write(hashed_vote + '\n')
        print(f"The hash has been saved to {filename}.")
    except IOError:
        print("Error attempting to write to the file.")

# Simulating a vote
def main():
    candidates = ["VOX", "PSOE", "SUMAR"]

    print("Welcome to the electronic voting system.")
    dni = input("Please enter your ID number: ")

    if validate_dni(dni):
        print("Please choose your candidate:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")

        vote = input("Enter the number of your chosen candidate: ")

        try:
            vote = int(vote)
            if 1 <= vote <= len(candidates):
                selected_candidate = candidates[vote - 1]
                hashed_vote = create_vote_hash(selected_candidate + dni)  # Adding the ID to the vote before hashing
                print("Your vote has been securely registered.")
                print(f"Hash of your vote: {hashed_vote}")

                # Writing the hash to an external file
                write_hash_to_file(hashed_vote)
                print("The hash has been saved to hashed_vote.txt.")
            else:
                print("Please enter a valid number corresponding to the candidate.")
        except ValueError:
            print("Please enter a valid number for the candidate.")
    else:
        print("The entered ID number is not valid or doesn't have the correct format (8 numbers followed by a letter).")

if __name__ == "__main__":
    main()

