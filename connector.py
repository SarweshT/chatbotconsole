# Approach 1 :
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="user",
    passwd ="password"
)

print(dataBase)

# Disconnecting from the server
dataBase.close()

# Approach 2 :
employees = [
    {'name': 'John', 'age': 30},
    {'name': 'Mary', 'age': 25},
    {'name': 'Bob', 'age': 40},
    {'name': 'Jane', 'age': 45}
]

file = open('employees.txt', "a")

for employee in employees:
    string = "{name}||{age}\n".format(**employee)

    file.write(string)

file.close()
