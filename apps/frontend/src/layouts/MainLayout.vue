<template>
  <div class="main-layout min-vh-100 d-flex flex-column bg-light">
    <!-- Header -->
    <TNavbar sticky="top" variant="white">
      <div class="container d-flex justify-content-between align-items-center">
        <TNavbarBrand class="d-flex align-items-center gap-2">
          <div class="icon-box bg-primary text-white rounded p-1">
             <i class="bi bi-rocket-takeoff-fill"></i>
          </div>
          TECHZEN TEST
        </TNavbarBrand>
        
        <div class="d-flex gap-3 align-items-center">
          <TLink href="#" class="text-dark">Trang chủ</TLink>
          <TLink href="#" class="text-dark">Quản lý</TLink>
          <TAvatar src="https://api.dicebear.com/7.x/avataaars/svg?seed=Son" size="38px" />
        </div>
      </div>
    </TNavbar>

    <!-- Main Content -->
    <main class="container py-5 flex-grow-1">
       <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-white border-top py-4 mt-auto">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-6 text-center text-md-start">
            <span class="text-muted small">© 2026 Techzen Education - Exam Preparation System</span>
          </div>
          <div class="col-md-6 text-center text-md-end">
            <TBadge variant="primary" pill>Student ID: 123456</TBadge>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.icon-box {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.main-layout {
  font-family: 'Inter', sans-serif;
}
</style>
