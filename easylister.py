a_list = []

while True:
    s = input('Enter name: ')
    if not s:
        break  
    a_list.append(s)
a_list.sort()
print(a_list)


# just going to run how this works. for future reference
# you have an empty list

#The while loop sets up the environment for a loop
# you take an import and then append to a list
# the code then repeats
# If you don't input anything, then the code breaks and sorts the list
# Then the list is printed
