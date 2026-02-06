#!/usr/bin/env node

const puppeteer = require('puppeteer');

// Expanded list focusing on high-engagement topics
const priorityUrls = [
  // Political/controversial (likely highest engagement)
  'https://blog.mindvalley.com/newsletter-borderless/',
  'https://blog.mindvalley.com/the-lie-about-your-neighbor/', 
  'https://blog.mindvalley.com/newsletter-wwkd/',
  
  // Business/entrepreneurship 
  'https://blog.mindvalley.com/newsletter-social-media/',
  'https://blog.mindvalley.com/job-your-love/',
  'https://blog.mindvalley.com/humans-want-humans/',
  
  // Personal development/spiritual
  'https://blog.mindvalley.com/newsletter-kundalini/',
  'https://blog.mindvalley.com/newsletter-manifestation/',
  'https://blog.mindvalley.com/newsletter-breakthroughs/',
  'https://blog.mindvalley.com/the-art-of-quantum-jumping/',
  
  // Relationships/parenting
  'https://blog.mindvalley.com/newsletter-parenting/',
  'https://blog.mindvalley.com/newsletter-mindvalley-u/',
  
  // Health/wellness  
  'https://blog.mindvalley.com/the-wealth-thermostat/',
  'https://blog.mindvalley.com/newsletter-subconscious/',
  'https://blog.mindvalley.com/how-one-habit-can-change-everything/',
  
  // Other topics
  'https://blog.mindvalley.com/newsletter-gifts/',
  'https://blog.mindvalley.com/newsletter-surrender/',
  'https://blog.mindvalley.com/newsletter-the-earth-flag/',
  'https://blog.mindvalley.com/newsletter-eywa/',
  'https://blog.mindvalley.com/newsletter-bruce-lee/',
  'https://blog.mindvalley.com/newsletter-events/',
  'https://blog.mindvalley.com/newsletter-manifesting/',
  'https://blog.mindvalley.com/unity-evolution-of-consciousness/',
  'https://blog.mindvalley.com/in-memory-of-bob-proctor/'
];

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function scrapeComments(url) {
  const browser = await puppeteer.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  try {
    console.log(`🔍 ${url.split('/')[3] || url.split('/').pop()}`);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    
    const title = await page.title();
    
    // Quick comment detection
    await delay(1500);
    
    const commentSelectors = [
      '.comment-list .comment',
      '.comments .comment', 
      '.wp-comment',
      '#disqus_thread .comment',
      '.comment-item'
    ];
    
    let commentCount = 0;
    let foundSection = false;
    
    // Try each selector
    for (const selector of commentSelectors) {
      try {
        const comments = await page.$$(selector);
        if (comments.length > 0) {
          commentCount = Math.max(commentCount, comments.length);
          foundSection = true;
        }
      } catch (e) {
        // Continue
      }
    }
    
    // Also check for comment section existence
    const sectionSelectors = ['#disqus_thread', '.comment-list', '.comments-section'];
    for (const selector of sectionSelectors) {
      try {
        const element = await page.$(selector);
        if (element && !foundSection) {
          foundSection = true;
          // If section exists but no comments counted, try alternative counting
          const altComments = await page.$$('.comment, [data-comment], .post-content');
          commentCount = Math.max(commentCount, altComments.length);
        }
      } catch (e) {
        // Continue
      }
    }
    
    console.log(`   📊 ${commentCount} comments - ${title.substring(0, 45)}...`);
    return { url, title, commentCount };
    
  } catch (error) {
    console.log(`   ❌ Error: ${error.message.substring(0, 50)}...`);
    return { url, title: 'Error', commentCount: 0, error: error.message };
  } finally {
    await browser.close();
  }
}

async function expandedScrape() {
  console.log('🚀 Scraping comment data from Mindvalley newsletters...\n');
  
  const results = [];
  
  for (let i = 0; i < priorityUrls.length; i++) {
    process.stdout.write(`[${i + 1}/${priorityUrls.length}] `);
    const result = await scrapeComments(priorityUrls[i]);
    results.push(result);
    await delay(800); // Brief pause between requests
  }
  
  // Sort by comment count
  const sorted = results.sort((a, b) => b.commentCount - a.commentCount);
  
  console.log('\n🏆 TOP 5 NEWSLETTERS BY COMMENT ENGAGEMENT:');
  console.log('=' .repeat(80));
  
  for (let i = 0; i < Math.min(5, sorted.length); i++) {
    const result = sorted[i];
    console.log(`${i + 1}. ${result.title}`);
    console.log(`   📊 ${result.commentCount} comments`);
    console.log(`   🔗 ${result.url}`);
    console.log('');
  }
  
  console.log('\n📈 COMPLETE RANKING:');
  console.log('=' .repeat(50));
  sorted.forEach((result, index) => {
    if (result.commentCount > 0) {
      console.log(`${index + 1}. ${result.commentCount} comments - ${result.title.substring(0, 50)}...`);
    }
  });
  
  // Save results
  const fs = require('fs');
  const timestamp = new Date().toISOString().slice(0, 19).replace(/[:-]/g, '');
  const filename = `/Users/vishen/clawd/newsletter_comments_${timestamp}.json`;
  
  fs.writeFileSync(filename, JSON.stringify(sorted, null, 2));
  console.log(`\n💾 Full results saved to: ${filename}`);
  
  return sorted;
}

expandedScrape().catch(console.error);