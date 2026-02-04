# FAQ Section Patterns

## Table of Contents
1. [FAQ Accordion with Schema.org](#faq-accordion-with-schemaorg) - SEO-optimized FAQ
2. [Two-Column FAQ](#two-column-faq) - Side-by-side layout
3. [Categorized FAQ](#categorized-faq) - Grouped by topic

---

## FAQ Accordion with Schema.org

Best for: Sales pages, program pages. Includes Schema.org FAQPage markup for SEO/AEO.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="max-width: 48rem; margin: 0 auto;">
      <!-- Section Header -->
      <div style="text-align: center; margin-bottom: 3rem;">
        <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">
          FAQ
        </p>
        <h2 class="title-bold-3" style="color: #0f131a;">
          Frequently Asked Questions
        </h2>
      </div>

      <!-- FAQ Items -->
      <div style="display: flex; flex-direction: column; gap: 1rem;">
        <!-- FAQ 1 -->
        <details style="background: white; border-radius: 12px; overflow: hidden;">
          <summary style="
            padding: 1.25rem 1.5rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            list-style: none;
          ">
            <span class="title-7" style="color: #0f131a;">{{QUESTION_1}}</span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2" style="flex-shrink: 0; transition: transform 0.2s;">
              <path d="M5 7.5l5 5 5-5"/>
            </svg>
          </summary>
          <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
            <p class="body" style="margin: 0;">{{ANSWER_1}}</p>
          </div>
        </details>

        <!-- FAQ 2 -->
        <details style="background: white; border-radius: 12px; overflow: hidden;">
          <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
            <span class="title-7" style="color: #0f131a;">{{QUESTION_2}}</span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2" style="flex-shrink: 0;"><path d="M5 7.5l5 5 5-5"/></svg>
          </summary>
          <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
            <p class="body" style="margin: 0;">{{ANSWER_2}}</p>
          </div>
        </details>

        <!-- FAQ 3 -->
        <details style="background: white; border-radius: 12px; overflow: hidden;">
          <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
            <span class="title-7" style="color: #0f131a;">{{QUESTION_3}}</span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2" style="flex-shrink: 0;"><path d="M5 7.5l5 5 5-5"/></svg>
          </summary>
          <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
            <p class="body" style="margin: 0;">{{ANSWER_3}}</p>
          </div>
        </details>

        <!-- FAQ 4 -->
        <details style="background: white; border-radius: 12px; overflow: hidden;">
          <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
            <span class="title-7" style="color: #0f131a;">{{QUESTION_4}}</span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2" style="flex-shrink: 0;"><path d="M5 7.5l5 5 5-5"/></svg>
          </summary>
          <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
            <p class="body" style="margin: 0;">{{ANSWER_4}}</p>
          </div>
        </details>

        <!-- FAQ 5 -->
        <details style="background: white; border-radius: 12px; overflow: hidden;">
          <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
            <span class="title-7" style="color: #0f131a;">{{QUESTION_5}}</span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2" style="flex-shrink: 0;"><path d="M5 7.5l5 5 5-5"/></svg>
          </summary>
          <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
            <p class="body" style="margin: 0;">{{ANSWER_5}}</p>
          </div>
        </details>
      </div>

      <!-- Contact CTA -->
      <div style="text-align: center; margin-top: 2rem;">
        <p class="body" style="color: #6b7280;">
          Still have questions? <a href="{{CONTACT_URL}}" style="color: #7a12d4; text-decoration: underline;">Contact our support team</a>
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Schema.org FAQPage Markup (add to <head> or before </body>) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{QUESTION_1}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_1}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{QUESTION_2}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_2}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{QUESTION_3}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_3}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{QUESTION_4}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_4}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{QUESTION_5}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER_5}}"
      }
    }
  ]
}
</script>

<!-- Optional: Rotate chevron on open -->
<style>
details[open] summary svg {
  transform: rotate(180deg);
}
details summary::-webkit-details-marker {
  display: none;
}
</style>
```

---

## Two-Column FAQ

Best for: Longer FAQ lists, landing pages.

```html
<section class="mv-container" style="padding: 5rem 0;">
  <div style="text-align: center; margin-bottom: 3rem;">
    <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">FAQ</p>
    <h2 class="title-bold-3" style="color: #0f131a;">Common Questions</h2>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
    <!-- Left Column -->
    <div style="display: flex; flex-direction: column; gap: 2rem;">
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_1}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_1}}</p>
      </div>
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_2}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_2}}</p>
      </div>
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_3}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_3}}</p>
      </div>
    </div>

    <!-- Right Column -->
    <div style="display: flex; flex-direction: column; gap: 2rem;">
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_4}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_4}}</p>
      </div>
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_5}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_5}}</p>
      </div>
      <div>
        <h3 class="title-7" style="color: #0f131a; margin-bottom: 0.5rem;">{{QUESTION_6}}</h3>
        <p class="body" style="color: #4b5563; margin: 0;">{{ANSWER_6}}</p>
      </div>
    </div>
  </div>
</section>
```

---

## Categorized FAQ

Best for: Complex products, membership pages with many questions.

```html
<section style="background: #f9f7fc; padding: 5rem 0;">
  <div class="mv-container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <p class="overline-text" style="color: #7a12d4; margin-bottom: 0.75rem;">FAQ</p>
      <h2 class="title-bold-3" style="color: #0f131a;">Everything You Need to Know</h2>
    </div>

    <div style="max-width: 48rem; margin: 0 auto;">
      <!-- Category 1: Getting Started -->
      <div style="margin-bottom: 2.5rem;">
        <h3 class="title-bold-6" style="color: #7a12d4; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e8e0f0;">
          Getting Started
        </h3>
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <details style="background: white; border-radius: 12px; overflow: hidden;">
            <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
              <span class="title-7" style="color: #0f131a;">{{GS_QUESTION_1}}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2"><path d="M5 7.5l5 5 5-5"/></svg>
            </summary>
            <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
              <p class="body" style="margin: 0;">{{GS_ANSWER_1}}</p>
            </div>
          </details>
          <details style="background: white; border-radius: 12px; overflow: hidden;">
            <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
              <span class="title-7" style="color: #0f131a;">{{GS_QUESTION_2}}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2"><path d="M5 7.5l5 5 5-5"/></svg>
            </summary>
            <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
              <p class="body" style="margin: 0;">{{GS_ANSWER_2}}</p>
            </div>
          </details>
        </div>
      </div>

      <!-- Category 2: Billing & Pricing -->
      <div style="margin-bottom: 2.5rem;">
        <h3 class="title-bold-6" style="color: #7a12d4; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e8e0f0;">
          Billing & Pricing
        </h3>
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <details style="background: white; border-radius: 12px; overflow: hidden;">
            <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
              <span class="title-7" style="color: #0f131a;">{{BP_QUESTION_1}}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2"><path d="M5 7.5l5 5 5-5"/></svg>
            </summary>
            <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
              <p class="body" style="margin: 0;">{{BP_ANSWER_1}}</p>
            </div>
          </details>
          <details style="background: white; border-radius: 12px; overflow: hidden;">
            <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
              <span class="title-7" style="color: #0f131a;">{{BP_QUESTION_2}}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2"><path d="M5 7.5l5 5 5-5"/></svg>
            </summary>
            <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
              <p class="body" style="margin: 0;">{{BP_ANSWER_2}}</p>
            </div>
          </details>
        </div>
      </div>

      <!-- Category 3: Support -->
      <div>
        <h3 class="title-bold-6" style="color: #7a12d4; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e8e0f0;">
          Support
        </h3>
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <details style="background: white; border-radius: 12px; overflow: hidden;">
            <summary style="padding: 1.25rem 1.5rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none;">
              <span class="title-7" style="color: #0f131a;">{{SUP_QUESTION_1}}</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#7a12d4" stroke-width="2"><path d="M5 7.5l5 5 5-5"/></svg>
            </summary>
            <div style="padding: 0 1.5rem 1.25rem; color: #4b5563;">
              <p class="body" style="margin: 0;">{{SUP_ANSWER_1}}</p>
            </div>
          </details>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## AEO-Optimized Answer Format

For AI/LLM discoverability, structure answers with the key point first:

```
❌ Bad: "Many of our students have found that the program works best when..."

✅ Good: "Yes, the program is designed for beginners. No prior experience is required. You'll start with foundational concepts and progress at your own pace."
```

**Answer structure:**
1. Direct answer (yes/no/the key fact)
2. Supporting detail
3. Additional context if needed
