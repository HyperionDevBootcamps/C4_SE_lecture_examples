while True:
    try:
        selection = input("Please provide a file name: ")
        if not ".txt" in selection:
            selection += ".txt"
        file = open(selection, "r")
        content = file.read()
        print("File content: \n" + content)
        break
    except FileNotFoundError:
        print("File Error")


































# try:
#     file = open(selection, "r")
#     content = file.read()
#     print("File content: \n" + content)
# except FileNotFoundError:
#     print("No such file")













# import os
# if os.path.isfile(selection):
#     file = open("./"+selection, "r")
#     content = file.read()
#     print("File content: \n" + content)
# else:
#     print("No such file")