# Hero Section Patterns

## Table of Contents
1. [Centered Hero](#centered-hero) - Default, most versatile
2. [Split Hero (Image Right)](#split-hero-image-right) - Text left, image right
3. [Split Hero (Image Left)](#split-hero-image-left) - Image left, text right
4. [Video Background Hero](#video-background-hero) - Full-width video
5. [Gradient Background Hero](#gradient-background-hero) - Purple gradient
6. [Hero with Form](#hero-with-form) - Lead capture

---

## Centered Hero

Best for: Sales pages, program pages, general landing pages.

```html
<section class="mv-container" style="padding: 6rem 0 5rem 0; text-align: center;">
  <div style="max-width: 48rem; margin: 0 auto;">
    <!-- Eyebrow -->
    <p class="overline-text" style="color: #7a12d4; margin-bottom: 1rem;">
      {{EYEBROW}}
    </p>

    <!-- Headline -->
    <h1 class="title-bold-1" style="color: #0f131a; margin-bottom: 1.5rem;">
      {{HEADLINE}}
    </h1>

    <!-- Subheadline -->
    <p class="body-lg" style="color: #4b5563; margin-bottom: 2rem; max-width: 40rem; margin-left: auto; margin-right: auto;">
      {{SUBHEADLINE}}
    </p>

    <!-- CTA Buttons -->
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

      <!-- Optional secondary CTA -->
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

    <!-- Optional: Social proof stat -->
    <p class="body-sm" style="color: #6b7280; margin-top: 1.5rem;">
      {{SOCIAL_PROOF}}
    </p>
  </div>

  <!-- Optional: Hero image below -->
  <div style="margin-top: 3rem;">
    <img src="{{IMAGE_URL}}" alt="{{IMAGE_ALT}}" style="
      max-width: 100%;
      border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    ">
  </div>
</section>
```

---

## Split Hero (Image Right)

Best for: Program pages, teacher-focused pages.

```html
<section class="mv-container" style="padding: 6rem 0 5rem 0;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <!-- Text Column -->
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 1rem;">
        {{EYEBROW}}
      </p>

      <h1 class="title-bold-2" style="color: #0f131a; margin-bottom: 1.5rem;">
        {{HEADLINE}}
      </h1>

      <p class="body-lg" style="color: #4b5563; margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

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

      <p class="body-sm" style="color: #6b7280; margin-top: 1.5rem;">
        {{SOCIAL_PROOF}}
      </p>
    </div>

    <!-- Image Column -->
    <div>
      <img src="{{IMAGE_URL}}" alt="{{IMAGE_ALT}}" style="
        width: 100%;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      ">
    </div>
  </div>
</section>

<!-- Mobile responsive: Add this CSS -->
<style>
@media (max-width: 768px) {
  .mv-container > div[style*="grid-template-columns: 1fr 1fr"] {
    grid-template-columns: 1fr !important;
    text-align: center;
  }
}
</style>
```

---

## Split Hero (Image Left)

Best for: When visual should lead, story-focused pages.

```html
<section class="mv-container" style="padding: 6rem 0 5rem 0;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <!-- Image Column (First on desktop) -->
    <div>
      <img src="{{IMAGE_URL}}" alt="{{IMAGE_ALT}}" style="
        width: 100%;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      ">
    </div>

    <!-- Text Column -->
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 1rem;">
        {{EYEBROW}}
      </p>

      <h1 class="title-bold-2" style="color: #0f131a; margin-bottom: 1.5rem;">
        {{HEADLINE}}
      </h1>

      <p class="body-lg" style="color: #4b5563; margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        padding: 1rem 2rem;
        background: #7a12d4;
        color: white;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
      ">{{CTA_TEXT}}</a>
    </div>
  </div>
</section>
```

---

## Video Background Hero

Best for: High-energy pages, event promotions.

```html
<section style="position: relative; min-height: 80vh; display: flex; align-items: center; overflow: hidden;">
  <!-- Video Background -->
  <video autoplay muted loop playsinline style="
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -2;
  ">
    <source src="{{VIDEO_URL}}" type="video/mp4">
  </video>

  <!-- Dark Overlay -->
  <div style="
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: -1;
  "></div>

  <!-- Content -->
  <div class="mv-container" style="text-align: center; color: white; padding: 6rem 0;">
    <div style="max-width: 48rem; margin: 0 auto;">
      <p class="overline-text" style="color: #F5C918; margin-bottom: 1rem;">
        {{EYEBROW}}
      </p>

      <h1 class="title-bold-1" style="color: white; margin-bottom: 1.5rem;">
        {{HEADLINE}}
      </h1>

      <p class="body-lg" style="color: rgba(255, 255, 255, 0.9); margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        padding: 1rem 2rem;
        background: #7a12d4;
        color: white;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
      ">{{CTA_TEXT}}</a>
    </div>
  </div>
</section>
```

---

## Gradient Background Hero

Best for: Premium feel, membership pages.

```html
<section style="background: linear-gradient(135deg, #7a12d4 0%, #5b0fa8 50%, #3d0a70 100%); padding: 6rem 0 5rem 0;">
  <div class="mv-container" style="text-align: center;">
    <div style="max-width: 48rem; margin: 0 auto;">
      <p class="overline-text" style="color: #F5C918; margin-bottom: 1rem;">
        {{EYEBROW}}
      </p>

      <h1 class="title-bold-1" style="color: white; margin-bottom: 1.5rem;">
        {{HEADLINE}}
      </h1>

      <p class="body-lg" style="color: rgba(255, 255, 255, 0.9); margin-bottom: 2rem; max-width: 40rem; margin-left: auto; margin-right: auto;">
        {{SUBHEADLINE}}
      </p>

      <a href="{{CTA_URL}}" class="button" style="
        display: inline-flex;
        padding: 1rem 2rem;
        background: white;
        color: #7a12d4;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
      ">{{CTA_TEXT}}</a>

      <p class="body-sm" style="color: rgba(255, 255, 255, 0.7); margin-top: 1.5rem;">
        {{SOCIAL_PROOF}}
      </p>
    </div>
  </div>
</section>
```

---

## Hero with Form

Best for: Lead capture, webinar registration, newsletter signup.

```html
<section class="mv-container" style="padding: 6rem 0 5rem 0;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <!-- Text Column -->
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 1rem;">
        {{EYEBROW}}
      </p>

      <h1 class="title-bold-2" style="color: #0f131a; margin-bottom: 1.5rem;">
        {{HEADLINE}}
      </h1>

      <p class="body-lg" style="color: #4b5563; margin-bottom: 2rem;">
        {{SUBHEADLINE}}
      </p>

      <!-- Bullet points -->
      <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0;">
        <li class="body" style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem; color: #0f131a;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex-shrink: 0;">
            <circle cx="10" cy="10" r="10" fill="#10b981"/>
            <path d="M6 10l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          {{BULLET_1}}
        </li>
        <li class="body" style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem; color: #0f131a;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex-shrink: 0;">
            <circle cx="10" cy="10" r="10" fill="#10b981"/>
            <path d="M6 10l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          {{BULLET_2}}
        </li>
        <li class="body" style="display: flex; align-items: center; gap: 0.75rem; color: #0f131a;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" style="flex-shrink: 0;">
            <circle cx="10" cy="10" r="10" fill="#10b981"/>
            <path d="M6 10l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          {{BULLET_3}}
        </li>
      </ul>
    </div>

    <!-- Form Column -->
    <div style="
      background: white;
      border-radius: 16px;
      padding: 2rem;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
    ">
      <h3 class="title-bold-5" style="margin-bottom: 1.5rem; color: #0f131a; text-align: center;">
        {{FORM_TITLE}}
      </h3>

      <form action="{{FORM_ACTION}}" method="POST">
        <div style="margin-bottom: 1rem;">
          <label class="body-sm" style="display: block; margin-bottom: 0.5rem; color: #4b5563;">First Name</label>
          <input type="text" name="first_name" required style="
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            font-size: 16px;
            box-sizing: border-box;
          ">
        </div>

        <div style="margin-bottom: 1rem;">
          <label class="body-sm" style="display: block; margin-bottom: 0.5rem; color: #4b5563;">Email Address</label>
          <input type="email" name="email" required style="
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            font-size: 16px;
            box-sizing: border-box;
          ">
        </div>

        <button type="submit" class="button" style="
          width: 100%;
          padding: 1rem 2rem;
          background: #7a12d4;
          color: white;
          font-weight: 600;
          border-radius: 999px;
          border: none;
          cursor: pointer;
          font-size: 16px;
        ">{{CTA_TEXT}}</button>

        <p class="caption-disclaimer" style="text-align: center; color: #9ca3af; margin-top: 1rem;">
          {{DISCLAIMER}}
        </p>
      </form>
    </div>
  </div>
</section>
```

---

## Placeholder Examples

For draft pages, use these placeholder image URLs:

```
Hero background: https://placehold.co/1920x800/e8e0f0/7a12d4?text=Hero+Background
Split image: https://placehold.co/600x600/f5f0fa/7a12d4?text=Hero+Image
Speaker photo: https://placehold.co/500x600/e8e0f0/7a12d4?text=Speaker
```
