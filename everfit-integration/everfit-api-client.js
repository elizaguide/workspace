/**
 * Everfit API Integration Client
 * Proof of Concept for Vibrantly Health Dashboard
 */

class EverfitAPIClient {
    constructor(apiToken) {
        this.apiToken = apiToken;
        this.baseURL = 'https://public-api.everfit.io/public-api';
        this.headers = {
            'api-token': apiToken,
            'Content-Type': 'application/json'
        };
    }

    /**
     * Get all available workout collections
     */
    async getWorkoutCollections(page = 1, limit = 20) {
        try {
            const response = await fetch(`${this.baseURL}/on-demand-workout/get-list-collection?page=${page}&limit=${limit}`, {
                method: 'GET',
                headers: this.headers
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error fetching workout collections:', error);
            throw error;
        }
    }

    /**
     * Get program library with workout videos
     */
    async getProgramLibrary() {
        try {
            const response = await fetch(`${this.baseURL}/programs`, {
                method: 'GET',
                headers: this.headers
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error fetching program library:', error);
            throw error;
        }
    }

    /**
     * Add client to Everfit system
     */
    async addClient(clientData) {
        try {
            const response = await fetch(`${this.baseURL}/add-new-client`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify({
                    firstName: clientData.firstName,
                    lastName: clientData.lastName,
                    email: clientData.email,
                    type: clientData.type || 'Online',
                    sendMail: clientData.sendMail || true,
                    trainerEmail: clientData.trainerEmail
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error adding client:', error);
            throw error;
        }
    }

    /**
     * Assign workout collection to client
     */
    async assignWorkoutToClient(clientId, collectionId) {
        try {
            const response = await fetch(`${this.baseURL}/on-demand-workout/add-client-to-workout-collection`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify({
                    clientId: clientId,
                    collectionId: collectionId
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error assigning workout:', error);
            throw error;
        }
    }

    /**
     * Get client's assigned workout collections
     */
    async getClientWorkouts(clientId, page = 1, limit = 10) {
        try {
            const response = await fetch(`${this.baseURL}/on-demand-workout/get-list-collection-of-client?page=${page}&limit=${limit}&client=${clientId}`, {
                method: 'GET',
                headers: this.headers
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error fetching client workouts:', error);
            throw error;
        }
    }

    /**
     * Setup webhook endpoint for real-time updates
     */
    setupWebhook(webhookURL) {
        console.log(`Webhook configured for: ${webhookURL}`);
        console.log('Available events: client.connected, client.accessed-app');
        
        // This would be configured on Everfit's side
        return {
            webhookURL,
            events: ['client.connected', 'client.accessed-app'],
            status: 'configured'
        };
    }
}

// Mock data for demonstration
const MOCK_WORKOUT_COLLECTIONS = {
    "data": {
        "list": [
            {
                "name": "HIIT Strength Circuit",
                "type": "High Intensity",
                "id": "hiit_001",
                "description": "20-minute high-intensity strength training",
                "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "difficulty": "Intermediate",
                "duration": "20 minutes",
                "equipment": ["Dumbbells", "Mat"]
            },
            {
                "name": "Yoga Flow Fundamentals", 
                "type": "Flexibility",
                "id": "yoga_001",
                "description": "30-minute beginner yoga flow",
                "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "difficulty": "Beginner",
                "duration": "30 minutes",
                "equipment": ["Yoga Mat"]
            },
            {
                "name": "Cardio Boxing Blast",
                "type": "Cardio",
                "id": "boxing_001", 
                "description": "45-minute boxing cardio workout",
                "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "difficulty": "Advanced",
                "duration": "45 minutes",
                "equipment": ["Boxing Gloves", "Heavy Bag"]
            },
            {
                "name": "Core Power Pilates",
                "type": "Strength",
                "id": "pilates_001",
                "description": "25-minute core-focused pilates",
                "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "difficulty": "Intermediate", 
                "duration": "25 minutes",
                "equipment": ["Mat", "Pilates Ball"]
            }
        ],
        "total": 4,
        "page": 1,
        "limit": 10
    }
};

const MOCK_PROGRAMS = {
    "data": [
        {
            "id": "program_strength_001",
            "title": "8-Week Strength Foundation",
            "description": "Progressive strength training program designed for beginners to intermediate. Build foundational strength with compound movements.",
            "weeks": 8,
            "total_workouts": 24,
            "difficulty": "Beginner-Intermediate",
            "workouts": [
                {
                    "week": 1,
                    "day": 1,
                    "name": "Full Body Foundation",
                    "exercises": [
                        {
                            "name": "Bodyweight Squats",
                            "sets": 3,
                            "reps": "12-15",
                            "videoUrl": "https://www.youtube.com/watch?v=YaXPRqUwItQ",
                            "thumbnail": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=300&h=200&fit=crop"
                        },
                        {
                            "name": "Push-ups",
                            "sets": 3,
                            "reps": "8-12",
                            "videoUrl": "https://www.youtube.com/watch?v=IODxDxX7oi4",
                            "thumbnail": "https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?w=300&h=200&fit=crop"
                        }
                    ]
                }
            ]
        },
        {
            "id": "program_cardio_001", 
            "title": "4-Week Cardio Kickstart",
            "description": "High-energy cardiovascular training program to boost endurance and burn calories effectively.",
            "weeks": 4,
            "total_workouts": 16,
            "difficulty": "All Levels",
            "workouts": [
                {
                    "week": 1,
                    "day": 1, 
                    "name": "HIIT Starter",
                    "exercises": [
                        {
                            "name": "Jumping Jacks",
                            "sets": 4,
                            "reps": "30 seconds",
                            "videoUrl": "https://www.youtube.com/watch?v=2W4ZNSwoW_4",
                            "thumbnail": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=300&h=200&fit=crop"
                        }
                    ]
                }
            ]
        }
    ]
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { EverfitAPIClient, MOCK_WORKOUT_COLLECTIONS, MOCK_PROGRAMS };
}