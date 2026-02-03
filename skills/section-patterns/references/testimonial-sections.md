# Testimonial Section Patterns

## Table of Contents
1. [Quote Cards Grid](#quote-cards-grid) - 3-column testimonial cards
2. [Featured Testimonial](#featured-testimonial) - Single large testimonial
3. [Video Testimonials](#video-testimonials) - Video embed grid
4. [Teacher/Author Bio](#teacherauthor-bio) - Authority section
5. [Logo Bar](#logo-bar) - "As seen in" media logos
6. [Social Proof Strip](#social-proof-strip) - Compact trust indicators

---

## Quote Cards Grid

Best for: Multiple customer testimonials, social proof sections.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <!-- Section Header -->
    <div style="text-align: center; margin-bottom: 3rem;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
        TESTIMONIALS
      </p>
      <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 1rem;">
        {{HEADLINE}}
      </h2>
    </div>

    <!-- Testimonial Grid -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
      <!-- Testimonial 1 -->
      <div style="background: white; border-radius: 16px; padding: 2rem; display: flex; flex-direction: column;">
        <!-- Stars -->
        <div style="display: flex; gap: 4px; margin-bottom: 1rem;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
        </div>

        <!-- Quote -->
        <p class="body" style="color: #4b5563; flex-grow: 1; margin-bottom: 1.5rem;">
          "{{QUOTE_1}}"
        </p>

        <!-- Result highlight -->
        <p class="body-bold" style="color: #10b981; margin-bottom: 1rem;">
          {{RESULT_1}}
        </p>

        <!-- Author -->
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <img src="{{AVATAR_1}}" alt="{{NAME_1}}" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover;">
          <div>
            <p class="body-bold" style="color: #0f131a; margin: 0;">{{NAME_1}}</p>
            <p class="body-sm" style="color: #6b7280; margin: 0;">{{TITLE_1}}</p>
          </div>
        </div>
      </div>

      <!-- Testimonial 2 -->
      <div style="background: white; border-radius: 16px; padding: 2rem; display: flex; flex-direction: column;">
        <div style="display: flex; gap: 4px; margin-bottom: 1rem;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
        </div>
        <p class="body" style="color: #4b5563; flex-grow: 1; margin-bottom: 1.5rem;">"{{QUOTE_2}}"</p>
        <p class="body-bold" style="color: #10b981; margin-bottom: 1rem;">{{RESULT_2}}</p>
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <img src="{{AVATAR_2}}" alt="{{NAME_2}}" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover;">
          <div>
            <p class="body-bold" style="color: #0f131a; margin: 0;">{{NAME_2}}</p>
            <p class="body-sm" style="color: #6b7280; margin: 0;">{{TITLE_2}}</p>
          </div>
        </div>
      </div>

      <!-- Testimonial 3 -->
      <div style="background: white; border-radius: 16px; padding: 2rem; display: flex; flex-direction: column;">
        <div style="display: flex; gap: 4px; margin-bottom: 1rem;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="#F5C918"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
        </div>
        <p class="body" style="color: #4b5563; flex-grow: 1; margin-bottom: 1.5rem;">"{{QUOTE_3}}"</p>
        <p class="body-bold" style="color: #10b981; margin-bottom: 1rem;">{{RESULT_3}}</p>
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <img src="{{AVATAR_3}}" alt="{{NAME_3}}" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover;">
          <div>
            <p class="body-bold" style="color: #0f131a; margin: 0;">{{NAME_3}}</p>
            <p class="body-sm" style="color: #6b7280; margin: 0;">{{TITLE_3}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Featured Testimonial

Best for: Hero-level social proof, key customer story.

```html
<section class="mv-container" style="padding: 5rem 0;">
  <div style="max-width: 48rem; margin: 0 auto; text-align: center;">
    <!-- Large quote marks -->
    <svg width="48" height="48" viewBox="0 0 48 48" fill="#e5e7eb" style="margin-bottom: 1.5rem;">
      <path d="M14 24c-4.4 0-8-3.6-8-8s3.6-8 8-8c4.4 0 8 3.6 8 8s-3.6 8-8 8zm20 0c-4.4 0-8-3.6-8-8s3.6-8 8-8c4.4 0 8 3.6 8 8s-3.6 8-8 8z"/>
    </svg>

    <!-- Quote -->
    <p class="title-bold-4" style="color: #0f131a; margin-bottom: 2rem; font-style: italic;">
      "{{QUOTE}}"
    </p>

    <!-- Result -->
    <p class="body-lg" style="color: #10b981; margin-bottom: 2rem;">
      {{RESULT}}
    </p>

    <!-- Author with larger photo -->
    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
      <img src="{{AVATAR}}" alt="{{NAME}}" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover;">
      <div style="text-align: left;">
        <p class="title-7" style="color: #0f131a; margin: 0;">{{NAME}}</p>
        <p class="body" style="color: #6b7280; margin: 0;">{{TITLE}}</p>
      </div>
    </div>
  </div>
</section>
```

---

## Video Testimonials

Best for: High-impact social proof, authentic customer stories.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">SUCCESS STORIES</p>
      <h2 class="title-bold-3" style="color: #0f131a;">{{HEADLINE}}</h2>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
      <!-- Video 1 -->
      <div style="background: white; border-radius: 16px; overflow: hidden;">
        <div style="position: relative; padding-bottom: 56.25%;">
          <iframe src="https://www.youtube.com/embed/{{VIDEO_ID_1}}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
        </div>
        <div style="padding: 1.5rem;">
          <p class="body-bold" style="color: #0f131a; margin-bottom: 0.25rem;">{{NAME_1}}</p>
          <p class="body-sm" style="color: #6b7280; margin: 0;">{{RESULT_1}}</p>
        </div>
      </div>

      <!-- Video 2 -->
      <div style="background: white; border-radius: 16px; overflow: hidden;">
        <div style="position: relative; padding-bottom: 56.25%;">
          <iframe src="https://www.youtube.com/embed/{{VIDEO_ID_2}}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
        </div>
        <div style="padding: 1.5rem;">
          <p class="body-bold" style="color: #0f131a; margin-bottom: 0.25rem;">{{NAME_2}}</p>
          <p class="body-sm" style="color: #6b7280; margin: 0;">{{RESULT_2}}</p>
        </div>
      </div>

      <!-- Video 3 -->
      <div style="background: white; border-radius: 16px; overflow: hidden;">
        <div style="position: relative; padding-bottom: 56.25%;">
          <iframe src="https://www.youtube.com/embed/{{VIDEO_ID_3}}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
        </div>
        <div style="padding: 1.5rem;">
          <p class="body-bold" style="color: #0f131a; margin-bottom: 0.25rem;">{{NAME_3}}</p>
          <p class="body-sm" style="color: #6b7280; margin: 0;">{{RESULT_3}}</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Teacher/Author Bio

Best for: Program pages, establishing authority.

```html
<section class="mv-container" style="padding: 5rem 0;">
  <div style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 4rem; align-items: start;">
    <!-- Photo Column -->
    <div>
      <img src="{{TEACHER_IMAGE}}" alt="{{TEACHER_NAME}}" style="width: 100%; border-radius: 16px;">
    </div>

    <!-- Bio Column -->
    <div>
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">YOUR TEACHER</p>
      <h2 class="title-bold-3" style="color: #0f131a; margin-bottom: 0.5rem;">{{TEACHER_NAME}}</h2>
      <p class="body-lg" style="color: #7a12d4; margin-bottom: 1.5rem;">{{TEACHER_TITLE}}</p>
      <p class="body-lg" style="color: #4b5563; margin-bottom: 1.5rem;">{{BIO_PARAGRAPH_1}}</p>
      <p class="body" style="color: #4b5563; margin-bottom: 2rem;">{{BIO_PARAGRAPH_2}}</p>

      <!-- Credentials -->
      <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 2rem;">
        <span style="background: #f5f0fa; color: #7a12d4; padding: 0.5rem 1rem; border-radius: 999px; font-size: 14px;">{{CREDENTIAL_1}}</span>
        <span style="background: #f5f0fa; color: #7a12d4; padding: 0.5rem 1rem; border-radius: 999px; font-size: 14px;">{{CREDENTIAL_2}}</span>
        <span style="background: #f5f0fa; color: #7a12d4; padding: 0.5rem 1rem; border-radius: 999px; font-size: 14px;">{{CREDENTIAL_3}}</span>
      </div>

      <!-- As Seen In -->
      <p class="body-sm" style="color: #6b7280; margin-bottom: 1rem;">As seen in:</p>
      <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; align-items: center; opacity: 0.6;">
        <img src="{{LOGO_1}}" alt="{{LOGO_1_ALT}}" style="height: 24px;">
        <img src="{{LOGO_2}}" alt="{{LOGO_2_ALT}}" style="height: 24px;">
        <img src="{{LOGO_3}}" alt="{{LOGO_3_ALT}}" style="height: 24px;">
      </div>
    </div>
  </div>
</section>
```

---

## Logo Bar

Best for: "As seen in" credibility, partner logos.

```html
<section style="background: #f9f7fc; padding: 3rem 0;">
  <div class="mv-container">
    <p class="body-sm" style="text-align: center; color: #6b7280; margin-bottom: 1.5rem;">AS FEATURED IN</p>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 3rem; opacity: 0.5;">
      <img src="{{LOGO_1}}" alt="{{LOGO_1_ALT}}" style="height: 32px;">
      <img src="{{LOGO_2}}" alt="{{LOGO_2_ALT}}" style="height: 32px;">
      <img src="{{LOGO_3}}" alt="{{LOGO_3_ALT}}" style="height: 32px;">
      <img src="{{LOGO_4}}" alt="{{LOGO_4_ALT}}" style="height: 32px;">
      <img src="{{LOGO_5}}" alt="{{LOGO_5_ALT}}" style="height: 32px;">
    </div>
  </div>
</section>
```

---

## Social Proof Strip

Best for: Compact trust indicators, between sections.

```html
<section style="background: white; padding: 2rem 0; border-top: 1px solid #e5e7eb; border-bottom: 1px solid #e5e7eb;">
  <div class="mv-container">
    <div style="display: flex; justify-content: center; align-items: center; gap: 3rem; flex-wrap: wrap;">
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="#10b981"><path d="M10 1l2.5 5.5H18l-4.5 3.5 1.7 5.5L10 12.5 4.8 15.5l1.7-5.5L2 6.5h5.5L10 1z"/></svg>
        <span class="body-bold" style="color: #0f131a;">{{RATING}}</span>
        <span class="body-sm" style="color: #6b7280;">{{RATING_COUNT}} reviews</span>
      </div>
      <div style="width: 1px; height: 24px; background: #e5e7eb;"></div>
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span class="body-bold" style="color: #0f131a;">{{STUDENTS}}</span>
        <span class="body-sm" style="color: #6b7280;">students enrolled</span>
      </div>
      <div style="width: 1px; height: 24px; background: #e5e7eb;"></div>
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span class="body-bold" style="color: #0f131a;">{{HOURS}}</span>
        <span class="body-sm" style="color: #6b7280;">hours of content</span>
      </div>
    </div>
  </div>
</section>
```

---

## Avatar Placeholders

When no avatar images are available, use CSS initials:

```html
<div style="width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, #7a12d4 0%, #9b4dca 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem;">
  {{INITIALS}}
</div>
```
