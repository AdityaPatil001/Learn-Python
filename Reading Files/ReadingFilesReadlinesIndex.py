employee_file = open("Employeees.txt", "r")
print(employee_file.readlines()[0])
employee_file.close()