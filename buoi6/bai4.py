employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500],
}

for index in range(len(employees["name"])):
    print(
        f"{employees['name'][index]} - "
        f"{employees['department'][index]} - "
        f"{employees['salary'][index]}"
    )
