product = {
    "id": 1,
    "name": "Laptop",
    "price": 15000000,
    "quantity": 10,
}

# 1. In tên sản phẩm
print(product["name"])

# 2. Đổi giá
product["price"] = 14000000
print(product["price"])

# 3. Thêm category
product["category"] = "Điện tử"
print(product["category"])

# 4. Xóa quantity
del product["quantity"]

# 5. In product
print(product)
