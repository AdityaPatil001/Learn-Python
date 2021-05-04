employee_file = open("Employeees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()