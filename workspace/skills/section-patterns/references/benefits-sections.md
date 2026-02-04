# Benefits Section Patterns

## Table of Contents
1. [3-Column Benefits Grid](#3-column-benefits-grid) - Classic feature grid
2. [2-Column Features](#2-column-features) - Alternating image/text
3. [Icon List](#icon-list) - Vertical list with icons
4. [Problem-Agitation](#problem-agitation) - Pain points before solution
5. [Stats Bar](#stats-bar) - Key metrics display
6. [What's Included](#whats-included) - Curriculum/package contents

---

## 3-Column Benefits Grid

Best for: Feature highlights, key benefits, program outcomes.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <!-- Section Header -->
    <div style="text-align: center; margin-bottom: 3rem;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        {{EYEBROW}}
      </p>
      <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 1rem; max-width: 36rem; margin-left: auto; margin-right: auto;">
        {{HEADLINE}}
      </h2>
      <p class="body-lg" style="color: #4b5563; max-width: 32rem; margin: 0 auto;">
        {{SUBHEADLINE}}
      </p>
    </div>

    <!-- Benefits Grid -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
      <!-- Benefit 1 -->
      <div style="background: white; padding: 2rem; border-radius: 16px; text-align: center;">
        <div style="width: 64px; height: 64px; background: #f5f0fa; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#7a12d4" stroke-width="2">
            {{ICON_1_PATH}}
          </svg>
        </div>
        <h3 class="title-bold-6" style="color: #0f131a; margin-bottom: 0.75rem;">
          {{BENEFIT_1_TITLE}}
        </h3>
        <p class="body" style="color: #4b5563;">
          {{BENEFIT_1_DESC}}
        </p>
      </div>

      <!-- Benefit 2 -->
      <div style="background: white; padding: 2rem; border-radius: 16px; text-align: center;">
        <div style="width: 64px; height: 64px; background: #f5f0fa; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#7a12d4" stroke-width="2">
            {{ICON_2_PATH}}
          </svg>
        </div>
        <h3 class="title-bold-6" style="color: #0f131a; margin-bottom: 0.75rem;">
          {{BENEFIT_2_TITLE}}
        </h3>
        <p class="body" style="color: #4b5563;">
          {{BENEFIT_2_DESC}}
        </p>
      </div>

      <!-- Benefit 3 -->
      <div style="background: white; padding: 2rem; border-radius: 16px; text-align: center;">
        <div style="width: 64px; height: 64px; background: #f5f0fa; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#7a12d4" stroke-width="2">
            {{ICON_3_PATH}}
          </svg>
        </div>
        <h3 class="title-bold-6" style="color: #0f131a; margin-bottom: 0.75rem;">
          {{BENEFIT_3_TITLE}}
        </h3>
        <p class="body" style="color: #4b5563;">
          {{BENEFIT_3_DESC}}
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Mobile: Stack to single column -->
<style>
@media (max-width: 768px) {
  [style*="grid-template-columns: repeat(3, 1fr)"] {
    grid-template-columns: 1fr !important;
  }
}
</style>
```

---

## 2-Column Features

Best for: Detailed feature explanations, alternating content.

```html
<section class="mv-container" style="padding: 5rem 0;">
  <!-- Feature 1: Image Right -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; margin-bottom: 5rem;">
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        {{FEATURE_1_EYEBROW}}
      </p>
      <h3 class="title-bold-4" style="color: #0f131a; margin-bottom: 1rem;">
        {{FEATURE_1_TITLE}}
      </h3>
      <p class="body-lg" style="color: #4b5563;">
        {{FEATURE_1_DESC}}
      </p>
    </div>
    <div>
      <img src="{{FEATURE_1_IMAGE}}" alt="{{FEATURE_1_ALT}}" style="width: 100%; border-radius: 16px;">
    </div>
  </div>

  <!-- Feature 2: Image Left -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; margin-bottom: 5rem;">
    <div>
      <img src="{{FEATURE_2_IMAGE}}" alt="{{FEATURE_2_ALT}}" style="width: 100%; border-radius: 16px;">
    </div>
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        {{FEATURE_2_EYEBROW}}
      </p>
      <h3 class="title-bold-4" style="color: #0f131a; margin-bottom: 1rem;">
        {{FEATURE_2_TITLE}}
      </h3>
      <p class="body-lg" style="color: #4b5563;">
        {{FEATURE_2_DESC}}
      </p>
    </div>
  </div>

  <!-- Feature 3: Image Right -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        {{FEATURE_3_EYEBROW}}
      </p>
      <h3 class="title-bold-4" style="color: #0f131a; margin-bottom: 1rem;">
        {{FEATURE_3_TITLE}}
      </h3>
      <p class="body-lg" style="color: #4b5563;">
        {{FEATURE_3_DESC}}
      </p>
    </div>
    <div>
      <img src="{{FEATURE_3_IMAGE}}" alt="{{FEATURE_3_ALT}}" style="width: 100%; border-radius: 16px;">
    </div>
  </div>
</section>
```

---

## Icon List

Best for: Quick benefits, feature lists, checkmark lists.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
      <!-- Text Column -->
      <div>
        <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
          {{EYEBROW}}
        </p>
        <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 1.5rem;">
          {{HEADLINE}}
        </h2>

        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="display: flex; gap: 1rem; margin-bottom: 1.25rem;">
            <div style="width: 24px; height: 24px; background: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 7l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div>
              <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{ITEM_1_TITLE}}</h4>
              <p class="body" style="color: #4b5563; margin: 0;">{{ITEM_1_DESC}}</p>
            </div>
          </li>

          <li style="display: flex; gap: 1rem; margin-bottom: 1.25rem;">
            <div style="width: 24px; height: 24px; background: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 7l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div>
              <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{ITEM_2_TITLE}}</h4>
              <p class="body" style="color: #4b5563; margin: 0;">{{ITEM_2_DESC}}</p>
            </div>
          </li>

          <li style="display: flex; gap: 1rem; margin-bottom: 1.25rem;">
            <div style="width: 24px; height: 24px; background: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 7l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div>
              <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{ITEM_3_TITLE}}</h4>
              <p class="body" style="color: #4b5563; margin: 0;">{{ITEM_3_DESC}}</p>
            </div>
          </li>

          <li style="display: flex; gap: 1rem;">
            <div style="width: 24px; height: 24px; background: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 7l3 3 5-6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div>
              <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{ITEM_4_TITLE}}</h4>
              <p class="body" style="color: #4b5563; margin: 0;">{{ITEM_4_DESC}}</p>
            </div>
          </li>
        </ul>
      </div>

      <!-- Image Column -->
      <div>
        <img src="{{IMAGE_URL}}" alt="{{IMAGE_ALT}}" style="width: 100%; border-radius: 16px;">
      </div>
    </div>
  </div>
</section>
```

---

## Problem-Agitation

Best for: Sales pages, before introducing solution.

```html
<section class="mv-container" style="padding: 5rem 0;">
  <div style="max-width: 48rem; margin: 0 auto; text-align: center;">
    <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 2rem;">
      {{HEADLINE}}
    </h2>

    <p class="body-lg" style="color: #4b5563; margin-bottom: 3rem;">
      {{OPENING_HOOK}}
    </p>
  </div>

  <!-- Pain Point Cards -->
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; max-width: 56rem; margin: 0 auto;">
    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; padding: 1.5rem;">
      <p class="body-bold" style="color: #dc2626; margin-bottom: 0.5rem;">{{PAIN_1_TITLE}}</p>
      <p class="body-sm" style="color: #7f1d1d; margin: 0;">{{PAIN_1_DESC}}</p>
    </div>

    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; padding: 1.5rem;">
      <p class="body-bold" style="color: #dc2626; margin-bottom: 0.5rem;">{{PAIN_2_TITLE}}</p>
      <p class="body-sm" style="color: #7f1d1d; margin: 0;">{{PAIN_2_DESC}}</p>
    </div>

    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; padding: 1.5rem;">
      <p class="body-bold" style="color: #dc2626; margin-bottom: 0.5rem;">{{PAIN_3_TITLE}}</p>
      <p class="body-sm" style="color: #7f1d1d; margin: 0;">{{PAIN_3_DESC}}</p>
    </div>
  </div>

  <!-- Bridge Statement -->
  <div style="text-align: center; margin-top: 3rem;">
    <p class="body-lg" style="color: #4b5563; font-style: italic;">
      {{BRIDGE_STATEMENT}}
    </p>
  </div>
</section>
```

---

## Stats Bar

Best for: Social proof, credibility, impact numbers.

```html
<section style="background: #7a12d4; padding: 3rem 0;">
  <div class="mv-container">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; text-align: center;">
      <div>
        <p class="title-bold-2" style="color: white; margin-bottom: 0.25rem;">{{STAT_1_NUMBER}}</p>
        <p class="body" style="color: rgba(255, 255, 255, 0.8); margin: 0;">{{STAT_1_LABEL}}</p>
      </div>

      <div>
        <p class="title-bold-2" style="color: white; margin-bottom: 0.25rem;">{{STAT_2_NUMBER}}</p>
        <p class="body" style="color: rgba(255, 255, 255, 0.8); margin: 0;">{{STAT_2_LABEL}}</p>
      </div>

      <div>
        <p class="title-bold-2" style="color: white; margin-bottom: 0.25rem;">{{STAT_3_NUMBER}}</p>
        <p class="body" style="color: rgba(255, 255, 255, 0.8); margin: 0;">{{STAT_3_LABEL}}</p>
      </div>

      <div>
        <p class="title-bold-2" style="color: white; margin-bottom: 0.25rem;">{{STAT_4_NUMBER}}</p>
        <p class="body" style="color: rgba(255, 255, 255, 0.8); margin: 0;">{{STAT_4_LABEL}}</p>
      </div>
    </div>
  </div>
</section>

<!-- Mobile: 2x2 grid -->
<style>
@media (max-width: 768px) {
  [style*="grid-template-columns: repeat(4, 1fr)"] {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
</style>
```

---

## What's Included

Best for: Program curriculum, package contents, membership benefits.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        WHAT'S INCLUDED
      </p>
      <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 1rem;">
        {{HEADLINE}}
      </h2>
    </div>

    <!-- Curriculum Grid -->
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; max-width: 56rem; margin: 0 auto;">
      <!-- Module 1 -->
      <div style="background: white; border-radius: 12px; padding: 1.5rem; display: flex; gap: 1rem;">
        <div style="width: 48px; height: 48px; background: #f5f0fa; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span class="title-bold-6" style="color: #7a12d4;">01</span>
        </div>
        <div>
          <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{MODULE_1_TITLE}}</h4>
          <p class="body-sm" style="color: #4b5563; margin: 0;">{{MODULE_1_DESC}}</p>
        </div>
      </div>

      <!-- Module 2 -->
      <div style="background: white; border-radius: 12px; padding: 1.5rem; display: flex; gap: 1rem;">
        <div style="width: 48px; height: 48px; background: #f5f0fa; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span class="title-bold-6" style="color: #7a12d4;">02</span>
        </div>
        <div>
          <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{MODULE_2_TITLE}}</h4>
          <p class="body-sm" style="color: #4b5563; margin: 0;">{{MODULE_2_DESC}}</p>
        </div>
      </div>

      <!-- Module 3 -->
      <div style="background: white; border-radius: 12px; padding: 1.5rem; display: flex; gap: 1rem;">
        <div style="width: 48px; height: 48px; background: #f5f0fa; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span class="title-bold-6" style="color: #7a12d4;">03</span>
        </div>
        <div>
          <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{MODULE_3_TITLE}}</h4>
          <p class="body-sm" style="color: #4b5563; margin: 0;">{{MODULE_3_DESC}}</p>
        </div>
      </div>

      <!-- Module 4 -->
      <div style="background: white; border-radius: 12px; padding: 1.5rem; display: flex; gap: 1rem;">
        <div style="width: 48px; height: 48px; background: #f5f0fa; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span class="title-bold-6" style="color: #7a12d4;">04</span>
        </div>
        <div>
          <h4 class="title-7" style="color: #0f131a; margin-bottom: 0.25rem;">{{MODULE_4_TITLE}}</h4>
          <p class="body-sm" style="color: #4b5563; margin: 0;">{{MODULE_4_DESC}}</p>
        </div>
      </div>
    </div>

    <!-- Bonus callout -->
    <div style="max-width: 56rem; margin: 2rem auto 0; background: linear-gradient(135deg, #7a12d4, #5b0fa8); border-radius: 12px; padding: 1.5rem; display: flex; align-items: center; gap: 1rem;">
      <div style="width: 48px; height: 48px; background: rgba(255,255,255,0.2); border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
          <path d="M12 2l3 7h7l-5.5 4.5 2 7L12 16l-6.5 4.5 2-7L2 9h7l3-7z"/>
        </svg>
      </div>
      <div>
        <h4 class="title-7" style="color: white; margin-bottom: 0.25rem;">BONUS: {{BONUS_TITLE}}</h4>
        <p class="body-sm" style="color: rgba(255,255,255,0.9); margin: 0;">{{BONUS_DESC}}</p>
      </div>
    </div>
  </div>
</section>
```

---

## Common Icon SVG Paths

Use these in the icon containers:

```html
<!-- Checkmark -->
<path d="M5 12l5 5L20 7"/>

<!-- Star -->
<path d="M12 2l3 7h7l-5.5 4.5 2 7L12 16l-6.5 4.5 2-7L2 9h7l3-7z"/>

<!-- Heart -->
<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>

<!-- Lightning -->
<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>

<!-- Brain -->
<path d="M12 2a4 4 0 0 0-4 4v1a4 4 0 0 0-4 4c0 1.5.8 2.8 2 3.4V18a4 4 0 0 0 4 4h4a4 4 0 0 0 4-4v-3.6a4 4 0 0 0 2-3.4 4 4 0 0 0-4-4V6a4 4 0 0 0-4-4z"/>

<!-- Clock -->
<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>

<!-- Users -->
<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>

<!-- Play -->
<polygon points="5 3 19 12 5 21 5 3"/>
```
