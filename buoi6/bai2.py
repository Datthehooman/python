customer = {
    "name": "Minh",
    "email": "minh@gmail.com",
}

print(customer.get("email"))

phone = customer.get("phone")
if phone is None:
    print("Chưa có số điện thoại")
else:
    print(phone)
