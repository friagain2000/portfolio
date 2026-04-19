/**
 * SHIN SEONG MIN Portfolio - Optimized Script
 */

gsap.registerPlugin(ScrollTrigger);

const EASE_OUT = "power3.out";

/* ---------- Hero: 정적 요소 등장 ---------- */
gsap.timeline({ delay: 0.2 }).from(".hero-desc", { y: 30, opacity: 0, duration: 1.2, ease: EASE_OUT }).from(".hero-btns", { y: 30, opacity: 0, duration: 1.2, ease: EASE_OUT }, "-=0.9").to(".scroll-indicator", { opacity: 1, y: 0, duration: 1, ease: "power2.out" }, "-=0.5");

/* ---------- Hero: 무한 루프 텍스트 ---------- */
(() => {
  const heroTexts = [
    ["태도는", "디자인은"],
    ["MAXIMUM", "MINIMUM"],
  ];
  const ani1 = document.querySelector(".ani1");
  const max = document.querySelector(".max");

  if (!ani1 || !max) return;

  let index = 0;
  let timeline;
  let split1, split2;

  const play = () => {
    timeline?.kill();
    split1?.revert();
    split2?.revert();
    
    ani1.textContent = heroTexts[0][index];
    max.textContent = heroTexts[1][index];
    
    ani1.style.marginRight = "15px";

    split1 = new SplitType(ani1, { types: "chars" });
    split2 = new SplitType(max, { types: "chars" });

    timeline = gsap.timeline({
      onComplete: () => {
        index = (index + 1) % heroTexts[0].length;
        play();
      },
    });

    gsap.set([split1.chars, split2.chars], { y: 50, opacity: 0, rotationX: -30, transformOrigin: "50% 50% -50" });

    timeline
      .to(split1.chars, {
        y: 0,
        opacity: 1,
        rotationX: 0,
        duration: 0.8,
        ease: "power4.out",
        stagger: 0.03
      })
      .to(split2.chars, {
        y: 0,
        opacity: 1,
        rotationX: 0,
        duration: 1,
        ease: "expo.out",
        stagger: 0.04
      }, "-=0.4")
      .addLabel("out", "+=2.5")
      .to(split1.chars, {
        y: -30,
        opacity: 0,
        duration: 0.6,
        ease: "power2.in",
        stagger: 0.02
      }, "out")
      .to(split2.chars, {
        y: -30,
        opacity: 0,
        duration: 0.6,
        ease: "power2.in",
        stagger: 0.02
      }, "out+=0.1");
  };

  play();
})();

/* ---------- 섹션 제목 문자 단위 리빌 ---------- */
document.querySelectorAll(".pf-section-title").forEach((title) => {
  const split = new SplitType(title, { types: "chars" });
  gsap.from(split.chars, {
    scrollTrigger: { trigger: title, start: "top 80%" },
    y: 30,
    opacity: 0,
    duration: 1,
    stagger: 0.02,
    ease: EASE_OUT,
  });
});
/* ---------- 공통 Reveal 애니메이션 ---------- */
document.querySelectorAll(".reveal, .reveal-toss").forEach((el) => {
  const delay = el.dataset.delay || "0";
  el.style.transitionDelay = `${delay}s`;
  
  ScrollTrigger.create({
    trigger: el,
    start: "top 85%",
    onEnter: () => {
      el.classList.add("active");
      el.querySelectorAll(".progress-fill").forEach((bar) => {
        const percent = bar.dataset.percent;
        if (percent) bar.style.width = percent;
      });
    },
  });
});

/* ---------- 헤더 스크롤 축소 ---------- */
const header = document.querySelector("#main-header");
const gnbNav = document.querySelector(".gnb-nav");
if (header && gnbNav) {
  ScrollTrigger.create({
    start: "top -20",
    onUpdate: () => {
      const scrolled = window.scrollY > 20;
      header.classList.toggle("py-6", !scrolled);
      header.classList.toggle("py-2", scrolled);
      gnbNav.classList.toggle("shadow-sm", scrolled);
      gnbNav.classList.toggle("mx-4", scrolled);
    },
  });
}

/* ---------- 로고 클릭 시 최상단 스크롤 ---------- */
document.querySelector(".logo")?.addEventListener("click", (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

/* ---------- Lamp 둥둥 애니메이션 ---------- */
gsap.to(".lamp", {
  y: 170,
  duration: 2,
  ease: "sine.inOut",
  repeat: -1,
  yoyo: true,
});

ScrollTrigger.refresh();
