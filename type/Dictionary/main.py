# Tạo dictionary
dic = {
    'name': "Shirakami Fubuki",
    'Person o': 18,
    'my waifu?': True,
    'status': "REAL",
    'hus': {
        'name': "Foob"
    }
}
print(dic['my wifi?']) # Out: True


# Sửa dữ liệu dictionary
dic['status'] = "VERY TRUE"
print(dic['status']) # Out: VERY TRUE

# CD dictionary khi lồng
print(dic["hus"]["name"]) # Foob

# Xóa phần tử dữ liệu dictionary
del dic['status']
print(dic) # Out: {'name': "Shirakami Fubuki", 'Person o': 18, 'my waifu?': True}

# Xóa tất phần tử dictionary
dic.clear() # Out: {}

# Xóa toàn bộ dữ liệu biến
del dic # is not defined