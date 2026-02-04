/**
 * Everfit Webhook Handler for Vibrantly Integration
 * Handles real-time events from Everfit API
 */

const express = require('express');
const crypto = require('crypto');

class EverfitWebhookHandler {
    constructor(options = {}) {
        this.app = express();
        this.port = options.port || 3000;
        this.webhookSecret = options.webhookSecret || 'your-webhook-secret';
        this.vibrantly = options.vibrantly || null; // Vibrantly API client
        
        this.setupMiddleware();
        this.setupRoutes();
    }

    setupMiddleware() {
        // Middleware to parse JSON bodies
        this.app.use(express.json());
        
        // Webhook signature verification middleware
        this.app.use('/webhook/everfit', (req, res, next) => {
            const signature = req.headers['x-everfit-signature'];
            const payload = JSON.stringify(req.body);
            const expectedSignature = this.generateSignature(payload);
            
            if (signature !== expectedSignature) {
                console.log('⚠️ Invalid webhook signature');
                return res.status(401).json({ error: 'Invalid signature' });
            }
            
            next();
        });
    }

    setupRoutes() {
        // Main webhook endpoint
        this.app.post('/webhook/everfit', async (req, res) => {
            try {
                await this.handleWebhook(req.body);
                res.status(200).json({ status: 'success' });
            } catch (error) {
                console.error('Webhook handling error:', error);
                res.status(500).json({ error: 'Internal server error' });
            }
        });

        // Health check endpoint
        this.app.get('/health', (req, res) => {
            res.json({
                status: 'healthy',
                timestamp: new Date().toISOString(),
                service: 'everfit-webhook-handler'
            });
        });

        // Demo endpoint to simulate webhooks
        this.app.post('/demo/webhook', async (req, res) => {
            console.log('🎭 Demo webhook received:', req.body);
            await this.handleWebhook(req.body);
            res.json({ status: 'demo processed' });
        });
    }

    async handleWebhook(eventData) {
        const { event, data, timestamp } = eventData;
        
        console.log(`📡 Webhook received: ${event}`, {
            timestamp: new Date(timestamp).toISOString(),
            clientId: data.id,
            clientName: `${data.firstName} ${data.lastName}`
        });

        switch (event) {
            case 'client.connected':
                await this.handleClientConnected(data);
                break;
                
            case 'client.accessed-app':
                await this.handleClientAccessedApp(data);
                break;
                
            case 'workout.started':
                await this.handleWorkoutStarted(data);
                break;
                
            case 'workout.completed':
                await this.handleWorkoutCompleted(data);
                break;
                
            case 'program.assigned':
                await this.handleProgramAssigned(data);
                break;
                
            default:
                console.log('🤷‍♂️ Unknown event type:', event);
        }
    }

    async handleClientConnected(data) {
        console.log(`🎉 Client connected: ${data.firstName} ${data.lastName}`);
        
        // Update Vibrantly dashboard
        if (this.vibrantly) {
            await this.vibrantly.updateClientStatus(data.id, 'connected');
        }

        // Send notification to Eliza
        await this.notifyEliza({
            type: 'client_connected',
            message: `🎉 ${data.firstName} just connected to Everfit! Ready to start their fitness journey.`,
            clientData: data
        });
    }

    async handleClientAccessedApp(data) {
        console.log(`👋 Client accessed app: ${data.firstName} ${data.lastName}`);
        
        // Update last activity in Vibrantly
        if (this.vibrantly) {
            await this.vibrantly.updateLastActivity(data.id, new Date());
        }

        // Update activity status
        await this.notifyEliza({
            type: 'client_activity',
            message: `💪 ${data.firstName} is active and ready to workout! Time to encourage them.`,
            clientData: data
        });
    }

    async handleWorkoutStarted(data) {
        console.log(`🏃‍♂️ Workout started:`, data);
        
        // Log workout start in Vibrantly
        if (this.vibrantly) {
            await this.vibrantly.logWorkoutStart({
                clientId: data.clientId,
                workoutId: data.workoutId,
                workoutName: data.workoutName,
                startTime: new Date(data.startTime),
                expectedDuration: data.expectedDuration
            });
        }

        // Notify Eliza to provide encouragement
        await this.notifyEliza({
            type: 'workout_started',
            message: `🔥 ${data.clientName} just started "${data.workoutName}"! Time for some motivational coaching.`,
            workoutData: data
        });
    }

    async handleWorkoutCompleted(data) {
        console.log(`✅ Workout completed:`, data);
        
        // Log detailed workout completion in Vibrantly
        if (this.vibrantly) {
            await this.vibrantly.logWorkoutCompletion({
                clientId: data.clientId,
                workoutId: data.workoutId,
                workoutName: data.workoutName,
                completedAt: new Date(data.completedAt),
                duration: data.duration,
                exercises: data.exercises,
                performance: data.performance
            });
        }

        // Generate AI analysis and encouragement
        await this.generateWorkoutAnalysis(data);
    }

    async handleProgramAssigned(data) {
        console.log(`📋 Program assigned:`, data);
        
        // Update Vibrantly with new program
        if (this.vibrantly) {
            await this.vibrantly.assignProgram({
                clientId: data.clientId,
                programId: data.programId,
                programName: data.programName,
                startDate: new Date(data.startDate),
                duration: data.duration
            });
        }

        await this.notifyEliza({
            type: 'program_assigned',
            message: `🎯 New program "${data.programName}" assigned to ${data.clientName}! Let's set some goals.`,
            programData: data
        });
    }

    async generateWorkoutAnalysis(workoutData) {
        // This would integrate with Eliza's AI to generate personalized feedback
        const analysis = {
            performance: this.analyzePerformance(workoutData),
            recommendations: this.generateRecommendations(workoutData),
            nextWorkout: this.suggestNextWorkout(workoutData)
        };

        await this.notifyEliza({
            type: 'workout_analysis',
            message: `📊 Workout analysis complete for ${workoutData.clientName}`,
            analysis,
            workoutData
        });
    }

    analyzePerformance(workoutData) {
        // Analyze workout performance metrics
        const { exercises, duration, expectedDuration } = workoutData;
        
        return {
            completionRate: (duration / expectedDuration) * 100,
            exercisesCompleted: exercises.filter(e => e.completed).length,
            totalExercises: exercises.length,
            averageIntensity: exercises.reduce((sum, e) => sum + (e.intensity || 0), 0) / exercises.length,
            improvement: this.calculateImprovement(workoutData)
        };
    }

    generateRecommendations(workoutData) {
        // Generate personalized recommendations based on performance
        const recommendations = [];
        
        if (workoutData.duration < workoutData.expectedDuration * 0.8) {
            recommendations.push("Consider increasing workout duration gradually");
        }
        
        if (workoutData.exercises.some(e => e.difficulty === 'too_easy')) {
            recommendations.push("Ready to increase intensity on some exercises");
        }
        
        return recommendations;
    }

    suggestNextWorkout(workoutData) {
        // AI-powered next workout suggestion
        return {
            type: 'strength_training',
            focus: 'upper_body',
            duration: 30,
            intensity: 'moderate',
            reason: 'Balance after lower body focus'
        };
    }

    calculateImprovement(workoutData) {
        // Calculate improvement from previous workouts
        // This would query historical data
        return {
            strengthGain: '5%',
            enduranceGain: '8%',
            consistencyScore: 85
        };
    }

    async notifyEliza(notification) {
        // Send notification to Eliza for processing
        console.log(`🤖 Notifying Eliza:`, notification.message);
        
        // In real implementation, this would:
        // 1. Send message to Eliza's processing queue
        // 2. Trigger Eliza to generate appropriate response
        // 3. Update Vibrantly dashboard with new insights
        
        // Mock implementation
        setTimeout(() => {
            console.log(`💜 Eliza response: Generated personalized feedback for ${notification.clientData?.firstName || 'client'}`);
        }, 1000);
    }

    generateSignature(payload) {
        // Generate HMAC signature for webhook verification
        return crypto
            .createHmac('sha256', this.webhookSecret)
            .update(payload, 'utf8')
            .digest('hex');
    }

    start() {
        this.app.listen(this.port, () => {
            console.log(`🚀 Everfit webhook handler running on port ${this.port}`);
            console.log(`📡 Webhook endpoint: http://localhost:${this.port}/webhook/everfit`);
            console.log(`🩺 Health check: http://localhost:${this.port}/health`);
        });
    }
}

// Demo usage
if (require.main === module) {
    const webhookHandler = new EverfitWebhookHandler({
        port: 3000,
        webhookSecret: 'demo-secret-key'
    });

    webhookHandler.start();

    // Simulate some demo webhooks after startup
    setTimeout(() => {
        console.log('\n🎭 Simulating demo webhooks...\n');
        
        // Simulate client connection
        webhookHandler.handleWebhook({
            event: 'client.connected',
            data: {
                id: 'client_vishen_001',
                firstName: 'Vishen',
                lastName: 'Lakhiani',
                email: 'vishen@mindvalley.com',
                isArchived: false,
                status: 1,
                client_connection: 1
            },
            timestamp: Date.now()
        });

        // Simulate workout completion after 3 seconds
        setTimeout(() => {
            webhookHandler.handleWebhook({
                event: 'workout.completed',
                data: {
                    clientId: 'client_vishen_001',
                    clientName: 'Vishen Lakhiani',
                    workoutId: 'hiit_001',
                    workoutName: 'HIIT Strength Circuit',
                    completedAt: Date.now(),
                    duration: 22,
                    expectedDuration: 20,
                    exercises: [
                        { name: 'Burpees', completed: true, reps: 15, intensity: 'high' },
                        { name: 'Mountain Climbers', completed: true, reps: 20, intensity: 'high' },
                        { name: 'Push-ups', completed: true, reps: 12, intensity: 'moderate' }
                    ],
                    performance: {
                        heartRate: { avg: 145, max: 168 },
                        calories: 280,
                        effort: 8.5
                    }
                },
                timestamp: Date.now()
            });
        }, 3000);

    }, 2000);
}

module.exports = EverfitWebhookHandler;