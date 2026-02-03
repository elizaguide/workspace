#!/usr/bin/env python3
"""
Spanish Daily Lesson Generator
Generates personalized Spanish lessons based on user level and progress
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

class SpanishLessonGenerator:
    def __init__(self, progress_file="spanish_progress.json"):
        self.progress_file = progress_file
        self.load_progress()
        
    def load_progress(self):
        """Load user progress from file"""
        try:
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        except FileNotFoundError:
            self.progress = {
                "level": 1,
                "words_learned": [],
                "current_lesson": 1,
                "last_lesson_date": None,
                "retention_scores": {}
            }
    
    def save_progress(self):
        """Save progress to file"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def get_lesson_vocabulary(self, lesson_num, count=4):
        """Get vocabulary for specific lesson number"""
        
        # Vocabulary organized by lesson progression
        lesson_vocab = {
            # Foundation lessons (1-20)
            1: [
                {"spanish": "Buenos días", "english": "Good morning", "phonetic": "BWAY-nos DEE-ahs"},
                {"spanish": "¿Cómo estás?", "english": "How are you?", "phonetic": "KO-mo es-TAHS"},
                {"spanish": "Muy bien", "english": "Very well", "phonetic": "mwee bee-EN"},
                {"spanish": "Gracias", "english": "Thank you", "phonetic": "GRAH-see-ahs"}
            ],
            2: [
                {"spanish": "Un café, por favor", "english": "One coffee, please", "phonetic": "oon kah-FEH por fah-VOR"},
                {"spanish": "¿Tienen leche de avena?", "english": "Do you have oat milk?", "phonetic": "tee-EH-nen LEH-cheh deh ah-VEH-nah"},
                {"spanish": "Sin azúcar", "english": "Without sugar", "phonetic": "seen ah-SOO-kar"},
                {"spanish": "Mi amor", "english": "My love", "phonetic": "mee ah-MOR"}
            ],
            3: [
                {"spanish": "¿Cómo dormiste?", "english": "How did you sleep?", "phonetic": "KO-mo dor-MEES-teh"},
                {"spanish": "Te quiero mucho", "english": "I love you so much", "phonetic": "teh kee-EH-ro MOO-choh"},
                {"spanish": "¿Listos para el día?", "english": "Ready for the day?", "phonetic": "LEES-tos PAH-rah el DEE-ah"},
                {"spanish": "Hasta luego", "english": "See you later", "phonetic": "AHS-tah LWAY-go"}
            ],
            # Business Spanish (lessons 21-40)
            21: [
                {"spanish": "Mucho gusto", "english": "Nice to meet you", "phonetic": "MOO-choh GOOS-toh"},
                {"spanish": "Soy el CEO de Mindvalley", "english": "I'm the CEO of Mindvalley", "phonetic": "soy el SEH-oh deh"},
                {"spanish": "¿En qué puedo ayudarle?", "english": "How can I help you?", "phonetic": "en keh PWEH-doh ah-yoo-DAHR-leh"},
                {"spanish": "Perfecto", "english": "Perfect", "phonetic": "per-FEK-toh"}
            ]
        }
        
        # Get vocab for current lesson, or generate from higher levels
        if lesson_num in lesson_vocab:
            vocab = lesson_vocab[lesson_num]
        else:
            # For higher lessons, mix business and advanced vocab
            vocab = [
                {"spanish": "Estrategia", "english": "Strategy", "phonetic": "es-trah-TEH-hee-ah"},
                {"spanish": "Crecimiento personal", "english": "Personal growth", "phonetic": "kreh-see-mee-EN-toh per-so-NAHL"},
                {"spanish": "Transformación", "english": "Transformation", "phonetic": "trans-for-mah-see-OHN"},
                {"spanish": "Consciencia", "english": "Consciousness", "phonetic": "kon-see-EN-see-ah"}
            ]
        
        return vocab[:count]
    
    def generate_lesson(self, lesson_type="daily"):
        """Generate a complete lesson"""
        lesson_num = self.progress["current_lesson"]
        vocabulary = self.get_lesson_vocabulary(lesson_num)
        
        lesson = {
            "lesson_number": lesson_num,
            "date": datetime.now().isoformat(),
            "type": lesson_type,
            "vocabulary": vocabulary,
            "practice_challenge": self.generate_challenge(vocabulary),
            "cultural_note": self.get_cultural_note(lesson_num),
            "review_words": self.get_review_words()
        }
        
        return lesson
    
    def generate_challenge(self, vocabulary):
        """Generate practice challenge for vocabulary"""
        challenges = [
            f"Use '{vocabulary[0]['spanish']}' in a sentence with your family",
            f"Practice ordering coffee using '{vocabulary[1]['spanish']}'",
            f"Greet someone tomorrow morning with '{vocabulary[0]['spanish']}'",
            f"Record yourself saying all today's words with confidence"
        ]
        
        return random.choice(challenges)
    
    def get_cultural_note(self, lesson_num):
        """Get cultural context for lesson"""
        notes = [
            "In Spanish culture, greeting people warmly is essential for building trust",
            "Coffee culture varies greatly between Spain and Latin America",
            "'Mi amor' is commonly used between family members, not just romantic partners",
            "Business relationships in Spanish-speaking countries often start with personal connection"
        ]
        
        return notes[(lesson_num - 1) % len(notes)]
    
    def get_review_words(self):
        """Get words to review based on spaced repetition"""
        # Simple spaced repetition: review words from 1, 3, 7, and 14 days ago
        review_intervals = [1, 3, 7, 14]
        review_words = []
        
        for interval in review_intervals:
            target_date = (datetime.now() - timedelta(days=interval)).strftime("%Y-%m-%d")
            # In a real implementation, this would look up words learned on that date
            
        return review_words
    
    def advance_lesson(self):
        """Move to next lesson and update progress"""
        self.progress["current_lesson"] += 1
        self.progress["last_lesson_date"] = datetime.now().isoformat()
        self.save_progress()

def main():
    """Generate and display today's lesson"""
    generator = SpanishLessonGenerator()
    lesson = generator.generate_lesson()
    
    print("🇪🇸 SPANISH LESSON #{} 🇪🇸".format(lesson["lesson_number"]))
    print("=" * 40)
    
    print("\n📚 TODAY'S VOCABULARY:")
    for word in lesson["vocabulary"]:
        print(f"• {word['spanish']} - {word['english']}")
        print(f"  Pronunciation: {word['phonetic']}\n")
    
    print(f"🎯 PRACTICE CHALLENGE:")
    print(f"{lesson['practice_challenge']}\n")
    
    print(f"🌎 CULTURAL NOTE:")
    print(f"{lesson['cultural_note']}\n")
    
    # Advance to next lesson
    generator.advance_lesson()
    
    print("✅ Lesson completed! See you tomorrow for lesson #{}\n".format(generator.progress["current_lesson"]))

if __name__ == "__main__":
    main()