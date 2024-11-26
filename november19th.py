#s/ and mode= are 'hints', not needed
# 'cd..' (goes down a directory) 'cd [folder_name/file_name]' (goes up a directory)
#when going through directory, use 'ls' to list the files, folders, users, etc
#when going through directory, 'rm [file_name]' deletes file
random_list: list(str) = ["cookies", "milk", "walmart", "Avengers", "Harry Potter"]

with open('random_list.py', 'w') as file:
    file.write("random_list = [\n")
    for item in random_list:
        file.write



#put new item in list
# random_list.insert([position]0, [new item]Oreos)
# print("Aftering inserting Oreos at position 1:", random_list)
