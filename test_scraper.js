#!/usr/bin/env node

const puppeteer = require('puppeteer');

// Test with just 3 URLs
const testUrls = [
  'https://blog.mindvalley.com/newsletter-borderless/',  // Political topic - likely high engagement
  'https://blog.mindvalley.com/newsletter-social-media/',  // Business topic
  'https://blog.mindvalley.com/newsletter-kundalini/'     // Spiritual topic
];

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function quickScrapeComments(url) {
  const browser = await puppeteer.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  try {
    console.log(`🔍 Scraping: ${url}`);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    
    const title = await page.title();
    console.log(`📄 Title: ${title}`);
    
    // Simple comment detection
    await delay(2000);
    
    // Check for common comment indicators
    const commentIndicators = [
      '#disqus_thread',
      '.comments-section', 
      '.comment-list',
      '.wp-comment',
      '.fb-comments'
    ];
    
    let foundComments = false;
    let commentCount = 0;
    
    for (const selector of commentIndicators) {
      try {
        const element = await page.$(selector);
        if (element) {
          foundComments = true;
          console.log(`✅ Found comment section: ${selector}`);
          
          // Try to count visible comments
          const comments = await page.$$(`${selector} .comment, ${selector} [data-comment]`);
          commentCount = comments.length;
          
          if (commentCount === 0) {
            // Try other selectors within this section
            const altSelectors = ['.post-content', '.comment-item', '.comment-body'];
            for (const altSel of altSelectors) {
              const altComments = await page.$$(`${selector} ${altSel}`);
              if (altComments.length > 0) {
                commentCount = altComments.length;
                break;
              }
            }
          }
          break;
        }
      } catch (e) {
        // Continue to next selector
      }
    }
    
    if (!foundComments) {
      console.log(`❌ No comment section found`);
    } else {
      console.log(`📊 Found ${commentCount} comments`);
    }
    
    console.log('---');
    return { url, title, commentCount, hasComments: foundComments };
    
  } catch (error) {
    console.log(`❌ Error: ${error.message}`);
    return { url, title: 'Error', commentCount: 0, error: error.message };
  } finally {
    await browser.close();
  }
}

async function testScraper() {
  console.log('🧪 Testing comment scraper with 3 URLs...\n');
  
  const results = [];
  
  for (const url of testUrls) {
    const result = await quickScrapeComments(url);
    results.push(result);
    await delay(1000);
  }
  
  console.log('\n📊 TEST RESULTS:');
  results.forEach((result, i) => {
    console.log(`${i + 1}. ${result.title.substring(0, 50)}...`);
    console.log(`   Comments: ${result.commentCount}`);
    console.log(`   URL: ${result.url}`);
    console.log('');
  });
  
  return results;
}

testScraper().catch(console.error);