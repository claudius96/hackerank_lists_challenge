number_of_times = int(input('enter the number of time you wanna command '))
print(number_of_times)
def list_function(number_of_times):
    """This function is to be used for:
    1).INSERT i e: Insert integer  at position .
    2).PRINT: Print the list.
    3).REMOVE e: Delete the first occurrence of integer .
    4).APPEND e: Insert integer  at the end of the list.
    5).SORT: Sort the list.
    6).POP: Pop the last element from the list.
    7).REVERSE: Reverse the list.

"""
    instructions = []
    print('enter the COMMAND,POSITION,DESIRED_VALUE(NUMBER) in that order')
    for i in range(number_of_times):
        command = input().split()
        if command[0].lower() == 'insert':
            instructions.insert(int(command[1]),int(command[2]))
        if command[0].lower() == 'print':
            print(instructions)
        if command[0].lower() == 'remove':
            instructions.remove(int(command[1]))
        if command[0].lower() == 'append':
            instructions.append(int(command[1]))
        if command[0].lower() == 'sort':
            instructions.sort()
        if command[0].lower() == 'pop':
            instructions.pop()
        if command[0].lower() == 'reverse':
            instructions.reverse()
list_function(number_of_times)
        

