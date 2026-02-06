#!/usr/bin/env node

const puppeteer = require('puppeteer');

// All newsletter blog URLs (starting with subset for testing)
const blogUrls = [
  'https://blog.mindvalley.com/newsletter-social-media/',
  'https://blog.mindvalley.com/newsletter-kundalini/',
  'https://blog.mindvalley.com/the-art-of-quantum-jumping/',
  'https://blog.mindvalley.com/the-wealth-thermostat/',
  'https://blog.mindvalley.com/newsletter-subconscious/',
  'https://blog.mindvalley.com/unity-evolution-of-consciousness/',
  'https://blog.mindvalley.com/in-memory-of-bob-proctor/',
  'https://blog.mindvalley.com/newsletter-manifestation/',
  'https://blog.mindvalley.com/newsletter-gifts/',
  'https://blog.mindvalley.com/newsletter-parenting/',
  'https://blog.mindvalley.com/newsletter-wwkd/',
  'https://blog.mindvalley.com/newsletter-borderless/',
  'https://blog.mindvalley.com/newsletter-surrender/',
  'https://blog.mindvalley.com/newsletter-the-earth-flag/',
  'https://blog.mindvalley.com/newsletter-breakthroughs/',
  'https://blog.mindvalley.com/newsletter-eywa/',
  'https://blog.mindvalley.com/newsletter-bruce-lee/',
  'https://blog.mindvalley.com/newsletter-mindvalley-u/',
  'https://blog.mindvalley.com/newsletter-events/',
  'https://blog.mindvalley.com/newsletter-manifesting/',
  'https://blog.mindvalley.com/job-your-love/',
  'https://blog.mindvalley.com/humans-want-humans/',
  'https://blog.mindvalley.com/the-lie-about-your-neighbor/',
  'https://blog.mindvalley.com/how-one-habit-can-change-everything/'
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
    console.log(`🔍 Scraping: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
    
    // Wait for page to load
    await delay(3000);
    
    // Get page title
    const title = await page.title();
    
    // Try multiple comment section selectors
    const commentSelectors = [
      '#disqus_thread',
      '.disqus-comment',
      '.comment-list',
      '.comments-section',
      '.wp-comment',
      '.comment',
      '[data-comment]',
      '.fb-comments',
      '.comments'
    ];
    
    let commentSection = null;
    for (const selector of commentSelectors) {
      try {
        await page.waitForSelector(selector, { timeout: 5000 });
        commentSection = selector;
        console.log(`✅ Found comment section: ${selector}`);
        break;
      } catch (e) {
        // Try next selector
      }
    }
    
    if (!commentSection) {
      console.log(`❌ No comment section found for: ${url}`);
      return { url, title, commentCount: 0, error: 'No comment section found' };
    }
    
    let commentCount = 0;
    
    // Handle Disqus comments
    if (commentSection.includes('disqus')) {
      try {
        console.log(`🔄 Loading Disqus comments...`);
        await delay(5000); // Give Disqus time to load
        
        // Try to find comment count in Disqus
        const disqusCountSelectors = [
          '.disqus-comment-count',
          '#disqus-comment-header .comments-count',
          '.comment-count'
        ];
        
        for (const selector of disqusCountSelectors) {
          try {
            const countElement = await page.$(selector);
            if (countElement) {
              const countText = await page.evaluate(el => el.textContent, countElement);
              const count = parseInt(countText.match(/\d+/)?.[0] || '0');
              if (count > 0) {
                commentCount = count;
                break;
              }
            }
          } catch (e) {
            // Continue to next selector
          }
        }
        
        // If no count found, try to access iframe
        if (commentCount === 0) {
          const frames = await page.frames();
          let disqusFrame = null;
          
          for (const frame of frames) {
            const frameUrl = frame.url();
            if (frameUrl.includes('disqus.com')) {
              disqusFrame = frame;
              break;
            }
          }
          
          if (disqusFrame) {
            try {
              await delay(3000);
              const comments = await disqusFrame.$$('.post-content');
              commentCount = comments.length;
            } catch (e) {
              console.log(`⚠️  Could not access Disqus iframe: ${e.message}`);
            }
          }
        }
      } catch (e) {
        console.log(`⚠️  Disqus loading failed for ${url}: ${e.message}`);
      }
    } else {
      // Other comment systems
      try {
        // Click load more buttons
        let attempts = 0;
        const maxAttempts = 5;
        
        while (attempts < maxAttempts) {
          const loadMoreSelectors = [
            '.load-more-comments',
            '.show-more-comments',
            '.view-more-comments',
            'button[data-load-more]',
            '.loadmore',
            '.load-more'
          ];
          
          let clicked = false;
          for (const selector of loadMoreSelectors) {
            try {
              const button = await page.$(selector);
              if (button) {
                const isVisible = await page.evaluate(el => {
                  return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
                }, button);
                
                if (isVisible) {
                  await button.click();
                  await delay(2000);
                  clicked = true;
                  console.log(`🔄 Clicked load more button: ${selector}`);
                  break;
                }
              }
            } catch (e) {
              // Try next selector
            }
          }
          
          if (!clicked) break;
          attempts++;
        }
        
        // Count comments
        const commentCountSelectors = [
          '.comment-list .comment',
          '.comments .comment',
          '.comment-item',
          '.wp-comment',
          '[data-comment-id]',
          '.comment-content',
          '.comment-body'
        ];
        
        for (const selector of commentCountSelectors) {
          try {
            const comments = await page.$$(selector);
            if (comments.length > 0) {
              commentCount = comments.length;
              console.log(`📊 Found ${commentCount} comments using selector: ${selector}`);
              break;
            }
          } catch (e) {
            // Try next selector
          }
        }
      } catch (e) {
        console.log(`⚠️  Comment counting failed for ${url}: ${e.message}`);
      }
    }
    
    console.log(`📊 ${title.substring(0, 50)}...: ${commentCount} comments\n`);
    return { url, title, commentCount };
    
  } catch (error) {
    console.log(`❌ Error scraping ${url}: ${error.message}`);
    return { url, title: 'Error', commentCount: 0, error: error.message };
  } finally {
    await browser.close();
  }
}

async function scrapeAllComments() {
  console.log('🚀 Starting comment scraping for Mindvalley newsletters...\n');
  
  const results = [];
  
  // Process URLs one by one to avoid overwhelming the server
  for (let i = 0; i < blogUrls.length; i++) {
    const url = blogUrls[i];
    console.log(`[${i + 1}/${blogUrls.length}] Processing: ${url.split('/')[3] || url}`);
    
    const result = await scrapeComments(url);
    results.push(result);
    
    // Brief pause between requests
    await delay(2000);
  }
  
  // Sort by comment count (highest first)
  const sortedResults = results.sort((a, b) => b.commentCount - a.commentCount);
  
  console.log('\n🏆 TOP 5 NEWSLETTERS BY COMMENT ENGAGEMENT:');
  console.log('=' .repeat(80));
  
  for (let i = 0; i < Math.min(5, sortedResults.length); i++) {
    const result = sortedResults[i];
    console.log(`${i + 1}. ${result.title}`);
    console.log(`   Comments: ${result.commentCount}`);
    console.log(`   URL: ${result.url}`);
    console.log('');
  }
  
  console.log('\n📈 ALL RESULTS (sorted by comment count):');
  console.log('=' .repeat(80));
  
  sortedResults.forEach((result, index) => {
    console.log(`${index + 1}. ${result.commentCount} comments - ${result.title.substring(0, 60)}...`);
  });
  
  // Save complete results to file
  const fs = require('fs');
  const timestamp = new Date().toISOString().slice(0, 19).replace(/[:-]/g, '');
  const filename = `/Users/vishen/clawd/comment_analysis_${timestamp}.json`;
  
  fs.writeFileSync(filename, JSON.stringify(sortedResults, null, 2));
  console.log(`\n💾 Complete results saved to: ${filename}`);
  
  return sortedResults;
}

// Run the scraper
if (require.main === module) {
  scrapeAllComments().catch(console.error);
}

module.exports = { scrapeAllComments, scrapeComments };