# JavaScript/ES6 Cheat Sheet for Vue 3 Development

Tập trung vào các cú pháp ES6 hay dùng nhất trong Vue 3 Composition API.

## 1. Biến & Destructuring (Phân rã)
```js
// Let/Const
const name = 'Son'; // Không thể gán lại
let age = 25; // Có thể gán lại

// Object Destructuring (Cực hay dùng trong Props/Emits)
const user = { id: 1, email: 'son@techzen.com', role: 'admin' };
const { email, role } = user; // Lấy email, role từ object user

// Array Destructuring
const [first, second] = [10, 20];

// Alias (Đổi tên khi destructure)
const { email: userEmail } = user; 
```

## 2. Spread & Rest Operator (`...`)
```js
// Copy Object/Array (Gộp dữ liệu)
const base = { id: 1 };
const updated = { ...base, name: 'New Name', active: true }; // { id: 1, name: 'New Name', active: true }

const list = [1, 2];
const newList = [...list, 3, 4]; // [1, 2, 3, 4]

// Rest Params (Lấy phần còn lại)
const { id, ...others } = user; // others = { email: ..., role: ... }
```

## 3. Array Methods (Cực kỳ quan trọng để xử lý List)
```js
const items = [{id: 1, val: 10}, {id: 2, val: 20}, {id: 3, val: 30}];

// .map() - Tạo mảng mới từ mảng cũ (thường dùng để format lại data)
const ids = items.map(item => item.id); // [1, 2, 3]

// .filter() - Lọc phần tử (thường dùng cho Search/Delete)
const highValues = items.filter(item => item.val > 15); // [{id: 2...}, {id: 3...}]

// .find() - Tìm 1 phần tử duy nhất
const item2 = items.find(item => item.id === 2); // {id: 2, val: 20}

// .some() / .every() - Kiểm tra điều kiện (trả về true/false)
const hasLarge = items.some(i => i.val > 25); // true

// .reduce() - Tính tổng hoặc gộp data
const total = items.reduce((sum, item) => sum + item.val, 0); // 60
```

## 4. Arrow Functions & Template Literals
```js
// Arrow Function (Ngắn gọn, không bind 'this')
const add = (a, b) => a + b;
const log = msg => console.log(msg);

// Template Literals (Nối chuỗi có biến)
const url = `${BASE_URL}/items/${id}?query=${q}`;
```

## 5. Async / Await (Xử lý API)
```js
const loadData = async () => {
  try {
    const res = await fetch('/api/data');
    const data = await res.json();
    return data;
  } catch (err) {
    console.error('Lỗi API:', err);
  }
}
```

## 6. Optional Chaining & Nullish Coalescing
```js
// Optional Chaining (?.) - Tránh lỗi "cannot read property of undefined"
const city = user?.address?.city; // Trả về undefined nếu address null, không báo lỗi

// Nullish Coalescing (??) - Gán giá trị mặc định nếu là null/undefined
const theme = user.pref?.theme ?? 'light'; 
// Khác với || ở chỗ: || sẽ lấy 'light' nếu theme là 0 hoặc chuỗi rỗng "", còn ?? chỉ lấy khi là null/undefined.
```
