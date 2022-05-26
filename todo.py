import sys
from pathlib import Path

home_dir = str(Path.home())

filePath = home_dir + "/todo.txt"

todo_list = []
try:
    file = open(filePath,"r+")
except:
    file = open(filePath, "w+")

for line in file:
    todo_list.append(line[0:len(line)-1])



def printTodoList(todo_list):
    counter = 1
    print("to do:")
    for task in todo_list:
        print("[%s] " %counter + task)
        counter += 1

def addTaskToList(todo_list, task):
    todo_list.append(task)
    file.writelines(task + "\n")

def removeFromList(todo_list, taskNumber):
    counter = 1
    for task in todo_list:
        if counter == taskNumber:
            todo_list.remove(task)
            removeLineFromFile(file, taskNumber)
        counter += 1

def removeLineFromFile(file, lineToRemove):
    with open(filePath, "r") as read_file:
        lines = read_file.readlines()
    currentLine = 1
    with open(filePath, "w") as write_file:
        for line in lines:
            if currentLine == lineToRemove:
                pass
            else:
                write_file.write(line)
            currentLine += 1

if len(sys.argv) == 1:
    print("""params: 'add [task]' (use quotes for multiple words)
        'remove [number of task]' 
        'list'""")
    choice = ""
    task = ""

if len(sys.argv) == 2:
    choice = str(sys.argv[1])

if len(sys.argv) == 3:
    choice = str(sys.argv[1])
    task = str(sys.argv[2])

if choice == "add":
    addTaskToList(todo_list, task)
    printTodoList(todo_list)

if choice == "remove":
    removeFromList(todo_list, int(task))
    printTodoList(todo_list)

if choice == "list":
    printTodoList(todo_list)

file.close()
#print(todo_list)
print()
