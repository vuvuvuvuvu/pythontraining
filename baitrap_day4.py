# 1 tạo 1 list film
list_fimls = ["hihi", "hoho", "hahaha ", "ohohoho", "ahahaha"]
print("Danh sach bo phim la %s " % (list_fimls))

# 2 Sd hàm input nhập vào 1 bộ phim
new_movies = input("nhap vao bo phim moi coi : ")

# 3 Thêm bộ phim mới đó vào cuối danh sách
list_fimls.append(new_movies)

# 4 in ra phim đầu , cuối và giữa của list

print("Bộ phim đầu tiên là ", list_fimls[0])
print("Bộ phim cuoi cung là ", list_fimls[-1])
print("Bộ phim o giua  là ", list_fimls[len(list_fimls) // 2])

# 5 Đếm số lượng bộ phim có trong list
amount = len(list_fimls)
print("so luong bo phim co trong list la : ", amount)

# 6 Xóa bộ phim đầu và bộ phim cuối trong list
del list_fimls[0]
del list_fimls[-1]
print(list_fimls)

# 7 lấy ra và xóa bộ phim cuối cùng trong list
list_fimls.pop()

# 8 chèn 1 bộ phim bất ky vào đầu danh sách
list_fimls.insert(0, "phim hihi")
print(list_fimls)
