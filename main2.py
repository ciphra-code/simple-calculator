while True:
    print("=========Máy Tính=========")
    print()
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Bình phương")
    print("6. Kiểm tra chẵn lẻ")
    print("7. Giá trị tuyệt đối")
    print("0. Thoát")
    print()
    print("===========================")
    choice = int(input("Nhập tính năng:"))
    if choice == 1:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        print("Kết quả là:", a + b)
    elif choice == 2:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        print("Kết quả là:", a - b)
    elif choice == 3:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        print("Kết quả là: ", a * b)
    elif choice == 4:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        if b != 0:
            print("Kết quả là: ", a / b)
        else:
            print("Không thể chia hết cho 0")
    elif choice == 5:
        a = float(input("Nhập a: "))
        print("Kết quả là: ", a ** 2)
    elif choice == 6:
        a = int(input("Nhập a: "))
        if a % 2 == 0:
            print("Chẵn")
        else:
            print("Lẻ")
    elif choice == 7:
        a = float(input("Nhập a: "))
        print(abs(a))
    elif choice == 0:
        print("Thoát")
        break
    else:
        print("Lựa chọn không hợp lệ")