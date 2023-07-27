import ast
import json

def switchCase(action):
    if action == 1:
        name = input('Enter new name: ')
        if name in grade_dict.keys():
            print(f'{name} already exists')
        else:
            grade = float(input('Enter new grade: '))
            grade_dict[name] = grade

    elif action == 2 or action == 3 or action == 4:
        name = input('Enter the full name of student: ')
        if action == 2 and name in grade_dict.keys():
            print(f'{name}\'s grade is {grade_dict[name]}')

        elif action == 3 and name in grade_dict.keys():
            grade = float(input('Enter new grade: '))
            grade_dict[name] = grade

        elif action == 4 and name in grade_dict.keys():
            # del grade_dict[name]
            grade_dict.pop(name)

        else:
            print(f'No record of {name} or full name was not entered')
    else:
        print('You did not enter a valid action value')

# r+ for reading and overwriting any existing data
with open('grades.txt', 'r+') as file:
    # read file and convert to dictionary
    grade_dict = ast.literal_eval(file.read())

print("1 = create new name and grade")
print("2 = ask for a grade (given full name of student)")
print("3 = edit a grade (given full name of student)")
print("4 = delete a grade (given full name of student)\n")
action = int(input("Enter the number corresponding to your desired action: "))

switchCase(action)

with open('grades.txt', 'w') as file:
    json.dump(grade_dict, file, indent=3)


# 1 = create new name and grade
# 2 = user is asking for a grade (given full name of student)
# 3 = user wants to edit a grade
# 4 = user wants to delete a grade
# e.	Reads/writes to grades.txt to store grade data persistently in JSON format
    # use json.dump()
# f.	Stores grades in memory data as a dictionary and updates grades.txt with any changes
