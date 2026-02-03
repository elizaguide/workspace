# CTA Section Patterns

## Table of Contents
1. [Gradient CTA](#gradient-cta) - Purple gradient, high impact
2. [Dark CTA](#dark-cta) - Dark background, dramatic
3. [Light CTA](#light-cta) - White/lavender, subtle
4. [CTA with Image](#cta-with-image) - Split layout
5. [Sticky CTA Bar](#sticky-cta-bar) - Fixed bottom bar
6. [Inline CTA](#inline-cta) - Mid-page conversion point

---

## Gradient CTA

Best for: Final call-to-action, high urgency.

```html
<section style="background: linear-gradient(135deg, #7a12d4 0%, #5b0fa8 50%, #3d0a70 100%); padding: 5rem 0;">
  <div class="mv-container">
    <div style="max-width: 40rem; margin: 0 auto; text-align: center;">
      <h2 class="title-bold-2" style="color: white; margin-bottom: 1rem;">
        {{HEADLINE}}
      </h2>

      <p class="body-lg" style="color: rgba(255, 255, 255, 0.9); margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 1.25rem 2.5rem;
        background: white;
        color: #7a12d4;
        font-weight: 600;
        font-size: 18px;
        border-radius: 999px;
        text-decoration: none;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s, box-shadow 0.2s;
      " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.3)';"
         onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.2)';">
        {{CTA_TEXT}}
      </a>

      <p class="body-sm" style="color: rgba(255, 255, 255, 0.7); margin-top: 1.5rem;">
        {{GUARANTEE_TEXT}}
      </p>
    </div>
  </div>
</section>
```

---

## Dark CTA

Best for: Premium feel, dramatic close.

```html
<section style="background: #0f131a; padding: 5rem 0;">
  <div class="mv-container">
    <div style="max-width: 40rem; margin: 0 auto; text-align: center;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        {{EYEBROW}}
      </p>

      <h2 class="title-bold-2" style="color: white; margin-bottom: 1rem;">
        {{HEADLINE}}
      </h2>

      <p class="body-lg" style="color: #9ca3af; margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 1.25rem 2.5rem;
        background: #7a12d4;
        color: white;
        font-weight: 600;
        font-size: 18px;
        border-radius: 999px;
        text-decoration: none;
        box-shadow: 0 4px 16px rgba(122, 18, 212, 0.4);
        transition: transform 0.2s, box-shadow 0.2s;
      " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(122,18,212,0.5)';"
         onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 16px rgba(122,18,212,0.4)';">
        {{CTA_TEXT}}
      </a>

      <p class="body-sm" style="color: #6b7280; margin-top: 1.5rem;">
        {{GUARANTEE_TEXT}}
      </p>
    </div>
  </div>
</section>
```

---

## Light CTA

Best for: Soft close, less aggressive.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="max-width: 40rem; margin: 0 auto; text-align: center;">
      <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 1rem;">
        {{HEADLINE}}
      </h2>

      <p class="body-lg" style="color: #4b5563; margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
        <a href="{{CTA_URL}}" class="button" style="
          display: inline-flex;
          align-items: center;
          justify-content: center;
          padding: 1rem 2rem;
          background: #7a12d4;
          color: white;
          font-weight: 600;
          border-radius: 999px;
          text-decoration: none;
        ">{{CTA_TEXT}}</a>

        <a href="{{SECONDARY_URL}}" class="button" style="
          display: inline-flex;
          align-items: center;
          justify-content: center;
          padding: 1rem 2rem;
          background: transparent;
          color: #7a12d4;
          font-weight: 500;
          border-radius: 999px;
          border: 2px solid #7a12d4;
          text-decoration: none;
        ">{{SECONDARY_TEXT}}</a>
      </div>

      <p class="body-sm" style="color: #6b7280; margin-top: 1.5rem;">
        {{GUARANTEE_TEXT}}
      </p>
    </div>
  </div>
</section>
```

---

## CTA with Image

Best for: Visual reinforcement, product showcase.

```html
<section style="background: linear-gradient(135deg, #7a12d4 0%, #5b0fa8 100%); padding: 5rem 0;">
  <div class="mv-container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
      <!-- Text Column -->
      <div>
        <h2 class="title-bold-2" style="color: white; margin-bottom: 1rem;">
          {{HEADLINE}}
        </h2>

        <p class="body-lg" style="color: rgba(255, 255, 255, 0.9); margin-bottom: 2rem;">
          {{SUBHEADLINE}}
        </p>

        <a href="{{CTA_URL}}" class="button" style="
          display: inline-flex;
          padding: 1.25rem 2.5rem;
          background: white;
          color: #7a12d4;
          font-weight: 600;
          font-size: 18px;
          border-radius: 999px;
          text-decoration: none;
        ">{{CTA_TEXT}}</a>

        <p class="body-sm" style="color: rgba(255, 255, 255, 0.7); margin-top: 1.5rem;">
          {{GUARANTEE_TEXT}}
        </p>
      </div>

      <!-- Image Column -->
      <div>
        <img src="{{IMAGE_URL}}" alt="{{IMAGE_ALT}}" style="
          width: 100%;
          border-radius: 16px;
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        ">
      </div>
    </div>
  </div>
</section>
```

---

## Sticky CTA Bar

Best for: Long sales pages, persistent conversion opportunity.

```html
<!-- Sticky Bar (place at end of body) -->
<div id="sticky-cta" style="
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  padding: 1rem 0;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transform: translateY(100%);
  transition: transform 0.3s ease;
">
  <div class="mv-container">
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem;">
      <div style="display: flex; align-items: center; gap: 1rem;">
        <span class="title-7" style="color: #0f131a;">{{PRODUCT_NAME}}</span>
        <span class="body-bold" style="color: #7a12d4;">{{PRICE}}</span>
        <span class="body-sm" style="color: #6b7280; text-decoration: line-through;">{{ORIGINAL_PRICE}}</span>
      </div>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        padding: 0.75rem 2rem;
        background: #7a12d4;
        color: white;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
        white-space: nowrap;
      ">{{CTA_TEXT}}</a>
    </div>
  </div>
</div>

<!-- Show sticky bar after scrolling past hero -->
<script>
(function() {
  const stickyBar = document.getElementById('sticky-cta');
  const showAfter = 600; // pixels from top

  window.addEventListener('scroll', function() {
    if (window.scrollY > showAfter) {
      stickyBar.style.transform = 'translateY(0)';
    } else {
      stickyBar.style.transform = 'translateY(100%)';
    }
  });
})();
</script>
```

---

## Inline CTA

Best for: Mid-page conversion points, between content sections.

```html
<section class="mv-container" style="padding: 3rem 0;">
  <div style="
    background: linear-gradient(135deg, #f5f0fa 0%, #e8e0f0 100%);
    border-radius: 16px;
    padding: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
    flex-wrap: wrap;
  ">
    <div>
      <h3 class="title-bold-5" style="color: #0f131a; margin-bottom: 0.5rem;">
        {{HEADLINE}}
      </h3>
      <p class="body" style="color: #4b5563; margin: 0;">
        {{SUBHEADLINE}}
      </p>
    </div>

    <a href="{{CTA_URL}}" class="button" style="
      display: inline-flex;
      padding: 1rem 2rem;
      background: #7a12d4;
      color: white;
      font-weight: 600;
      border-radius: 999px;
      text-decoration: none;
      white-space: nowrap;
    ">{{CTA_TEXT}}</a>
  </div>
</section>
```

---

## CTA Button Variants

### Primary (Purple filled)
```html
<a href="{{URL}}" style="
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem;
  background: #7a12d4;
  color: white;
  font-weight: 600;
  border-radius: 999px;
  text-decoration: none;
">{{TEXT}}</a>
```

### Secondary (Purple outline)
```html
<a href="{{URL}}" style="
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem;
  background: transparent;
  color: #7a12d4;
  font-weight: 500;
  border-radius: 999px;
  border: 2px solid #7a12d4;
  text-decoration: none;
">{{TEXT}}</a>
```

### Orange (High conversion)
```html
<a href="{{URL}}" style="
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem;
  background: linear-gradient(180deg, #f97316 0%, #ea580c 100%);
  color: white;
  font-weight: 600;
  border-radius: 999px;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.4);
">{{TEXT}}</a>
```

### White (On dark backgrounds)
```html
<a href="{{URL}}" style="
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem;
  background: white;
  color: #7a12d4;
  font-weight: 600;
  border-radius: 999px;
  text-decoration: none;
">{{TEXT}}</a>
```

---

## Guarantee Text Examples

```
✓ 15-day money-back guarantee
✓ Cancel anytime, no questions asked
✓ Risk-free — try it for 15 days
✓ 100% satisfaction guaranteed
✓ Join 6+ million students worldwide
```
