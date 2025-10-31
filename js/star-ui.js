/* ===================================
   Star-UI 交互逻辑
   =================================== */

// ===== 等待 DOM 加载完成 =====
document.addEventListener('DOMContentLoaded', function() {
  initSmoothScroll();
  initScrollAnimations();
  initVideoHoverEffects();
  initMobileMenu();
});

// ===== Lenis 平滑滚动初始化 =====
function initSmoothScroll() {
  if (typeof Lenis !== 'undefined') {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smooth: true,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    // 锚点平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId !== '#') {
          e.preventDefault();
          const target = document.querySelector(targetId);
          if (target) {
            lenis.scrollTo(target, { offset: -80 });
          }
        }
      });
    });
  }
}

// ===== 滚动动画（Intersection Observer）=====
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        // 可选：只动画一次就取消观察
        // observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // 观察所有带 data-animate 属性的元素
  document.querySelectorAll('[data-animate]').forEach(el => {
    observer.observe(el);
  });
}

// ===== 视频悬浮自动播放 =====
function initVideoHoverEffects() {
  const videoElements = document.querySelectorAll('[data-hover-video]');

  videoElements.forEach(container => {
    const video = container.querySelector('video');
    if (!video) return;

    // 确保视频静音（允许自动播放）
    video.muted = true;
    video.loop = true;

    container.addEventListener('mouseenter', () => {
      video.play().catch(err => console.log('视频播放失败:', err));
    });

    container.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0; // 可选：重置到开头
    });
  });
}

// ===== 移动端菜单 =====
function initMobileMenu() {
  // 创建汉堡菜单按钮（如果不存在）
  const navbar = document.querySelector('.navbar-content');
  if (!navbar) return;

  let menuBtn = navbar.querySelector('.mobile-menu-btn');
  if (!menuBtn) {
    menuBtn = document.createElement('button');
    menuBtn.className = 'mobile-menu-btn';
    menuBtn.innerHTML = `
      <span></span>
      <span></span>
      <span></span>
    `;
    menuBtn.setAttribute('aria-label', '菜单');
    navbar.appendChild(menuBtn);
  }

  const menu = navbar.querySelector('.navbar-menu');
  if (!menu) return;

  menuBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    menuBtn.classList.toggle('active');
    document.body.classList.toggle('menu-open');
  });

  // 点击菜单项后关闭菜单
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('active');
      menuBtn.classList.remove('active');
      document.body.classList.remove('menu-open');
    });
  });
}

// ===== 工具函数：节流 =====
function throttle(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// ===== 导航栏滚动效果 =====
window.addEventListener('scroll', throttle(() => {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  if (window.scrollY > 100) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}, 100));

// ===== 星空背景生成（可选）=====
function createStarField(container) {
  const starCount = 50;
  for (let i = 0; i < starCount; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.cssText = `
      position: absolute;
      width: ${Math.random() * 3}px;
      height: ${Math.random() * 3}px;
      background: white;
      border-radius: 50%;
      top: ${Math.random() * 100}%;
      left: ${Math.random() * 100}%;
      opacity: ${Math.random()};
      animation: twinkle ${2 + Math.random() * 3}s infinite;
    `;
    container.appendChild(star);
  }
}

// 为所有 .stars-bg 元素创建星空
document.querySelectorAll('.stars-bg').forEach(createStarField);
