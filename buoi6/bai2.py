customer = {
    "name": "Minh",
    "email": "minh@gmail.com"
}

print(customer.get("email"))
if(not customer.get("phone")):
    print("Chưa có số điện thoại")