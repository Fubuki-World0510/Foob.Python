# Tạo List (Array)
name = ["Shirakami Fubuki", "Natsuiro Matsuri", "Gawr Gura"]
print(name[0]) # Out: Shirakami Fubuki

# Lấy list con
print(name[0:1]) # Out: ["Shirakami Fubuki", "Natsuiro Matsuri"]

# Sửa dữ liệu trong list
## Cập nhật
name[1] = "Kon Kon" # Out: ["Shirakami Fubuki", "Kon Kon", "Gawr Gura"]

## Xóa
del name[1] # Out: ["Shirakami Fubuki", "Gawr Gura"]

## Lồng các list
op = [99, 7389, "REAL", name] # Out: [99, 7389, "REAL", ["Shirakami Fubuki", "Natsuiro Matsuri", "Gawr Gura"]]

## CD vào list bị lồng
print(op[3][0]) # Out: Shirakami Fubuki