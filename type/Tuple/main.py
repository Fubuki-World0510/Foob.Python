# Tạo tuple
text = ("Sug", "hi", "sug", "cuma")
no = (); # rỗng
no1 = (10, ) # Giá trị duy nhất

# CD vào tuple
print(text[0]) # Out: Sug

# Lấy dữ liệu tuple con
print(text[0:2]) # ("Sug", "hi")

# Sửa dữ liệu tuple
del text # is not defined

# Thêm dữ liệu
n = ("hú", "hi")
d = ("Real", "Nah")
print(n + d) # Out: ("hú", "hi", "Real", "Nah")

# Lồng tuple
n = ("hú", "hi", d)
print(n[2][0]) # Out: ("Real")