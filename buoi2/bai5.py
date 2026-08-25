username = "admin"
password = "123456"

inputUserName = input("Nhập tên tài khoản: ")
inputPassword = input("Nhập mật khẩu: ")

if(inputUserName == username and inputPassword == password):
    print("\nĐăng nhập thành công")
elif(inputUserName != username or inputPassword != password):
    print("\nĐăng nhập thất bại")