/**
 * VIBRANTLY SUPPLEMENTS - PREMIUM INTERACTIONS
 * World-class user experience with smooth animations and intelligent behavior
 */

// Enhanced Global State Management
const AppState = {
    currentScreen: 'welcome-screen',
    selectedGoals: [],
    userProfile: {},
    bloodworkData: null,
    currentSupplements: [],
    analysisResults: {},
    isLoading: false,
    hasCompletedOnboarding: false,
    
    // Analytics tracking
    interactions: [],
    startTime: Date.now(),
    
    // Animation states
    animationQueue: [],
    isAnimating: false
};

// Enhanced Animation System
class AnimationEngine {
    static ease = {
        easeOutCubic: 'cubic-bezier(0.33, 1, 0.68, 1)',
        easeOutQuart: 'cubic-bezier(0.25, 1, 0.5, 1)',
        easeOutExpo: 'cubic-bezier(0.19, 1, 0.22, 1)',
        bounceOut: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)'
    };

    static fadeIn(element, duration = 500, delay = 0) {
        return new Promise(resolve => {
            setTimeout(() => {
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px)';
                element.style.transition = `opacity ${duration}ms ${this.ease.easeOutCubic}, transform ${duration}ms ${this.ease.easeOutCubic}`;
                
                requestAnimationFrame(() => {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                });
                
                setTimeout(resolve, duration);
            }, delay);
        });
    }

    static slideIn(element, direction = 'left', duration = 400) {
        return new Promise(resolve => {
            const translateValue = direction === 'left' ? '-100%' : '100%';
            element.style.transform = `translateX(${translateValue})`;
            element.style.transition = `transform ${duration}ms ${this.ease.easeOutQuart}`;
            
            requestAnimationFrame(() => {
                element.style.transform = 'translateX(0)';
            });
            
            setTimeout(resolve, duration);
        });
    }

    static scale(element, fromScale = 0.8, toScale = 1, duration = 300) {
        return new Promise(resolve => {
            element.style.transform = `scale(${fromScale})`;
            element.style.transition = `transform ${duration}ms ${this.ease.bounceOut}`;
            
            requestAnimationFrame(() => {
                element.style.transform = `scale(${toScale})`;
            });
            
            setTimeout(resolve, duration);
        });
    }

    static ripple(element, event) {
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        const ripple = document.createElement('div');
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: rippleEffect 600ms ease-out;
            pointer-events: none;
            z-index: 1000;
        `;
        
        element.style.position = 'relative';
        element.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
}

// Enhanced Screen Navigation System
class ScreenManager {
    static transitions = new Map();
    
    static async goToScreen(targetScreenId, direction = 'forward') {
        if (AppState.isAnimating) return;
        
        AppState.isAnimating = true;
        const currentScreen = document.getElementById(AppState.currentScreen);
        const targetScreen = document.getElementById(targetScreenId);
        
        // Track interaction
        this.trackInteraction('screen_transition', {
            from: AppState.currentScreen,
            to: targetScreenId,
            direction
        });
        
        // Animate out current screen
        if (currentScreen) {
            await this.animateOut(currentScreen, direction);
            currentScreen.classList.remove('active');
        }
        
        // Show target screen
        targetScreen.classList.add('active');
        AppState.currentScreen = targetScreenId;
        
        // Animate in target screen
        await this.animateIn(targetScreen, direction);
        
        // Initialize screen-specific functionality
        this.initializeScreen(targetScreenId);
        
        AppState.isAnimating = false;
        
        // Update URL without reloading
        if (history.pushState) {
            history.pushState(null, null, `#${targetScreenId}`);
        }
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    static async animateOut(screen, direction) {
        const content = screen.querySelector('.screen-content, .hero-section');
        if (!content) return;
        
        const translateX = direction === 'forward' ? '-30px' : '30px';
        content.style.transition = 'opacity 300ms ease-out, transform 300ms ease-out';
        content.style.opacity = '0';
        content.style.transform = `translateX(${translateX})`;
        
        return new Promise(resolve => setTimeout(resolve, 300));
    }
    
    static async animateIn(screen, direction) {
        const content = screen.querySelector('.screen-content, .hero-section');
        if (!content) return;
        
        const translateX = direction === 'forward' ? '30px' : '-30px';
        content.style.opacity = '0';
        content.style.transform = `translateX(${translateX})`;
        content.style.transition = 'opacity 400ms ease-out, transform 400ms ease-out';
        
        await new Promise(resolve => setTimeout(resolve, 50));
        
        content.style.opacity = '1';
        content.style.transform = 'translateX(0)';
        
        return new Promise(resolve => setTimeout(resolve, 400));
    }
    
    static initializeScreen(screenId) {
        switch(screenId) {
            case 'goals-screen':
                this.initializeGoalsScreen();
                break;
            case 'profile-screen':
                this.initializeProfileScreen();
                break;
            case 'bloodwork-screen':
                this.initializeBloodworkScreen();
                break;
        }
    }
    
    static initializeGoalsScreen() {
        // Animate in goal cards with staggered delay
        const goalCards = document.querySelectorAll('.goal-card');
        goalCards.forEach((card, index) => {
            AnimationEngine.fadeIn(card, 400, index * 100);
        });
    }
    
    static initializeProfileScreen() {
        // Animate form sections
        const formSections = document.querySelectorAll('.form-row, .form-group');
        formSections.forEach((section, index) => {
            AnimationEngine.fadeIn(section, 300, index * 50);
        });
    }
    
    static initializeBloodworkScreen() {
        const uploadArea = document.querySelector('.upload-area');
        const benefitsItems = document.querySelectorAll('.benefits-list li');
        
        if (uploadArea) {
            AnimationEngine.fadeIn(uploadArea, 400);
        }
        
        benefitsItems.forEach((item, index) => {
            AnimationEngine.fadeIn(item, 300, index * 100);
        });
    }
    
    static trackInteraction(event, data) {
        AppState.interactions.push({
            event,
            data,
            timestamp: Date.now() - AppState.startTime
        });
    }
}

// Enhanced Goals System
class GoalsManager {
    static maxGoals = 3;
    static selectedGoals = new Set();
    
    static initialize() {
        const goalCards = document.querySelectorAll('.goal-card');
        const nextButton = document.getElementById('goals-next-btn');
        
        goalCards.forEach(card => {
            card.addEventListener('click', (e) => this.handleGoalSelection(e));
            card.addEventListener('mouseenter', (e) => this.handleGoalHover(e));
            card.addEventListener('mouseleave', (e) => this.handleGoalLeave(e));
        });
        
        // Pre-select example goals with animation
        setTimeout(() => {
            this.selectGoal('fat-loss');
            setTimeout(() => this.selectGoal('muscle-gain'), 200);
            setTimeout(() => this.selectGoal('cognitive'), 400);
        }, 1000);
    }
    
    static handleGoalSelection(event) {
        const card = event.currentTarget;
        const goalId = card.dataset.goal;
        
        // Add ripple effect
        AnimationEngine.ripple(card, event);
        
        if (card.classList.contains('selected')) {
            this.deselectGoal(goalId);
        } else if (this.selectedGoals.size < this.maxGoals) {
            this.selectGoal(goalId);
        } else {
            this.showGoalLimitNotification();
        }
        
        this.updateDisplay();
    }
    
    static selectGoal(goalId) {
        this.selectedGoals.add(goalId);
        const card = document.querySelector(`[data-goal="${goalId}"]`);
        if (card) {
            card.classList.add('selected');
            AnimationEngine.scale(card, 0.95, 1.05, 200).then(() => {
                AnimationEngine.scale(card, 1.05, 1, 200);
            });
        }
    }
    
    static deselectGoal(goalId) {
        this.selectedGoals.delete(goalId);
        const card = document.querySelector(`[data-goal="${goalId}"]`);
        if (card) {
            card.classList.remove('selected');
        }
    }
    
    static handleGoalHover(event) {
        const card = event.currentTarget;
        if (!card.classList.contains('selected')) {
            card.style.transform = 'translateY(-8px) scale(1.02)';
        }
    }
    
    static handleGoalLeave(event) {
        const card = event.currentTarget;
        if (!card.classList.contains('selected')) {
            card.style.transform = 'translateY(0) scale(1)';
        }
    }
    
    static updateDisplay() {
        const goalsList = document.getElementById('selected-goals-list');
        const nextButton = document.getElementById('goals-next-btn');
        
        const goalNames = {
            'fat-loss': 'Accelerated Fat Loss',
            'muscle-gain': 'Muscle Development',
            'energy': 'Sustained Energy',
            'cognitive': 'Cognitive Enhancement',
            'stress': 'Stress Resilience',
            'sleep': 'Sleep Optimization',
            'longevity': 'Longevity & Anti-Aging',
            'immune': 'Immune Fortification',
            'recovery': 'Athletic Recovery'
        };
        
        if (this.selectedGoals.size === 0) {
            goalsList.innerHTML = '<p style="color: var(--gray-400); font-style: italic;">Choose your top 3 health priorities</p>';
        } else {
            goalsList.innerHTML = Array.from(this.selectedGoals).map(goalId => 
                `<div class="selected-goal-tag">${goalNames[goalId]}</div>`
            ).join('');
        }
        
        nextButton.disabled = this.selectedGoals.size === 0;
        AppState.selectedGoals = Array.from(this.selectedGoals);
    }
    
    static showGoalLimitNotification() {
        NotificationSystem.show(
            'You can select up to 3 primary goals for optimal results',
            'warning',
            'fas fa-exclamation-triangle'
        );
    }
}

// Enhanced Form System
class FormManager {
    static initialize() {
        this.setupSkinToneSelector();
        this.setupFormValidation();
        this.setupFormAnimations();
        this.loadExampleData();
    }
    
    static setupSkinToneSelector() {
        const skinOptions = document.querySelectorAll('.skin-option');
        
        skinOptions.forEach(option => {
            option.addEventListener('click', (e) => {
                skinOptions.forEach(opt => opt.classList.remove('selected'));
                option.classList.add('selected');
                AnimationEngine.scale(option, 0.9, 1.1, 150).then(() => {
                    AnimationEngine.scale(option, 1.1, 1, 150);
                });
                AppState.userProfile.skinTone = option.dataset.tone;
            });
        });
    }
    
    static setupFormValidation() {
        const inputs = document.querySelectorAll('input, select');
        
        inputs.forEach(input => {
            input.addEventListener('focus', (e) => {
                e.target.parentElement.classList.add('focused');
            });
            
            input.addEventListener('blur', (e) => {
                e.target.parentElement.classList.remove('focused');
                this.validateField(e.target);
            });
            
            input.addEventListener('input', (e) => {
                this.validateField(e.target);
            });
        });
    }
    
    static validateField(field) {
        const formGroup = field.parentElement;
        formGroup.classList.remove('error', 'success');
        
        if (field.type === 'number') {
            const min = parseInt(field.min);
            const max = parseInt(field.max);
            const value = parseInt(field.value);
            
            if (value && (value < min || value > max)) {
                formGroup.classList.add('error');
                return false;
            } else if (value && value >= min && value <= max) {
                formGroup.classList.add('success');
                return true;
            }
        } else if (field.required && !field.value.trim()) {
            formGroup.classList.add('error');
            return false;
        } else if (field.value.trim()) {
            formGroup.classList.add('success');
            return true;
        }
        
        return true;
    }
    
    static setupFormAnimations() {
        const formGroups = document.querySelectorAll('.form-group');
        
        formGroups.forEach((group, index) => {
            const input = group.querySelector('input, select');
            if (input) {
                input.addEventListener('focus', () => {
                    AnimationEngine.scale(group, 0.98, 1.02, 200);
                });
                
                input.addEventListener('blur', () => {
                    AnimationEngine.scale(group, 1.02, 1, 200);
                });
            }
        });
    }
    
    static loadExampleData() {
        AppState.userProfile = {
            age: 49,
            gender: 'male',
            weight: 80,
            height: 175,
            location: 'London, UK',
            skinTone: '3',
            activityLevel: 'active'
        };
        
        setTimeout(() => {
            document.getElementById('age').value = 49;
            document.getElementById('weight').value = 80;
            document.getElementById('height').value = 175;
            document.getElementById('location').value = 'London, UK';
            document.getElementById('activity-level').value = 'active';
        }, 100);
    }
    
    static collectData() {
        return {
            age: parseInt(document.getElementById('age').value),
            gender: document.getElementById('gender').value,
            weight: parseInt(document.getElementById('weight').value),
            height: parseInt(document.getElementById('height').value),
            location: document.getElementById('location').value,
            skinTone: document.querySelector('.skin-option.selected')?.dataset.tone,
            activityLevel: document.getElementById('activity-level').value
        };
    }
}

// Enhanced Bloodwork System
class BloodworkManager {
    static initialize() {
        this.setupFileUpload();
        this.setupExampleData();
    }
    
    static setupFileUpload() {
        const uploadArea = document.getElementById('bloodwork-upload');
        const fileInput = document.getElementById('file-input');
        const continueBtn = document.getElementById('bloodwork-continue-btn');
        
        // Drag and drop functionality
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('drag-over');
        });
        
        uploadArea.addEventListener('dragleave', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
        });
        
        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
            const files = e.dataTransfer.files;
            this.handleFiles(files);
        });
        
        fileInput.addEventListener('change', (e) => {
            this.handleFiles(e.target.files);
        });
    }
    
    static handleFiles(files) {
        const continueBtn = document.getElementById('bloodwork-continue-btn');
        
        if (files.length > 0) {
            NotificationSystem.show(
                `${files.length} file(s) uploaded successfully! Processing...`,
                'success',
                'fas fa-check-circle'
            );
            
            // Simulate processing delay
            setTimeout(() => {
                continueBtn.disabled = false;
                continueBtn.innerHTML = `
                    Analyze My Results
                    <i class="fas fa-chart-line"></i>
                `;
            }, 1500);
            
            AppState.bloodworkData = {
                files: Array.from(files).map(f => f.name),
                uploadedAt: new Date().toISOString()
            };
        }
    }
    
    static setupExampleData() {
        const exampleBtn = document.querySelector('button[onclick="loadExampleBloodwork()"]');
        if (exampleBtn) {
            exampleBtn.addEventListener('click', () => {
                this.loadExampleBloodwork();
            });
        }
    }
    
    static loadExampleBloodwork() {
        const continueBtn = document.getElementById('bloodwork-continue-btn');
        
        // Show loading animation
        NotificationSystem.show(
            'Loading comprehensive example bloodwork...',
            'info',
            'fas fa-spinner fa-spin'
        );
        
        setTimeout(() => {
            AppState.bloodworkData = {
                example: true,
                biomarkers: {
                    hba1c: { value: 4.9, unit: '%', status: 'excellent', range: '<5.7' },
                    totalCholesterol: { value: 241.1, unit: 'mg/dL', status: 'elevated', range: '<200' },
                    ldlCholesterol: { value: 170.98, unit: 'mg/dL', status: 'high', range: '<100' },
                    hdlCholesterol: { value: 51.14, unit: 'mg/dL', status: 'good', range: '>40' },
                    testosterone: { value: 30.5, unit: 'nmol/L', status: 'optimal', range: '10.4-34.7' },
                    vitaminD: { value: 41.8, unit: 'ng/mL', status: 'adequate', range: '30-50' },
                    ferritin: { value: 220, unit: 'ng/mL', status: 'good', range: '12-300' },
                    b12: { value: 843, unit: 'pg/mL', status: 'high', range: '197-771' }
                }
            };
            
            continueBtn.disabled = false;
            continueBtn.innerHTML = `
                Analyze Example Results
                <i class="fas fa-chart-line"></i>
            `;
            
            NotificationSystem.show(
                'Example bloodwork loaded! Ready for analysis.',
                'success',
                'fas fa-check-circle'
            );
        }, 1200);
    }
}

// Enhanced Loading System
class LoadingManager {
    static show(message = 'Processing...', steps = []) {
        const loadingScreen = document.getElementById('loading-screen');
        if (!loadingScreen) return;
        
        loadingScreen.classList.add('active');
        
        if (steps.length > 0) {
            this.animateSteps(steps);
        }
        
        // Simulate realistic loading time
        return new Promise(resolve => {
            setTimeout(resolve, 3000);
        });
    }
    
    static hide() {
        const loadingScreen = document.getElementById('loading-screen');
        if (loadingScreen) {
            loadingScreen.classList.remove('active');
        }
    }
    
    static animateSteps(steps) {
        const stepElements = document.querySelectorAll('.loading-step');
        
        steps.forEach((step, index) => {
            setTimeout(() => {
                stepElements.forEach(el => el.classList.remove('active'));
                if (stepElements[index]) {
                    stepElements[index].classList.add('active');
                }
            }, index * 1000);
        });
    }
}

// Enhanced Notification System
class NotificationSystem {
    static notifications = [];
    static maxNotifications = 3;
    
    static show(message, type = 'info', icon = 'fas fa-info-circle', duration = 4000) {
        const notification = this.create(message, type, icon);
        document.body.appendChild(notification);
        
        // Animate in
        requestAnimationFrame(() => {
            notification.classList.add('show');
        });
        
        // Auto remove
        setTimeout(() => {
            this.remove(notification);
        }, duration);
        
        // Limit notifications
        this.notifications.push(notification);
        if (this.notifications.length > this.maxNotifications) {
            this.remove(this.notifications.shift());
        }
        
        return notification;
    }
    
    static create(message, type, icon) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="${icon}"></i>
                <span>${message}</span>
            </div>
        `;
        
        // Add click to dismiss
        notification.addEventListener('click', () => {
            this.remove(notification);
        });
        
        return notification;
    }
    
    static remove(notification) {
        if (notification && notification.parentNode) {
            notification.classList.remove('show');
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
                this.notifications = this.notifications.filter(n => n !== notification);
            }, 300);
        }
    }
}

// Enhanced Button System
class ButtonManager {
    static initialize() {
        this.setupButtons();
        this.setupRippleEffects();
    }
    
    static setupButtons() {
        const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button');
        
        buttons.forEach(button => {
            button.addEventListener('mouseenter', (e) => {
                if (!button.disabled) {
                    AnimationEngine.scale(button, 1, 1.02, 150);
                }
            });
            
            button.addEventListener('mouseleave', (e) => {
                if (!button.disabled) {
                    AnimationEngine.scale(button, 1.02, 1, 150);
                }
            });
            
            button.addEventListener('mousedown', (e) => {
                if (!button.disabled) {
                    AnimationEngine.scale(button, 1.02, 0.98, 100);
                }
            });
            
            button.addEventListener('mouseup', (e) => {
                if (!button.disabled) {
                    AnimationEngine.scale(button, 0.98, 1, 150);
                }
            });
        });
    }
    
    static setupRippleEffects() {
        const rippleButtons = document.querySelectorAll('.btn-primary, .goal-card, .option-card');
        
        rippleButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                AnimationEngine.ripple(button, e);
            });
        });
    }
}

// Enhanced Analytics
class AnalyticsManager {
    static trackEvent(event, properties = {}) {
        const data = {
            event,
            properties: {
                ...properties,
                timestamp: new Date().toISOString(),
                sessionTime: Date.now() - AppState.startTime,
                currentScreen: AppState.currentScreen
            }
        };
        
        console.log('Analytics:', data);
        // In production, send to analytics service
    }
    
    static trackScreenView(screenId) {
        this.trackEvent('screen_view', {
            screen: screenId,
            goals_selected: AppState.selectedGoals.length,
            profile_completed: Object.keys(AppState.userProfile).length > 0,
            bloodwork_uploaded: !!AppState.bloodworkData
        });
    }
    
    static trackGoalSelection(goalId, action) {
        this.trackEvent('goal_interaction', {
            goal: goalId,
            action,
            total_selected: AppState.selectedGoals.length
        });
    }
}

// Global Functions (for onclick handlers)
function startJourney() {
    AnalyticsManager.trackEvent('cta_clicked', { location: 'hero' });
    ScreenManager.goToScreen('goals-screen');
}

function goToScreen(screenId) {
    ScreenManager.goToScreen(screenId);
}

function triggerFileUpload() {
    document.getElementById('file-input').click();
}

function loadExampleBloodwork() {
    BloodworkManager.loadExampleBloodwork();
}

// Enhanced Initialization
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Vibrantly Supplements Premium - Initializing...');
    
    // Initialize all systems
    GoalsManager.initialize();
    FormManager.initialize();
    BloodworkManager.initialize();
    ButtonManager.initialize();
    
    // Setup CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes rippleEffect {
            to {
                transform: scale(1);
                opacity: 0;
            }
        }
        
        .drag-over {
            background: rgba(99, 102, 241, 0.1) !important;
            border-color: var(--primary-500) !important;
            transform: scale(1.02) !important;
        }
        
        .form-group.focused input,
        .form-group.focused select {
            border-color: var(--primary-500) !important;
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1) !important;
        }
        
        .form-group.error input,
        .form-group.error select {
            border-color: var(--error) !important;
            box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1) !important;
        }
        
        .form-group.success input,
        .form-group.success select {
            border-color: var(--success) !important;
            box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.1) !important;
        }
        
        .loading-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
            padding: var(--space-8);
        }
        
        .dna-helix {
            width: 100px;
            height: 100px;
            position: relative;
            margin-bottom: var(--space-8);
        }
        
        .dna-strand {
            position: absolute;
            width: 4px;
            height: 100%;
            background: var(--gradient-primary);
            border-radius: 2px;
            animation: dnaRotate 2s linear infinite;
        }
        
        .dna-strand.strand-1 {
            left: 20px;
            animation-delay: 0s;
        }
        
        .dna-strand.strand-2 {
            right: 20px;
            animation-delay: 1s;
        }
        
        @keyframes dnaRotate {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }
        
        .loading-steps {
            display: flex;
            flex-direction: column;
            gap: var(--space-4);
            margin-top: var(--space-8);
            max-width: 300px;
        }
        
        .loading-step {
            display: flex;
            align-items: center;
            gap: var(--space-3);
            padding: var(--space-3);
            background: rgba(255, 255, 255, 0.1);
            border-radius: var(--radius-lg);
            color: var(--gray-400);
            transition: all var(--duration-300) var(--ease-out);
        }
        
        .loading-step.active {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            transform: scale(1.05);
        }
        
        .privacy-notice {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: var(--space-6);
            border-radius: var(--radius-xl);
            margin: var(--space-8) 0;
            display: flex;
            align-items: center;
            gap: var(--space-4);
            border: 1px solid var(--primary-200);
        }
        
        .privacy-notice i {
            color: var(--primary-500);
            font-size: var(--font-size-xl);
        }
        
        .privacy-notice p {
            margin: 0;
            color: var(--gray-700);
            font-size: var(--font-size-sm);
            line-height: 1.5;
        }
        
        .supported-labs {
            margin-top: var(--space-8);
            padding-top: var(--space-6);
            border-top: 1px solid var(--gray-200);
        }
        
        .supported-labs h4 {
            margin-bottom: var(--space-4);
            color: var(--gray-800);
            font-size: var(--font-size-base);
            display: flex;
            align-items: center;
            gap: var(--space-2);
        }
        
        .lab-logos {
            display: flex;
            flex-wrap: wrap;
            gap: var(--space-2);
        }
        
        .lab-tag {
            background: var(--primary-100);
            color: var(--primary-700);
            padding: var(--space-1) var(--space-3);
            border-radius: var(--radius-full);
            font-size: var(--font-size-xs);
            font-weight: 600;
        }
        
        .background-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }
        
        .floating-element {
            position: absolute;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
            animation: floatBackground 20s ease-in-out infinite;
        }
        
        .floating-element.element-1 {
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }
        
        .floating-element.element-2 {
            top: 60%;
            right: 10%;
            animation-delay: 7s;
        }
        
        .floating-element.element-3 {
            bottom: 20%;
            left: 30%;
            animation-delay: 14s;
        }
        
        @keyframes floatBackground {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -30px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }
    `;
    document.head.appendChild(style);
    
    // Track initial page load
    AnalyticsManager.trackEvent('app_loaded');
    
    // Setup keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            // Close any open modals or notifications
            const notifications = document.querySelectorAll('.notification');
            notifications.forEach(notif => NotificationSystem.remove(notif));
        }
        
        if (e.key === 'Enter' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
            const activeButton = document.querySelector('.btn-primary:not(:disabled)');
            if (activeButton) {
                activeButton.click();
            }
        }
    });
    
    // Setup accessibility improvements
    document.querySelectorAll('[data-goal]').forEach(card => {
        card.setAttribute('role', 'button');
        card.setAttribute('tabindex', '0');
        card.setAttribute('aria-pressed', 'false');
        
        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                card.click();
            }
        });
    });
    
    // Performance monitoring
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.getEntriesByType('navigation')[0];
                AnalyticsManager.trackEvent('performance', {
                    loadTime: Math.round(perfData.loadEventEnd - perfData.fetchStart),
                    domReady: Math.round(perfData.domContentLoadedEventEnd - perfData.fetchStart),
                    firstPaint: performance.getEntriesByType('paint').find(p => p.name === 'first-paint')?.startTime || 0
                });
            }, 0);
        });
    }
    
    console.log('✨ Premium Experience Ready');
    
    // Show welcome message
    setTimeout(() => {
        NotificationSystem.show(
            'Welcome to the future of personalized supplementation!',
            'info',
            'fas fa-sparkles',
            6000
        );
    }, 2000);
});