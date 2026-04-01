# Python Data & JSON Operations Cheat Sheet

Tập trung vào các thao tác xử lý Object, Dict, List và JSON trong Python 3.10+.

## 1. Dictionary (Dict) - Kiểu dữ liệu chính để quản lý data
```python
# Khởi tạo
user = {"id": 1, "name": "Son", "email": "son@techzen.com"}

# Lấy giá trị (Nên dùng .get() để tránh báo lỗi nếu Key không tồn tại)
name = user.get("name") # "Son"
phone = user.get("phone", "N/A") # "N/A" (Gán giá trị mặc định)

# Thêm/Cập nhật
user["role"] = "admin"
user.update({"active": True, "token": "abc"})

# Gộp (Merge) 2 Dictionary (Python 3.9+)
extra = {"theme": "dark"}
full_user = user | extra

# Xóa Key
del user["token"] # Báo lỗi nếu Key ko có
deleted_val = user.pop("role", None) # Ko báo lỗi, lấy ra đc value 'admin'

# List keys/values
keys = list(user.keys()) # ["id", "name", ...]
values = list(user.values()) # [1, "Son", ...]
items = list(user.items()) # [("id", 1), ("name", "Son"), ...]
```

## 2. List Operations (Mảng)
```python
# Thêm phần tử
items = [1, 2]
items.append(3) # [1, 2, 3]
items.extend([4, 5]) # [1, 2, 3, 4, 5] (Gộp mảng khác vào)

# List Comprehension (Cực kỳ mạnh mẽ để filter/map data)
data = [10, 20, 30, 40]
doubled = [x * 2 for x in data] # [20, 40, 60, 80]
filtered = [x for x in data if x > 25] # [30, 40]
```

## 3. JSON Handling (Xử lý chuỗi JSON)
```python
import json

# JSON String -> Python Dict (.loads = Load String)
json_str = '{"id": 1, "name": "Son", "active": true}'
user_dict = json.loads(json_str) # Boolean true thành True (Python)

# Python Dict/List -> JSON String (.dumps = Dump String)
# indent=4: Format đẹp (Pretty Print)
# ensure_ascii=False: Hiển thị đúng tiếng Việt
json_output = json.dumps(user_dict, indent=4, ensure_ascii=False)

# File JSON (.load / .dump - Không có 's')
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

## 4. Pydantic v2 (Xử lý Object nâng cao trong FastAPI)
```python
from pydantic import BaseModel
class User(BaseModel):
    id: int; name: str

# Schema object -> Dict
user_obj = User(id=1, name="Son")
user_dict = user_obj.model_dump() # NEW in Pydantic v2
user_json = user_obj.model_dump_json()

# Dict -> Schema object
new_user = User(**user_dict)
```

## 5. String Tricks (Format & Slicing)
```python
# F-String (Interpolation)
name = "Son"; age = 25
msg = f"Chào {name}, bạn {age} tuổi."

# Join list (Nối mảng thành chuỗi)
tags = ["python", "fastapi", "vue"]
tag_str = ", ".join(tags) # "python, fastapi, vue"

# Split string (Cắt chuỗi thành mảng)
email = "son@techzen.com"
username = email.split("@")[0] # "son"
```

## 6. Sắp xếp (Sorting)
```python
# Sắp xếp List Objects theo Key cụ thể
items = [
    {"id": 3, "val": 10},
    {"id": 1, "val": 50},
    {"id": 2, "val": 30}
]

# Sắp xếp tăng dần theo val
sorted_items = sorted(items, key=lambda x: x["val"])
# Sắp xếp giảm dần theo val
sorted_desc = sorted(items, key=lambda x: x["val"], reverse=True)
```
