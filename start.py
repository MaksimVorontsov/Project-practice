import os
from Parser_create_csv import create_csv
from Parser_get_pic import download_celebrations
from Parser_get_memes import dowload_memes
print("Please choose the path to create Bot's directory (for example: 'C:\\Bot'):")
directory_name = str(input())+'\\'
print("Please move the program files to the created folder")
print("Please enter your windows user's name:")
user_name = str(input())
def main(directory_name, user_name):
    try:
        os.mkdir(directory_name)
    except OSError:
        print("Can't create diretory with path: " + directory_name)
        return -1
    os.mkdir(directory_name + 'lists\\')
    with open(directory_name + 'Path.txt', 'w') as path:
        path.write(directory_name)

    with open(directory_name + 'User_name.txt', 'w') as username:
        username.write(user_name)
    create_csv(directory_name)
    dowload_memes(directory_name)
    download_celebrations(directory_name)

main(directory_name, user_name)
