def xoa_truong(data, field):
    if field in data:
        return data.pop(field)
    return "Trường thông tin không tồn tại"


employee = {
    "name": "An",
    "department": "IT",
    "salary": 2000,
}

print(xoa_truong(employee, "department"))
print(xoa_truong(employee, "phone"))
