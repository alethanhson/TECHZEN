<template>
  <MainLayout>
    <!-- Hero Section -->
    <section class="hero-section py-5 overflow-hidden position-relative">
      <div class="container py-lg-5">
        <div class="row align-items-center g-5">
          <div class="col-lg-6 animate-fade-in">
            <TBadge variant="primary" pill class="mb-3 px-3 py-2 fw-bold text-uppercase tracking-wider">
              Hệ thống ôn thi 2026
            </TBadge>
            <h1 class="display-3 fw-bold mb-4 tracking-tight">
              Sẵn sàng cho kỳ thi <span class="text-gradient">Techzen.</span>
            </h1>
            <p class="lead text-muted mb-5 pe-lg-5">
              Nền tảng quản lý và thực hành chuyên sâu dành cho Fresher Developer. Hãy bắt đầu hành trình của bạn ngay hôm nay.
            </p>
            <div class="d-flex flex-wrap gap-3">
              <TButton size="lg" gradient @click="$router.push('/products')">
                <i class="bi bi-rocket-takeoff-fill me-2"></i> Vào thi ngay
              </TButton>
              <TButton size="lg" variant="outline-primary" @click="scrollToSection('exam-info')">
                Xem lịch thi
              </TButton>
            </div>
          </div>
          <div class="col-lg-6 position-relative">
            <div class="hero-visual animate-float">
              <TCard class="glass-card p-4 border-0">
                <div class="d-flex align-items-center gap-3 mb-4">
                  <TAvatar src="https://api.dicebear.com/7.x/avataaars/svg?seed=Ngoc" size="56px" />
                  <div>
                    <h6 class="mb-0 fw-bold">Bảo Ngọc</h6>
                    <small class="text-muted">Bộ phận Nhân sự - Techzen</small>
                  </div>
                </div>
                <TAlert variant="info" class="mb-0">
                  Chào mừng bạn tham gia bài test chuyên môn vào 08:00 sáng mai!
                </TAlert>
              </TCard>
              
              <!-- Decorative elements -->
              <div class="blob-1"></div>
              <div class="blob-2"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="py-5 bg-white border-top border-bottom border-light">
      <div class="container py-4">
        <div class="row g-4 text-center">
          <div class="col-md-3 col-6">
            <h3 class="fw-bold mb-1">100+</h3>
            <p class="text-muted small mb-0">Ứng viên tham gia</p>
          </div>
          <div class="col-md-3 col-6">
            <h3 class="fw-bold mb-1">VUE 3</h3>
            <p class="text-muted small mb-0">Framework cốt lõi</p>
          </div>
          <div class="col-md-3 col-6">
            <h3 class="fw-bold mb-1">FASTAPI</h3>
            <p class="text-muted small mb-0">Hệ thống Backend</p>
          </div>
          <div class="col-md-3 col-6">
            <h3 class="fw-bold mb-1">BOOTSTRAP</h3>
            <p class="text-muted small mb-0">Giao diện Atomic</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Exam Info Section -->
    <section id="exam-info" class="py-5 mt-5">
      <div class="container">
        <div class="text-center mb-5">
          <h2 class="fw-bold h1">Thông tin chi tiết kỳ thi</h2>
          <p class="text-muted">Chi tiết lịch thi và yêu cầu kỹ thuật dành cho ứng viên</p>
        </div>
        
        <div class="row g-4 justify-content-center">
          <div class="col-lg-4">
            <TCard class="h-100 text-center border-0 shadow-soft">
              <div class="icon-circle bg-primary-soft text-primary mx-auto mb-4">
                <i class="bi bi-clock-fill"></i>
              </div>
              <h5 class="fw-bold mb-3">Thời gian</h5>
              <p class="text-muted">08:00 - 12:00<br>Ngày 02/04/2026</p>
            </TCard>
          </div>
          <div class="col-lg-4">
            <TCard class="h-100 text-center border-0 shadow-soft">
              <div class="icon-circle bg-success-soft text-success mx-auto mb-4">
                <i class="bi bi-geo-alt-fill"></i>
              </div>
              <h5 class="fw-bold mb-3">Địa điểm</h5>
              <p class="text-muted">06 Trần Phú, Hải Châu<br>Đà Nẵng (Tầng 3)</p>
            </TCard>
          </div>
          <div class="col-lg-4">
            <TCard class="h-100 text-center border-0 shadow-soft">
              <div class="icon-circle bg-info-soft text-info mx-auto mb-4">
                <i class="bi bi-hdd-network-fill"></i>
              </div>
              <h5 class="fw-bold mb-3">Yêu cầu BE/FE</h5>
              <p class="text-muted">Vue.js / ReactJS<br>Java / Python / Node.js</p>
            </TCard>
          </div>
        </div>
      </div>
    </section>

    <!-- Modules Grid -->
    <section class="py-5 mb-5">
      <div class="container">
        <div class="d-flex justify-content-between align-items-end mb-4">
          <div>
            <h2 class="fw-bold mb-1">Các Module bài tập</h2>
            <p class="text-muted mb-0">Các phần thực hành CRUD quan trọng</p>
          </div>
          <TButton variant="link" class="text-decoration-none fw-bold" @click="$router.push('/products')">
            Xem tất cả <i class="bi bi-arrow-right ms-2"></i>
          </TButton>
        </div>
        
        <div class="row g-4">
          <div class="col-md-6">
            <TCard class="p-4 border-0 bg-white hover-up" @click="$router.push('/products')">
              <div class="d-flex gap-4">
                <div class="p-3 bg-primary-soft text-primary rounded-4 height-auto">
                  <i class="bi bi-box-seam h2"></i>
                </div>
                <div>
                  <h4 class="fw-bold mb-2">Quản lý Sản phẩm</h4>
                  <p class="text-muted small">Thực hành các thao tác thêm, sửa, xóa và truy vấn với API chuẩn RESTful.</p>
                  <TBadge variant="primary" class="me-2">Priority</TBadge>
                  <TBadge variant="light">CRUD</TBadge>
                </div>
              </div>
            </TCard>
          </div>
          <div class="col-md-6">
            <TCard class="p-4 border-0 bg-white opacity-75 grayscale cursor-not-allowed">
              <div class="d-flex gap-4">
                <div class="p-3 bg-secondary-soft text-secondary rounded-4 height-auto">
                  <i class="bi bi-people h2"></i>
                </div>
                <div>
                  <h4 class="fw-bold mb-2">Quản lý Nhân sự</h4>
                  <p class="text-muted small">Mô-đun mở rộng dành cho bài tập quản lý tài khoản và phân quyền.</p>
                  <TBadge variant="secondary">Upcoming</TBadge>
                </div>
              </div>
            </TCard>
          </div>
        </div>
      </div>
    </section>
  </MainLayout>
</template>

<script setup lang="ts">
import MainLayout from '@/layouts/MainLayout.vue'

const scrollToSection = (id: string) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped lang="scss">
.text-gradient {
  background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tracking-tight {
  letter-spacing: -0.05em;
}

.tracking-wider {
  letter-spacing: 0.1em;
}

.hero-section {
  padding-bottom: 8rem !important;
}

.hero-visual {
  z-index: 2;
  position: relative;
}

.glass-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.1);
  border-radius: 24px;
}

.blob-1, .blob-2 {
  position: absolute;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(46, 91, 255, 0.15) 0%, transparent 70%);
  z-index: -1;
  border-radius: 50%;
}

.blob-1 { top: -50px; right: -50px; }
.blob-2 { bottom: -100px; left: -50px; }

.shadow-soft {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
}

.icon-circle {
  width: 64px;
  height: 64px;
  border-radius: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

.bg-primary-soft { background-color: rgba(46, 91, 255, 0.1); }
.bg-success-soft { background-color: rgba(0, 201, 167, 0.1); }
.bg-info-soft { background-color: rgba(102, 16, 242, 0.1); }
.bg-secondary-soft { background-color: rgba(108, 117, 125, 0.1); }

.hover-up {
  transition: all 0.3s ease;
  cursor: pointer;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1) !important;
  }
}

.animate-fade-in {
  animation: fadeIn 1s ease-out;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.height-auto {
  height: fit-content;
}

.grayscale {
  filter: grayscale(1);
}

.cursor-not-allowed {
  cursor: not-allowed;
}
</style>
