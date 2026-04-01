# Bootstrap 5 & BootstrapVueNext Cheat Sheet

## 1. Bootstrap 5 Utility Classes
### Layout & Grid
- **Containers**: `.container`, `.container-fluid`
- **Rows & Columns**:
  ```html
  <div class="row">
    <div class="col-md-6 col-lg-4">Responsive Column</div>
    <div class="col-12 px-2 py-4">Full Width with padding</div>
  </div>
  ```
- **Flexbox**: `.d-flex`, `.flex-column`, `.justify-content-center`, `.align-items-center`, `.flex-grow-1`

### Spacing (m = margin, p = padding)
- **Format**: `{property}{side}-{size}`
- **Property**: `m`, `p`
- **Side**: `t` (top), `b` (bottom), `s` (start/left), `e` (end/right), `x` (left & right), `y` (top & bottom)
- **Size**: `0` to `5`, `auto`
- **Example**: `mt-3`, `px-2`, `me-auto`

### Colors & Typography
- **Text Color**: `.text-primary`, `.text-secondary`, `.text-success`, `.text-danger`, `.text-warning`, `.text-info`, `.text-light`, `.text-dark`, `.text-muted`, `.text-white`
- **Background**: `.bg-primary`, `.bg-dark`, `.bg-transparent`
- **Text Alignment**: `.text-start`, `.text-center`, `.text-end`, `.text-nowrap`
- **Text Size**: `.h1` to `.h6`, `.lead`, `.small`, `.fw-bold`, `.fst-italic`

### Sizing
- **Width**: `.w-25`, `.w-50`, `.w-75`, `.w-100`, `.vw-100`
- **Height**: `.h-25`, `.h-50`, `.h-75`, `.h-100`, `.vh-100`

---

## 2. BootstrapVueNext Components
### 1. Simple Card
```vue
<BLink to="/profile">
  <BCard title="User Profile" sub-title="Details">
    <BCardText>
        Welcome to Techzen Platform.
    </BCardText>
    <BButton variant="primary">Confirm</BButton>
  </BCard>
</BLink>
```

### 2. Form & Inputs
```vue
<BForm @submit.prevent="handleSubmit">
  <BFormGroup label="Email address:" label-for="email-input">
    <BFormInput id="email-input" v-model="form.email" type="email" placeholder="example@email.com" required />
  </BFormGroup>
  
  <BFormGroup label="Role:" class="mt-3">
    <BFormSelect v-model="form.role" :options="roleOptions" />
  </BFormGroup>
  
  <BFormCheckbox v-model="form.terms" class="mt-2">I accept terms</BFormCheckbox>
</BForm>
```

### 3. Data Tables
```vue
<BTable 
  :items="items" 
  :fields="fields" 
  striped 
  hover 
  responsive
>
  <!-- Custom Cell Slot -->
  <template #cell(actions)="{ item }">
    <BButton size="sm" variant="info" class="me-1">View</BButton>
    <BButton size="sm" variant="danger" @click="handleDelete(item.id)">Delete</BButton>
  </template>
</BTable>

<script setup>
const fields = [
  { key: 'name', sortable: true },
  { key: 'email', sortable: false },
  { key: 'actions', label: 'Operations' }
]
const items = [{ id: 1, name: 'Alice', email: 'alice@email.com' }]
</script>
```

### 4. Modals
```vue
<BButton @click="showModal = true">Open Modal</BButton>

<BModal v-model="showModal" title="Confirm Action" @ok="handleOk">
  Are you sure you want to proceed?
</BModal>

<script setup>
const showModal = ref(false)
const handleOk = () => { /* Logic */ }
</script>
```

### 5. Toast Notifications
```vue
<script setup>
import { useToast } from 'bootstrap-vue-next'
const toast = useToast()

const notify = () => {
  toast.show({ body: 'Saved successfully!', variant: 'success' })
}
</script>
```

### 6. Badges & Pills
```html
<BBadge variant="primary">New</BBadge>
<BBadge pill variant="danger">High</BBadge>
```

### 7. Spinners (Loading)
```html
<BSpinner label="Loading..." variant="primary" small />
<BSpinner type="grow" label="Spinning" />
```

### 8. Dropdowns
```vue
<BDropdown text="Actions" variant="outline-primary">
  <BDropdownItem @click="editItem">Edit</BDropdownItem>
  <BDropdownItem @click="deleteItem" variant="danger">Delete</BDropdownItem>
  <BDropdownDivider />
  <BDropdownItem disabled>Archive</BDropdownItem>
</BDropdown>
```
