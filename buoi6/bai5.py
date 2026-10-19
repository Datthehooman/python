employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500],
}

salary_by_department = {}

for index in range(len(employees["department"])):
    department = employees["department"][index]
    salary = employees["salary"][index]

    if department not in salary_by_department:
        salary_by_department[department] = 0
    salary_by_department[department] += salary

print(salary_by_department)
