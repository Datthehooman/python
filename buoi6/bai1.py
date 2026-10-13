product = {
    "id": 1,
    "name": "dat",
    "price": 100,
    "quantity": 5
}

#1. In tên
print(product["name"])

#2. Đổi giá
product["price"] = 200
print(product["price"])

#3. thêm category
product["category"] = "sinh vien"
print(product["category"])

#4. Xóa quantity
del product["quantity"]

#5. In product
print(product)