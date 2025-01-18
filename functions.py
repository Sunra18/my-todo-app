FILEPATH = "todo.txt"

def get_todos(filepath="todo.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todo.txt"):
    """ Write a to-do items list in the text file. """
    with open("todo.txt", "w") as file:
        file.writelines(todos_arg)

"""Making a block function that only executed in this file, but not executed 
when it imports as module on different file"""
if __name__ == "__main__":
    print("Hello")
    print(get_todos())