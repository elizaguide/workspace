#!/usr/bin/env node

const puppeteer = require('puppeteer');

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function deepScrapeComments(url) {
  const browser = await puppeteer.launch({ 
    headless: false, // Show browser to see what's happening
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  try {
    console.log(`🔍 Deep scraping: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 45000 });
    
    const title = await page.title();
    console.log(`📄 ${title}`);
    
    // Wait for page to fully load
    await delay(5000);
    
    let commentCount = 0;
    let totalClicks = 0;
    const maxClicks = 50; // Prevent infinite loops
    
    // Check for Disqus first
    const disqusPresent = await page.$('#disqus_thread');
    
    if (disqusPresent) {
      console.log('🎯 Found Disqus - handling iframe...');
      
      // Wait for Disqus to load
      await delay(8000);
      
      // Try to find Disqus iframe
      let disqusFrame = null;
      let attempts = 0;
      
      while (!disqusFrame && attempts < 10) {
        const frames = await page.frames();
        for (const frame of frames) {
          const frameUrl = frame.url();
          if (frameUrl.includes('disqus.com') && frameUrl.includes('embed')) {
            disqusFrame = frame;
            console.log('✅ Found Disqus iframe');
            break;
          }
        }
        if (!disqusFrame) {
          await delay(2000);
          attempts++;
        }
      }
      
      if (disqusFrame) {
        // Click "Load More" in Disqus repeatedly
        let loadingMore = true;
        
        while (loadingMore && totalClicks < maxClicks) {
          try {
            // Look for various "load more" button selectors in Disqus
            const loadMoreSelectors = [
              'button[data-action="load-more"]',
              '.load-more',
              '.post-list__load-more',
              'button:contains("Load more")',
              'a:contains("Load more")',
              '[aria-label*="Load more"]'
            ];
            
            let clicked = false;
            for (const selector of loadMoreSelectors) {
              try {
                const button = await disqusFrame.$(selector);
                if (button) {
                  const isVisible = await disqusFrame.evaluate(el => {
                    const style = window.getComputedStyle(el);
                    return style.display !== 'none' && style.visibility !== 'hidden' && el.offsetHeight > 0;
                  }, button);
                  
                  if (isVisible) {
                    await button.click();
                    console.log(`🔄 Clicked load more (${totalClicks + 1})`);
                    await delay(3000); // Wait for new comments to load
                    clicked = true;
                    totalClicks++;
                    break;
                  }
                }
              } catch (e) {
                // Try next selector
              }
            }
            
            if (!clicked) {
              loadingMore = false;
            }
          } catch (e) {
            loadingMore = false;
          }
        }
        
        // Count all comments in Disqus
        try {
          const commentSelectors = [
            '.post-content',
            '[data-role="post-content"]', 
            '.post',
            '.comment'
          ];
          
          for (const selector of commentSelectors) {
            const comments = await disqusFrame.$$(selector);
            if (comments.length > commentCount) {
              commentCount = comments.length;
            }
          }
        } catch (e) {
          console.log('⚠️  Error counting Disqus comments:', e.message);
        }
      }
    } else {
      console.log('🎯 Non-Disqus comment system - handling pagination...');
      
      // Handle other comment systems with pagination
      let loadingMore = true;
      
      while (loadingMore && totalClicks < maxClicks) {
        const loadMoreSelectors = [
          '.load-more-comments',
          '.show-more-comments', 
          '.view-more-comments',
          '.loadmore',
          'button[data-load-more]',
          '.more-comments',
          'a:contains("Load more")',
          'button:contains("Load more")',
          'button:contains("Show more")',
          '.pagination .next',
          '.comment-nav-below .nav-next a'
        ];
        
        let clicked = false;
        for (const selector of loadMoreSelectors) {
          try {
            const button = await page.$(selector);
            if (button) {
              const isVisible = await page.evaluate(el => {
                const style = window.getComputedStyle(el);
                return style.display !== 'none' && style.visibility !== 'hidden' && el.offsetHeight > 0;
              }, button);
              
              if (isVisible) {
                await button.click();
                console.log(`🔄 Clicked pagination (${totalClicks + 1})`);
                await delay(3000);
                clicked = true;
                totalClicks++;
                break;
              }
            }
          } catch (e) {
            // Try next selector
          }
        }
        
        if (!clicked) {
          loadingMore = false;
        }
      }
      
      // Count all visible comments
      const commentSelectors = [
        '.comment-list .comment',
        '.comments .comment',
        '.comment-item',
        '.wp-comment',
        '.comment-content',
        '[data-comment-id]'
      ];
      
      for (const selector of commentSelectors) {
        try {
          const comments = await page.$$(selector);
          if (comments.length > commentCount) {
            commentCount = comments.length;
          }
        } catch (e) {
          // Try next selector
        }
      }
    }
    
    console.log(`📊 TOTAL: ${commentCount} comments (after ${totalClicks} pagination clicks)`);
    console.log('---\n');
    
    return { url, title, commentCount, paginationClicks: totalClicks };
    
  } catch (error) {
    console.log(`❌ Error: ${error.message}`);
    return { url, title: 'Error', commentCount: 0, error: error.message };
  } finally {
    await browser.close();
  }
}

async function testDeepScraping() {
  // Test with the political newsletter that should have high engagement
  const testUrls = [
    'https://blog.mindvalley.com/newsletter-borderless/', // The 27-comment leader
    'https://blog.mindvalley.com/the-art-of-quantum-jumping/', // The 23-comment one
    'https://blog.mindvalley.com/newsletter-wwkd/' // The 22-comment one
  ];
  
  console.log('🔬 DEEP COMMENT ANALYSIS - Testing pagination handling...\n');
  
  const results = [];
  
  for (const url of testUrls) {
    const result = await deepScrapeComments(url);
    results.push(result);
  }
  
  console.log('🎯 DEEP SCRAPING RESULTS:');
  console.log('=' .repeat(80));
  results.forEach((result, i) => {
    console.log(`${i + 1}. ${result.title}`);
    console.log(`   📊 ${result.commentCount} total comments`);
    console.log(`   🔄 ${result.paginationClicks} pagination clicks needed`);
    console.log(`   🔗 ${result.url}`);
    console.log('');
  });
  
  return results;
}

testDeepScraping().catch(console.error);