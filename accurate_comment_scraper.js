#!/usr/bin/env node

const puppeteer = require('puppeteer');

// Test URLs with known high comment counts
const testUrls = [
  'https://blog.mindvalley.com/newsletter-donald-trump/', // 523 responses
  'https://blog.mindvalley.com/newsletter-borderless/',   // 140 responses  
  'https://blog.mindvalley.com/newsletter-unity/',       // 1,256 responses
];

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getAccurateCommentCount(url) {
  const browser = await puppeteer.launch({ 
    headless: false, // Show browser to debug
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  try {
    console.log(`🔍 Scraping: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 45000 });
    
    const title = await page.title();
    console.log(`📄 ${title}`);
    
    // Wait for page to load
    await delay(5000);
    
    let commentCount = 0;
    let method = 'unknown';
    
    // Method 1: Look for response/comment count text (like "526 Responses")
    const countSelectors = [
      // Look for text patterns like "526 Responses", "140 Comments", etc.
      'text*="Responses"',
      'text*="Comments"', 
      'text*="responses"',
      'text*="comments"',
      'h2:contains("Responses")',
      'h3:contains("Responses")', 
      '.comment-count',
      '.response-count',
      '.comments-title',
      '.comment-header'
    ];
    
    for (const selector of countSelectors) {
      try {
        // Look for elements containing response/comment count
        const elements = await page.$$eval('*', (nodes) => {
          return nodes.filter(node => {
            const text = node.textContent || '';
            return /\d+\s*(response|comment|Response|Comment)s?/.test(text);
          }).map(node => node.textContent.trim());
        });
        
        if (elements.length > 0) {
          for (const text of elements) {
            const match = text.match(/(\d+)\s*(response|comment|Response|Comment)s?/);
            if (match) {
              const count = parseInt(match[1]);
              if (count > commentCount) {
                commentCount = count;
                method = `count-text: "${text}"`;
                console.log(`✅ Found count in text: "${text}" = ${count}`);
              }
            }
          }
          if (commentCount > 0) break;
        }
      } catch (e) {
        // Try next method
      }
    }
    
    // Method 2: Look for specific comment count elements
    if (commentCount === 0) {
      const specificSelectors = [
        '.comments-title',
        '.comment-reply-title', 
        '.comments-number',
        'h2[class*="comment"]',
        'h3[class*="comment"]',
        '[data-comment-count]'
      ];
      
      for (const selector of specificSelectors) {
        try {
          const element = await page.$(selector);
          if (element) {
            const text = await page.evaluate(el => el.textContent, element);
            const match = text.match(/(\d+)/);
            if (match) {
              const count = parseInt(match[1]);
              if (count > commentCount) {
                commentCount = count;
                method = `element: ${selector} = "${text}"`;
                console.log(`✅ Found count in element: ${selector} = "${text}"`);
              }
            }
          }
        } catch (e) {
          // Continue
        }
      }
    }
    
    // Method 3: Count individual comment elements (fallback)
    if (commentCount === 0) {
      console.log('🔄 Fallback: Counting individual comment elements...');
      
      const commentSelectors = [
        '.comment',
        '.comment-item', 
        '.wp-comment',
        '[data-comment-id]',
        '.comment-content',
        '.comment-body'
      ];
      
      for (const selector of commentSelectors) {
        try {
          const comments = await page.$$(selector);
          if (comments.length > commentCount) {
            commentCount = comments.length;
            method = `individual-count: ${selector}`;
            console.log(`✅ Counted individual elements: ${selector} = ${comments.length}`);
          }
        } catch (e) {
          // Continue
        }
      }
    }
    
    // Method 4: Check for Disqus iframe (last resort)
    if (commentCount === 0) {
      console.log('🔄 Checking for Disqus...');
      try {
        const disqusFrame = await page.$('#disqus_thread iframe');
        if (disqusFrame) {
          method = 'disqus-detected';
          commentCount = -1; // Mark as Disqus for special handling
        }
      } catch (e) {
        // Continue
      }
    }
    
    console.log(`📊 FINAL COUNT: ${commentCount} (method: ${method})`);
    console.log('---\n');
    
    return { 
      url, 
      title, 
      commentCount, 
      method,
      success: commentCount > 0 
    };
    
  } catch (error) {
    console.log(`❌ Error: ${error.message}`);
    return { url, title: 'Error', commentCount: 0, method: 'error', error: error.message };
  } finally {
    await browser.close();
  }
}

async function testAccurateCounting() {
  console.log('🎯 TESTING ACCURATE COMMENT COUNTING ON HIGH-ENGAGEMENT POSTS\n');
  
  const results = [];
  
  for (const url of testUrls) {
    const result = await getAccurateCommentCount(url);
    results.push(result);
  }
  
  console.log('🏆 ACCURATE COMMENT COUNT RESULTS:');
  console.log('=' .repeat(80));
  
  results.forEach((result, i) => {
    console.log(`${i + 1}. ${result.title}`);
    console.log(`   📊 ${result.commentCount} comments`);
    console.log(`   🔧 Method: ${result.method}`);
    console.log(`   ✅ Success: ${result.success}`);
    console.log(`   🔗 ${result.url}`);
    console.log('');
  });
  
  // Save results
  const fs = require('fs');
  const timestamp = new Date().toISOString().slice(0, 19).replace(/[:-]/g, '');
  const filename = `/Users/vishen/clawd/accurate_comments_${timestamp}.json`;
  
  fs.writeFileSync(filename, JSON.stringify(results, null, 2));
  console.log(`💾 Results saved to: ${filename}`);
  
  return results;
}

testAccurateCounting().catch(console.error);