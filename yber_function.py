from cryptography.fernet import Fernet
# generate a key
key = "jdgjhliduhgiflhgrijkfiurrrrrrrrrrrrr"

key = Fernet.generate_key()
# print(key)

# original message
message = "I love my cybersecurity"
print(message)


# create cypher object used to encrypt message
cypher = Fernet(key)

# use cypher 
encrypted_message = cypher.encrypt(message.encode())
print(encrypted_message)

# decryption
decrypted_message = cypher.decrypt(encrypted_message)
print(decrypted_message.decode())

# hashing - converting
import hashlib
def hashpassword(password):
    # create the hasher
    hasher = hashlib.sha256()
    # use hasher to hash the passsword
    hasher.update(password.encode())
    hashed_password =hasher.hexdigest()
    
    return hashed_password

hashed_password = hashpassword("admin1234")
print(f"the harshed password is {hashed_password}")


def verifyhash(input_password, harsh_value) :
    hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_input_password ==harsh_value

print(verifyhash("admin1234", hashed_password))