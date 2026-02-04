# Mindvalley Component Patterns

Copy-paste ready patterns for building Mindvalley-branded pages.

**IMPORTANT: Purple (#7a12d4) is ONLY for action items - CTAs, links, eyebrow text. Use neutral backgrounds.**

## Table of Contents
1. [Hero Sections](#hero-sections)
2. [Feature Sections](#feature-sections)
3. [Speaker/Host Sections](#speakerhost-sections)
4. [Testimonial Sections](#testimonial-sections)
5. [Schedule/Timeline Sections](#scheduletimeline-sections)
6. [FAQ Sections](#faq-sections)
7. [CTA Sections](#cta-sections)
8. [Cards](#cards)
9. [Buttons](#buttons)
10. [Footer](#footer)

---

## Hero Sections

### Standard Hero
```html
<section class="mv-container" style="padding: 6rem 0 5rem 0;">
  <div class="overline-text" style="margin-bottom: 1rem; color: #7a12d4;">
    EYEBROW TEXT HERE
  </div>
  <h1 class="title-bold-2" style="max-width: 48rem; margin: 0 0 1.25rem 0;">
    Your compelling headline that captures attention
  </h1>
  <p class="body-lg" style="max-width: 40rem; color: #4b5563; margin-bottom: 0;">
    Supporting subheadline that expands on the main value proposition and gives context.
  </p>
  <div style="display: flex; gap: 1rem; margin-top: 2.5rem; flex-wrap: wrap;">
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2rem; background-color: #7a12d4; color: white;
      font-weight: 700; border-radius: 999px; text-decoration: none;
    ">Primary CTA</a>
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2rem; background-color: transparent; color: #7a12d4;
      border: 2px solid #7a12d4; font-weight: 500; border-radius: 999px;
      text-decoration: none;
    ">Secondary CTA</a>
  </div>
</section>
```

### Hero with Background Image
```html
<section style="position: relative; overflow: hidden;">
  <img src="https://placehold.co/1920x800/f3f4f6/6b7280?text=Hero+Background"
       alt="[PLACEHOLDER: Hero background]"
       style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;
              object-fit: cover; z-index: 0;" />
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;
              background: linear-gradient(to right, rgba(255,255,255,0.95), rgba(255,255,255,0.7));
              z-index: 1;"></div>
  <div class="mv-container" style="position: relative; z-index: 2; padding: 6rem 0 5rem 0;">
    <div class="overline-text" style="margin-bottom: 1rem; color: #7a12d4;">
      EYEBROW TEXT
    </div>
    <h1 class="title-bold-2" style="max-width: 48rem; margin: 0 0 1.25rem 0;">
      Headline over background
    </h1>
    <p class="body-lg" style="max-width: 40rem; color: #4b5563;">
      Supporting text here.
    </p>
  </div>
</section>
```

### Centered Hero
```html
<section class="mv-container" style="padding: 6rem 0 5rem 0; text-align: center;">
  <div class="overline-text" style="margin-bottom: 1rem; color: #7a12d4;">
    EYEBROW TEXT
  </div>
  <h1 class="title-bold-2" style="max-width: 48rem; margin: 0 auto 1.25rem auto;">
    Centered headline for impact
  </h1>
  <p class="body-lg" style="max-width: 40rem; margin: 0 auto; color: #4b5563;">
    Supporting subheadline text centered below.
  </p>
  <div style="display: flex; gap: 1rem; margin-top: 2.5rem; justify-content: center; flex-wrap: wrap;">
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2rem; background-color: #7a12d4; color: white;
      font-weight: 700; border-radius: 999px; text-decoration: none;
    ">Get Started</a>
  </div>
</section>
```

---

## Feature Sections

### Three-Column Grid
```html
<section class="mv-container" style="padding: 5rem 0;">
  <h2 class="title-bold-4" style="margin-bottom: 2.25rem;">What You'll Learn</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 2rem;">
    <div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Feature One</h3>
      <p class="body">Description of the first feature or benefit that users will receive.</p>
    </div>
    <div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Feature Two</h3>
      <p class="body">Description of the second feature or benefit that users will receive.</p>
    </div>
    <div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Feature Three</h3>
      <p class="body">Description of the third feature or benefit that users will receive.</p>
    </div>
  </div>
</section>
```

### Features with Icons
```html
<section class="mv-container" style="padding: 5rem 0;">
  <h2 class="title-bold-4" style="margin-bottom: 2.25rem; text-align: center;">Key Benefits</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem;">
    <div style="text-align: center;">
      <div style="width: 48px; height: 48px; background: #7a12d4; border-radius: 0.75rem;
                  margin: 0 auto 1rem auto; display: flex; align-items: center; justify-content: center;">
        <span style="color: white;">✦</span>
      </div>
      <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Benefit Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of the benefit and how it helps the user.
      </p>
    </div>
    <div style="text-align: center;">
      <div style="width: 48px; height: 48px; background: #7a12d4; border-radius: 0.75rem;
                  margin: 0 auto 1rem auto; display: flex; align-items: center; justify-content: center;">
        <span style="color: white;">◈</span>
      </div>
      <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Benefit Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of the benefit and how it helps the user.
      </p>
    </div>
    <div style="text-align: center;">
      <div style="width: 48px; height: 48px; background: #7a12d4; border-radius: 0.75rem;
                  margin: 0 auto 1rem auto; display: flex; align-items: center; justify-content: center;">
        <span style="color: white;">◇</span>
      </div>
      <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Benefit Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of the benefit and how it helps the user.
      </p>
    </div>
  </div>
</section>
```

### Feature with Image (Left)
```html
<section class="mv-container" style="padding: 5rem 0;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <div>
      <img src="https://placehold.co/600x400/f9fafb/6b7280?text=Feature+Image"
           alt="[PLACEHOLDER: Feature image]"
           style="width: 100%; border-radius: 1rem;" />
    </div>
    <div>
      <div class="overline-text" style="margin-bottom: 0.75rem; color: #7a12d4;">
        FEATURE CATEGORY
      </div>
      <h2 class="title-bold-4" style="margin-bottom: 1rem;">
        Feature headline that explains the value
      </h2>
      <p class="body" style="color: #4b5563; margin-bottom: 1.5rem;">
        Detailed description of this feature and why it matters to the user.
        Include specific benefits and outcomes they can expect.
      </p>
      <a href="#" style="color: #7a12d4; font-weight: 500; text-decoration: none;">
        Learn more →
      </a>
    </div>
  </div>
</section>
```

---

## Speaker/Host Sections

### Single Speaker
```html
<section class="mv-container" style="padding: 5rem 0;">
  <h2 class="title-bold-4" style="margin-bottom: 2.25rem;">Meet Your Host</h2>
  <div style="display: flex; gap: 2rem; align-items: flex-start; flex-wrap: wrap;">
    <img src="https://placehold.co/200x200/f3f4f6/6b7280?text=Speaker"
         alt="[PLACEHOLDER: Speaker Name]"
         style="width: 180px; height: 180px; border-radius: 1rem; object-fit: cover;" />
    <div style="flex: 1; min-width: 280px;">
      <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Speaker Name</h3>
      <p class="body" style="color: #7a12d4; margin-bottom: 1rem;">Title / Role</p>
      <p class="body" style="color: #4b5563;">
        Bio and credentials. Include relevant experience, achievements, and why
        this person is qualified to lead this experience.
      </p>
    </div>
  </div>
</section>
```

### Multiple Speakers Grid
```html
<section style="background-color: #f9fafb;">
  <div class="mv-container" style="padding: 5rem 0;">
    <h2 class="title-bold-4" style="margin-bottom: 2.25rem; text-align: center;">
      Featured Speakers
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
      <div style="text-align: center;">
        <img src="https://placehold.co/200x200/e5e7eb/6b7280?text=Speaker+1"
             alt="[PLACEHOLDER: Speaker Name]"
             style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;" />
        <h3 class="title-bold-7" style="margin-bottom: 0.25rem;">Speaker Name</h3>
        <p class="body-sm" style="color: #7a12d4;">Title / Role</p>
      </div>
      <div style="text-align: center;">
        <img src="https://placehold.co/200x200/e5e7eb/6b7280?text=Speaker+2"
             alt="[PLACEHOLDER: Speaker Name]"
             style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;" />
        <h3 class="title-bold-7" style="margin-bottom: 0.25rem;">Speaker Name</h3>
        <p class="body-sm" style="color: #7a12d4;">Title / Role</p>
      </div>
      <div style="text-align: center;">
        <img src="https://placehold.co/200x200/e5e7eb/6b7280?text=Speaker+3"
             alt="[PLACEHOLDER: Speaker Name]"
             style="width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;" />
        <h3 class="title-bold-7" style="margin-bottom: 0.25rem;">Speaker Name</h3>
        <p class="body-sm" style="color: #7a12d4;">Title / Role</p>
      </div>
    </div>
  </div>
</section>
```

---

## Testimonial Sections

### Testimonial Cards Grid
```html
<section style="background-color: #f9fafb;">
  <div class="mv-container" style="padding: 5rem 0;">
    <h2 class="title-bold-4" style="margin-bottom: 2.25rem; text-align: center;">
      What People Are Saying
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
      <div style="background: white; padding: 2rem; border-radius: 1rem; border: 1px solid #e5e7eb;">
        <p class="body-italic" style="margin-bottom: 1.5rem; color: #4b5563;">
          "Testimonial quote goes here. Keep it authentic and specific about
          the transformation or benefit experienced."
        </p>
        <div style="display: flex; align-items: center; gap: 1rem;">
          <img src="https://placehold.co/60x60/e5e7eb/6b7280?text=Photo"
               alt="[PLACEHOLDER: Person Name]"
               style="width: 48px; height: 48px; border-radius: 50%;" />
          <div>
            <p class="body-bold" style="margin: 0;">Person Name</p>
            <p class="body-sm" style="color: #6b7280; margin: 0;">Location or Title</p>
          </div>
        </div>
      </div>
      <!-- Repeat for more testimonials -->
    </div>
  </div>
</section>
```

### Single Large Testimonial
```html
<section class="mv-container" style="padding: 5rem 0; text-align: center;">
  <p class="title-3" style="font-style: italic; max-width: 48rem; margin: 0 auto 2rem auto; color: #4b5563;">
    "A powerful, standout testimonial that captures the essence of the experience
    and the transformation it provides."
  </p>
  <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
    <img src="https://placehold.co/80x80/e5e7eb/6b7280?text=Photo"
         alt="[PLACEHOLDER: Person Name]"
         style="width: 64px; height: 64px; border-radius: 50%;" />
    <div style="text-align: left;">
      <p class="body-bold" style="margin: 0;">Person Name</p>
      <p class="body-sm" style="color: #6b7280; margin: 0;">Title, Company</p>
    </div>
  </div>
</section>
```

---

## Schedule/Timeline Sections

### Event Schedule
```html
<section class="mv-container" style="padding: 5rem 0;">
  <h2 class="title-bold-4" style="margin-bottom: 2.25rem;">Event Schedule</h2>
  <div style="max-width: 48rem;">
    <div style="margin-bottom: 2rem; padding-bottom: 2rem; border-bottom: 1px solid #e5e7eb;">
      <div class="overline-text" style="color: #7a12d4; margin-bottom: 0.5rem;">
        9:00 AM - 10:30 AM
      </div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Session Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of what this session covers and what participants will experience.
      </p>
    </div>
    <div style="margin-bottom: 2rem; padding-bottom: 2rem; border-bottom: 1px solid #e5e7eb;">
      <div class="overline-text" style="color: #7a12d4; margin-bottom: 0.5rem;">
        10:45 AM - 12:00 PM
      </div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Session Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of what this session covers and what participants will experience.
      </p>
    </div>
    <div>
      <div class="overline-text" style="color: #7a12d4; margin-bottom: 0.5rem;">
        1:00 PM - 3:00 PM
      </div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Session Title</h3>
      <p class="body" style="color: #4b5563;">
        Description of what this session covers and what participants will experience.
      </p>
    </div>
  </div>
</section>
```

---

## FAQ Sections

### Simple FAQ List
```html
<section style="background-color: #f9fafb;">
  <div class="mv-container" style="padding: 5rem 0;">
    <h2 class="title-bold-4" style="margin-bottom: 2.25rem; text-align: center;">
      Frequently Asked Questions
    </h2>
    <div style="max-width: 48rem; margin: 0 auto;">
      <div style="margin-bottom: 2rem;">
        <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Question one goes here?</h3>
        <p class="body" style="color: #4b5563;">
          Answer to the question with helpful detail and clarity.
        </p>
      </div>
      <div style="margin-bottom: 2rem;">
        <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Question two goes here?</h3>
        <p class="body" style="color: #4b5563;">
          Answer to the question with helpful detail and clarity.
        </p>
      </div>
      <div style="margin-bottom: 2rem;">
        <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Question three goes here?</h3>
        <p class="body" style="color: #4b5563;">
          Answer to the question with helpful detail and clarity.
        </p>
      </div>
    </div>
  </div>
</section>
```

---

## CTA Sections

### Final CTA Block
```html
<section style="background-color: #f9fafb;">
  <div class="mv-container" style="padding: 5rem 0; text-align: center;">
    <h2 class="title-bold-3" style="max-width: 40rem; margin: 0 auto 1rem auto;">
      Ready to transform your life?
    </h2>
    <p class="body-lg" style="max-width: 36rem; margin: 0 auto 2rem auto; color: #4b5563;">
      Join thousands who have already started their journey.
    </p>
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2.5rem; background-color: #7a12d4; color: white;
      font-weight: 700; border-radius: 999px; text-decoration: none;
      font-size: 1.125rem;
    ">Join Now</a>
  </div>
</section>
```

---

## Cards

### Content Card
```html
<div style="background: white; padding: 2rem; border-radius: 1rem; border: 1px solid #e5e7eb;">
  <img src="https://placehold.co/400x200/f9fafb/6b7280?text=Card+Image"
       alt="[PLACEHOLDER: Card image]"
       style="width: 100%; border-radius: 0.5rem; margin-bottom: 1.5rem;" />
  <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Card Title</h3>
  <p class="body" style="color: #4b5563; margin-bottom: 1rem;">
    Card description with relevant information.
  </p>
  <a href="#" style="color: #7a12d4; font-weight: 500; text-decoration: none;">
    Learn more →
  </a>
</div>
```

### Pricing Card
```html
<div style="background: white; padding: 2.5rem; border-radius: 1rem; text-align: center;
            border: 1px solid #e5e7eb;">
  <h3 class="title-bold-6" style="margin-bottom: 0.5rem;">Plan Name</h3>
  <p class="body-sm" style="color: #6b7280; margin-bottom: 1.5rem;">Best for individuals</p>
  <div style="margin-bottom: 1.5rem;">
    <span class="title-bold-3">$99</span>
    <span class="body" style="color: #6b7280;">/month</span>
  </div>
  <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; text-align: left;">
    <li class="body" style="padding: 0.5rem 0; border-bottom: 1px solid #f3f4f6;">✓ Feature one</li>
    <li class="body" style="padding: 0.5rem 0; border-bottom: 1px solid #f3f4f6;">✓ Feature two</li>
    <li class="body" style="padding: 0.5rem 0;">✓ Feature three</li>
  </ul>
  <a href="#" class="button" style="
    display: block; padding: 1rem; background-color: #7a12d4; color: white;
    font-weight: 700; border-radius: 999px; text-decoration: none;
  ">Get Started</a>
</div>
```

---

## Buttons

### Primary Button
```html
<a href="#" class="button" style="
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; background-color: #7a12d4; color: white;
  font-weight: 700; border-radius: 999px; text-decoration: none;
">Primary CTA</a>
```

### Secondary Button
```html
<a href="#" class="button" style="
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; background-color: transparent; color: #7a12d4;
  border: 2px solid #7a12d4; font-weight: 500; border-radius: 999px;
  text-decoration: none;
">Secondary CTA</a>
```

### Small Button
```html
<a href="#" class="button-sm" style="
  display: inline-flex; align-items: center; justify-content: center;
  padding: 0.75rem 1.5rem; background-color: #7a12d4; color: white;
  font-weight: 500; border-radius: 999px; text-decoration: none;
">Small CTA</a>
```

---

## Footer

### Simple Footer
```html
<footer class="mv-container" style="padding: 4rem 0; margin-top: 2rem; color: #6b7280;">
  © Mindvalley • Page Name
</footer>
```

### Footer with Links
```html
<footer style="background-color: #f9fafb; margin-top: 2rem;">
  <div class="mv-container" style="padding: 3rem 0;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
      <p class="body-sm" style="color: #6b7280; margin: 0;">
        © 2024 Mindvalley. All rights reserved.
      </p>
      <div style="display: flex; gap: 1.5rem;">
        <a href="#" class="body-sm" style="color: #6b7280; text-decoration: none;">Privacy</a>
        <a href="#" class="body-sm" style="color: #6b7280; text-decoration: none;">Terms</a>
        <a href="#" class="body-sm" style="color: #6b7280; text-decoration: none;">Contact</a>
      </div>
    </div>
  </div>
</footer>
```
