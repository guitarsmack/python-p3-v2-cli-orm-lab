from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)
    pass


def find_employee_by_name():
    name = input("Enter employee's name: ")
    if employee := Employee.find_by_name(name):
        print(employee)
    else:
        print(f"Employee {name} not found.")
    pass


def find_employee_by_id():
    id_ = input("Enter employee's ID: ")
    if employee := Employee.find_by_id(id_):
        print(employee)
    else:
        print(f"Employee {id_} not found.")


def create_employee():
    name = input("Employee name: ")
    job_title = input("Employee job: ")
    department_id = int(input("Department ID: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Exception: ", exc)


def update_employee():
    id_ = int(input("Employee to update: "))
    if employee := Employee.find_by_id(id_):
        try:
            employee.name = input("New name: ")
            employee.job_title = input("New job: ")
            employee.update()
            print(f'Employee updated: {employee.name}')
        except Exception as exc:
            print("Exception error: ", exc)
    else:
        print(f'Employee {id_} not found')
    pass


def delete_employee():
    id_ = int(input("Employee to update: "))
    if employee := Employee.find_by_id(id_):
        try:
            employee.delete()
            print(f'Employee deleted: {employee.name}')
        except Exception as exc:
            print("Exception error: ", exc)
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    id_ = int(input("Department to employees: "))
    if department := Department.find_by_id(id_):
        try:
            employees = department.employees()
            for employee in employees:
                print(employee)
        except Exception as exc:
            print('Exception: ', exc)
    else:
        print(f'Dempartment {id_} does not exist')

    