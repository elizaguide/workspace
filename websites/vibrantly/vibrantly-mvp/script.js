// Global state
const state = {
    selectedGoals: [],
    userProfile: {},
    currentScreen: 'welcome-screen'
};

// Screen navigation
function goToScreen(screenId) {
    // Hide current screen
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    
    // Show new screen
    document.getElementById(screenId).classList.add('active');
    state.currentScreen = screenId;
    
    // Scroll to top
    window.scrollTo(0, 0);
}

// Goals selection logic
document.addEventListener('DOMContentLoaded', function() {
    // Initialize goal selection
    initGoalSelection();
    
    // Initialize skin tone selection
    initSkinToneSelection();
    
    // Set example data for Vishen
    setExampleData();
});

function initGoalSelection() {
    const goalCards = document.querySelectorAll('.goal-card');
    const selectedGoalsList = document.getElementById('selected-goals-list');
    const nextButton = document.getElementById('goals-next-btn');
    
    goalCards.forEach(card => {
        card.addEventListener('click', function() {
            const goal = this.dataset.goal;
            
            if (this.classList.contains('selected')) {
                // Deselect goal
                this.classList.remove('selected');
                state.selectedGoals = state.selectedGoals.filter(g => g !== goal);
            } else {
                // Select goal (max 3)
                if (state.selectedGoals.length < 3) {
                    this.classList.add('selected');
                    state.selectedGoals.push(goal);
                } else {
                    // Show message about max 3 goals
                    showNotification('You can select up to 3 primary goals', 'warning');
                }
            }
            
            updateSelectedGoalsList();
            updateNextButton();
        });
    });
}

function updateSelectedGoalsList() {
    const selectedGoalsList = document.getElementById('selected-goals-list');
    
    if (state.selectedGoals.length === 0) {
        selectedGoalsList.innerHTML = '<p style="color: var(--text-gray);">No goals selected yet</p>';
        return;
    }
    
    const goalNames = {
        'fat-loss': 'Lose Body Fat',
        'muscle-gain': 'Build Muscle', 
        'energy': 'Boost Energy',
        'cognitive': 'Mental Clarity',
        'stress': 'Stress Resilience',
        'sleep': 'Sleep Quality',
        'longevity': 'Anti-Aging',
        'immune': 'Immune Support',
        'recovery': 'Exercise Recovery'
    };
    
    selectedGoalsList.innerHTML = state.selectedGoals.map(goal => 
        `<div class="selected-goal-tag">${goalNames[goal]}</div>`
    ).join('');
}

function updateNextButton() {
    const nextButton = document.getElementById('goals-next-btn');
    nextButton.disabled = state.selectedGoals.length === 0;
}

function initSkinToneSelection() {
    const skinOptions = document.querySelectorAll('.skin-option');
    
    skinOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Remove selected class from all options
            skinOptions.forEach(opt => opt.classList.remove('selected'));
            
            // Add selected class to clicked option
            this.classList.add('selected');
            
            // Store selection
            state.userProfile.skinTone = this.dataset.tone;
        });
    });
}

function setExampleData() {
    // Pre-populate with Vishen's data
    state.selectedGoals = ['fat-loss', 'muscle-gain', 'cognitive'];
    state.userProfile = {
        age: 49,
        gender: 'male',
        weight: 80,
        height: 175,
        location: 'London, UK',
        skinTone: '3',
        activityLevel: 'active'
    };
}

// Utility functions
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${type === 'warning' ? 'exclamation-triangle' : 'info-circle'}"></i>
            <span>${message}</span>
        </div>
    `;
    
    // Add styles for notification
    const style = document.createElement('style');
    style.textContent = `
        .notification {
            position: fixed;
            top: 24px;
            right: 24px;
            background: white;
            padding: 16px 24px;
            border-radius: 12px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            border-left: 4px solid var(--primary-color);
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }
        
        .notification-warning {
            border-left-color: var(--warning-color);
        }
        
        .notification-content {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-dark);
        }
        
        .notification-content i {
            color: var(--primary-color);
        }
        
        .notification-warning .notification-content i {
            color: var(--warning-color);
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(notification);
    
    // Animate in
    requestAnimationFrame(() => {
        notification.style.transform = 'translateX(0)';
    });
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Form validation and data collection
function collectProfileData() {
    state.userProfile = {
        age: parseInt(document.getElementById('age').value) || 49,
        gender: document.getElementById('gender').value,
        weight: parseInt(document.getElementById('weight').value) || 80,
        height: parseInt(document.getElementById('height').value) || 175,
        location: document.getElementById('location').value || 'London, UK',
        skinTone: document.querySelector('.skin-option.selected')?.dataset.tone || '3',
        activityLevel: document.getElementById('activity-level').value
    };
    
    console.log('Profile data collected:', state.userProfile);
}

// Pre-select example goals for demo
setTimeout(() => {
    if (state.selectedGoals.length > 0) {
        // Pre-select the goals
        state.selectedGoals.forEach(goal => {
            const card = document.querySelector(`[data-goal="${goal}"]`);
            if (card) {
                card.classList.add('selected');
            }
        });
        
        updateSelectedGoalsList();
        updateNextButton();
    }
}, 100);

// Add smooth scrolling for better UX
document.documentElement.style.scrollBehavior = 'smooth';

// Add loading states for transitions
function showLoading() {
    const loader = document.createElement('div');
    loader.id = 'global-loader';
    loader.innerHTML = `
        <div class="loader-content">
            <div class="spinner"></div>
            <p>Analyzing your profile...</p>
        </div>
    `;
    
    const style = document.createElement('style');
    style.textContent = `
        #global-loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        }
        
        .loader-content {
            text-align: center;
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid var(--border-color);
            border-left-color: var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 16px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .loader-content p {
            color: var(--text-gray);
            font-weight: 500;
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(loader);
}

function hideLoading() {
    const loader = document.getElementById('global-loader');
    if (loader) {
        document.body.removeChild(loader);
    }
}

// Enhanced navigation with loading states
function navigateWithLoading(targetScreen, delay = 1000) {
    showLoading();
    
    setTimeout(() => {
        hideLoading();
        goToScreen(targetScreen);
    }, delay);
}

// Bloodwork handling
function triggerFileUpload() {
    document.getElementById('file-input').click();
}

function loadExampleBloodwork() {
    state.bloodwork = {
        hba1c: 4.9,
        totalCholesterol: 241.1,
        ldl: 170.98,
        hdl: 51.14,
        testosterone: 30.5,
        vitaminD: 41.8,
        ferritin: 220,
        b12: 843
    };
    
    document.getElementById('bloodwork-continue-btn').disabled = false;
    showNotification('Example bloodwork loaded successfully', 'info');
}

// Supplement option selection
function selectSupplementOption(option) {
    // Remove selected class from all options
    document.querySelectorAll('.option-card').forEach(card => {
        card.classList.remove('selected');
    });
    
    // Add selected class to clicked option
    event.target.closest('.option-card').classList.add('selected');
    
    // Hide all input sections
    document.querySelectorAll('.input-section').forEach(section => {
        section.style.display = 'none';
    });
    
    // Show relevant input section
    if (option === 'photo') {
        document.getElementById('photo-upload-section').style.display = 'block';
    } else if (option === 'manual') {
        document.getElementById('manual-entry-section').style.display = 'block';
    }
    
    state.supplementOption = option;
}

function loadExampleSupplements() {
    // Load Vishen's supplement stack
    state.currentSupplements = [
        'Alpha GPC 300mg',
        'L-Carnitine 1500mg', 
        'CoQ10 200mg',
        'Berberine 500mg',
        'Omega-3 1g',
        'Vitamin D3/K2',
        'Creatine 5g',
        'Collagen 10g',
        'Glycine 3g',
        'Lion\'s Mane 1000mg'
    ];
    
    showNotification('Loaded example supplement stack', 'info');
}

// Doctor conversation
function selectDoctorOption(option) {
    // Remove selected class from all options
    document.querySelectorAll('.option-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    // Add selected class to clicked option
    event.target.classList.add('selected');
    
    state.doctorChoice = option;
    
    // Show follow-up based on choice
    setTimeout(() => {
        showDoctorFollowup(option);
    }, 1000);
}

function showDoctorFollowup(choice) {
    const conversation = document.querySelector('.doctor-conversation');
    let followupMessage = '';
    
    switch(choice) {
        case 'increase-berberine':
            followupMessage = '<p><strong>Excellent choice.</strong> Increasing to 1500mg daily will provide better lipid management. Take 500mg with each main meal for optimal absorption and glucose control.</p>';
            break;
        case 'add-red-yeast':
            followupMessage = '<p><strong>Good thinking.</strong> Red yeast rice contains natural statins and works synergistically with berberine. We\'ll start with 600mg twice daily with meals.</p>';
            break;
        case 'current-dosing':
            followupMessage = '<p><strong>Conservative approach.</strong> Let\'s monitor for 8 weeks and reassess. We\'ll focus on optimizing your current stack timing and add other cardiovascular support.</p>';
            break;
    }
    
    const followup = document.createElement('div');
    followup.className = 'doctor-message followup';
    followup.innerHTML = followupMessage;
    conversation.appendChild(followup);
    
    // Scroll to show new message
    followup.scrollIntoView({ behavior: 'smooth' });
}

// Tier selection
function selectTier(tier) {
    // Update tier buttons
    document.querySelectorAll('.tier-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // Update stack content
    document.querySelectorAll('.stack-content').forEach(content => {
        content.classList.remove('active');
    });
    document.getElementById(`${tier}-stack`).classList.add('active');
    
    state.selectedTier = tier;
}

// Subscription modal
function showSubscriptionModal() {
    const modal = document.createElement('div');
    modal.className = 'subscription-modal';
    modal.innerHTML = `
        <div class="modal-overlay" onclick="closeSubscriptionModal()"></div>
        <div class="modal-content">
            <div class="modal-header">
                <h3>Start Your Vibrantly Journey</h3>
                <button onclick="closeSubscriptionModal()" class="close-btn">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="subscription-plans">
                    <div class="plan">
                        <h4>Basic Plan</h4>
                        <div class="price">$29/month</div>
                        <ul>
                            <li>Basic stack recommendations</li>
                            <li>Monthly optimization reviews</li>
                            <li>Email support</li>
                        </ul>
                        <button class="btn-secondary">Choose Basic</button>
                    </div>
                    
                    <div class="plan featured">
                        <h4>Advanced Plan</h4>
                        <div class="price">$69/month</div>
                        <ul>
                            <li>Advanced + Biohacker stacks</li>
                            <li>Weekly optimization</li>
                            <li>Bloodwork analysis</li>
                            <li>Priority support</li>
                        </ul>
                        <button class="btn-primary">Choose Advanced</button>
                    </div>
                    
                    <div class="plan">
                        <h4>Pro Plan</h4>
                        <div class="price">$149/month</div>
                        <ul>
                            <li>Everything in Advanced</li>
                            <li>1-on-1 consultations</li>
                            <li>Custom protocols</li>
                            <li>Vibrantly Food integration</li>
                        </ul>
                        <button class="btn-secondary">Choose Pro</button>
                    </div>
                </div>
                
                <div class="modal-footer">
                    <p>✨ 30-day money-back guarantee • Cancel anytime</p>
                </div>
            </div>
        </div>
    `;
    
    // Add modal styles
    const modalStyles = document.createElement('style');
    modalStyles.textContent = `
        .subscription-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
        }
        
        .modal-content {
            background: white;
            border-radius: 16px;
            max-width: 900px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            z-index: 1;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 32px;
            border-bottom: 1px solid var(--border-color);
        }
        
        .modal-header h3 {
            margin: 0;
            font-size: 1.5rem;
        }
        
        .close-btn {
            background: none;
            border: none;
            font-size: 1.2rem;
            cursor: pointer;
            padding: 8px;
            border-radius: 50%;
            transition: var(--transition);
        }
        
        .close-btn:hover {
            background: var(--bg-secondary);
        }
        
        .modal-body {
            padding: 32px;
        }
        
        .subscription-plans {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 24px;
            margin-bottom: 32px;
        }
        
        .plan {
            border: 2px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            transition: var(--transition);
        }
        
        .plan.featured {
            border-color: var(--primary-color);
            transform: scale(1.05);
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
            color: white;
        }
        
        .plan h4 {
            font-size: 1.3rem;
            margin-bottom: 16px;
        }
        
        .price {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 24px;
        }
        
        .plan ul {
            list-style: none;
            padding: 0;
            margin-bottom: 24px;
        }
        
        .plan li {
            padding: 8px 0;
            border-bottom: 1px solid var(--border-color);
        }
        
        .plan.featured li {
            border-bottom-color: rgba(255, 255, 255, 0.2);
        }
        
        .modal-footer {
            text-align: center;
            color: var(--text-gray);
        }
    `;
    
    document.head.appendChild(modalStyles);
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

function closeSubscriptionModal() {
    const modal = document.querySelector('.subscription-modal');
    if (modal) {
        document.body.removeChild(modal);
        document.body.style.overflow = 'auto';
    }
}

// File upload handling
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const files = e.target.files;
            if (files.length > 0) {
                showNotification(`${files.length} file(s) uploaded successfully`, 'info');
                document.getElementById('bloodwork-continue-btn').disabled = false;
            }
        });
    }
});

// Enhanced state management
function updateState(key, value) {
    state[key] = value;
    console.log(`State updated: ${key}`, value);
}

// Navigation with form data collection
function proceedToAnalysis() {
    collectProfileData();
    updateState('profileComplete', true);
    goToScreen('bloodwork-screen');
}

// Console logging for development
console.log('Vibrantly Supplements MVP Initialized');
console.log('Example user goals:', state.selectedGoals);
console.log('Example user profile:', state.userProfile);

// Add some demo data for the MVP
setTimeout(() => {
    // Pre-load some example data
    if (state.currentScreen === 'welcome-screen') {
        console.log('MVP Demo Mode: Example data will be pre-loaded');
    }
}, 2000);